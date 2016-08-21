import json
import re
from collections import namedtuple
from .concept import ProgrammingConcept, EnvironmentConcept, GameConcept, BlockConcept
from core.data.managers import ToolboxManager, BlockManager
from core.data.fixtures.concepts import CONCEPTS


class Task(object):
    """ Model for a task (exercise)
    """

    def __init__(self, pk, title, solution, revision=1, maze_settings='{}',
                 workspace_settings='{}'):
        self.pk = pk
        self.title = title
        self.revision = revision
        self.maze_settings = maze_settings
        self.workspace_settings = workspace_settings
        self.solution = solution
        assert maze_settings is not None and solution is not None
        self.infer_attributes_from_setting_and_solution()

    export_class = namedtuple('Task', ['task_id', 'title', 'level',
                                       'concepts_ids', 'blocks_ids',
                                       'maze_settings', 'solution'])

    toolbox = None

    _blocks_limit = None

    _contained_concepts = None

    #  constants describing semantic of a maze grid
    _COLORS_FIELDS = [3, 4, 5]
    _FREE_FIELDS = [0, 2, 3, 4, 5]
    _PIT_FIELD = 6

    # from which level to use block limit
    _BLOCK_LIMIT_LEVEL = 3

    def get_toolbox(self, complete_if_none=True):
        if not self.toolbox and complete_if_none:
            return ToolboxManager.get_complete_toolbox()
        return self.toolbox

    def get_level(self):
        toolbox = self.get_toolbox()
        return toolbox.level if toolbox else 1

    def get_contained_concepts(self):
        return self._contained_concepts

    def get_programming_concepts(self):
        return filter(lambda e: isinstance(e, ProgrammingConcept), self._contained_concepts)

    def get_required_blocks(self):
        return self.get_toolbox(complete_if_none=True).get_all_blocks()

    def get_blocks_limit(self):
        """ Return blocks limit or None, if there is no limit on blocks
        """
        return self._blocks_limit

    def contains_tokens(self):
        return bool(self.get_tokens())

    def get_tokens(self):
        """ Return list of tokens or None, if there are no tokens
        """
        tokens = self.get_maze_settings().get('tokens', None)
        return tokens if tokens else None

    def contains_blocks_limit(self):
        return self.get_blocks_limit() is not None

    def contains_pits(self):
        """ Return True if the task contains pits
        """
        return any(self._PIT_FIELD in row for row in self.get_grid())

    def contains_colors(self):
        """ Return True if the task contains colors
        """
        return any(self._COLORS_FIELDS in row for row in self.get_grid())

    def get_grid(self):
        """ Return 2D list representation of the maze
        """
        return self.get_maze_settings()['grid']

    def get_workspace_settings(self):
        workspace_dict = json.loads(self.workspace_settings)
        workspace_dict['blocks-limit'] = self.get_blocks_limit()
        workspace_dict['toolbox'] = [block.to_json() for block in self.get_required_blocks()]
        return workspace_dict

    def get_maze_settings(self):
        maze_dict = json.loads(self.maze_settings)
        return maze_dict

    def __str__(self):
        return '[{pk}] {title}'.format(pk=self.pk, title=self.title)

    def to_export_tuple(self):
        export_tuple = self.export_class(
            task_id=self.pk,
            title=self.title,
            concepts_ids=[concept.pk for concept in self.get_contained_concepts()],
            blocks_ids=[block.pk for block in self.get_required_blocks()],
            maze_settings=self.maze_settings.replace('\n', ' '),
            solution=self.solution.replace('\n', ' '),
            level=self.get_level())
        return export_tuple

    def to_json(self):
        """Return JSON (dictionary) representation of the task.
        """
        task_dict = {
            'task-id': self.pk,
            'title': self.title,
            'maze-settings': self.get_maze_settings,
            'workspace-settings': self.get_workspace_settings()
        }
        return task_dict

    def infer_attributes_from_setting_and_solution(self):
        """ Infer toolbox, block limit and concepts from task setting and
            solution. The order of inference is important: concepts
            inference requires block limit to be known, block limit inference
            requires level (i.e. toolbox to be known).
        """
        assert self.maze_settings is not None and self.solution is not None
        self._infer_toolbox()
        self._infer_blocks_limit()
        self._infer_concepts()

    def _infer_blocks_limit(self):
        """ It only overrides block limit if it's not already set to
            a non-null value, if the task level is not small and if there
            is a solution to infer the block limit from
        """
        if self._blocks_limit is not None:
            return  # don't override non-null blocks limits
        if not self.solution or self.get_level() < self._BLOCK_LIMIT_LEVEL:
            return
        blocks = self._get_blocks_identifiers_in_solution()
        self._blocks_limit = len(blocks)

    def _infer_concepts(self):
        """ It only adds concepts as we do not need to remove concepts.
        """
        assert self.solution is not None
        contained_concepts = set()
        for concept in filter(lambda e: isinstance(e, EnvironmentConcept), CONCEPTS):
            contained_concepts.add(concept)
        for concept in filter(lambda e: isinstance(e, GameConcept), CONCEPTS):
            if concept.is_contained_in(self):
                contained_concepts.add(concept)
        blocks = self._get_blocks_in_solution()
        for concept in filter(lambda e: isinstance(e, BlockConcept), CONCEPTS):
            if concept.block in blocks:
                contained_concepts.add(concept)
        for concept in filter(lambda e: isinstance(e, ProgrammingConcept), CONCEPTS):
            if not contained_concepts.isdisjoint(concept.subconcepts):
                contained_concepts.add(concept)
        self._contained_concepts = contained_concepts

    def _infer_toolbox(self):
        assert self.solution is not None
        blocks = self._get_blocks_in_solution()
        self.toolbox = ToolboxManager.get_first_toolbox_containing(blocks)

    def _get_blocks_in_solution(self):
        blocks_identifiers = self._get_blocks_identifiers_in_solution()
        blocks = [BlockManager.get_by_natural_key(identifier)
                  for identifier in blocks_identifiers]
        return blocks

    def _get_blocks_identifiers_in_solution(self):
        """ Return list of blocks identifiers as they appear in the solution
            If the solution is not provided, return None
        """
        if not self.solution:
            return None
        blocks = re.findall(r'<block type="(.*?)"', self.solution)
        return blocks
