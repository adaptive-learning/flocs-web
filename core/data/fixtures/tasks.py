from core.data.models.task import Task

TASKS = [
    Task(pk=1,
         title='Tři kroky vpřed',
         revision=1,
         maze_settings="""
    {
      "grid": [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 2, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]],
      "hero": {
        "position": [2, 4],
        "direction": 0
      }
    }""", workspace_settings='{}',
         solution='<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="10" y="10"><next><block type="maze_move_forward"><next><block type="maze_move_forward"><next><block type="maze_move_forward"></block></next></block></next></block></next></block></xml>'
         )
]
