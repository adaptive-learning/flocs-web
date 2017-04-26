import {
  FETCH_STATIC_DATA_FULFILLED,
  UPDATE_STUDENT_FULFILLED,
  SET_TASK,
  SEE_INSTRUCTION_PENDING,
  SEE_INSTRUCTION_FULFILLED,
  SHOW_INSTRUCTIONS,
  } from '../action-types';
import { getRelevantInstructions } from '../selectors/instructions';
import { practicePageTaskEnvironmentId } from '../selectors/taskEnvironment';


const initial = {
  byId: {},
  all: [],
  seen: [],
  scheduled: [],
  activeIndex: null,

  // the following lock is just a hack to overcome the following bug: if the
  // student clicks on "show instructions" button and then presses Enters
  // (instead of clicking) then the last Enter on the last scheduled
  // instruction also fires "show instruction" action again (I don't know why,
  // and I wasn't able to avoid this).
  seeingInstructionLock: false,
};


export default function reduceInstructions(state = initial, action) {
  switch (action.type) {
    case FETCH_STATIC_DATA_FULFILLED: {
      const instructionList = action.payload.instructions.map(parseInstruction);
      return {
        ...state,
        byId: createEntityMap(instructionList),
        all: instructionList.map(instruction => instruction.id),
      };
    }
    case UPDATE_STUDENT_FULFILLED: {
      return {
        ...state,
        seen: action.payload.seenInstructions,
      };
    }
    case SET_TASK: {
      if (action.payload.taskEnvironmentId !== practicePageTaskEnvironmentId) {
        return state;
      }
      const relevantInstructions = getRelevantInstructions(state, action.payload.task);
      return {
        ...state,
        activeIndex: (relevantInstructions.length > 0) ? 0 : null,
        scheduled: relevantInstructions,
      };
    }
    case SEE_INSTRUCTION_PENDING: {
      if (action.payload.instructionId !== state.scheduled[state.activeIndex]) {
        return state;
      }
      let nextIndex = state.activeIndex + 1;
      if (nextIndex >= state.scheduled.length) {
        nextIndex = null;
      }
      return {
        ...state,
        activeIndex: nextIndex,
        seeingInstructionLock: true,
      };
    }
    case SEE_INSTRUCTION_FULFILLED: {
      return {
        ...state,
        seeingInstructionLock: false,
      };
    }
    case SHOW_INSTRUCTIONS: {
      if (state.activeIndex !== null) {
        return state;
      }
      if (state.scheduled.length === 0) {
        return state;
      }
      if (state.seeingInstructionLock) {
        return state;
      }
      return {
        ...state,
        activeIndex: 0,
      };
    }
  }
  return state;
}


const viewData = {
  'env.space-world': {
    selector: '.instructionable-env-space-world',
    position: 'bottom',
  },
  'env.toolbox': {
    selector: '.blocklyFlyout',
    position: 'right',
  },
  'env.snapping': {
    selector: '.instructionable-env-snapping',
    position: 'bottom-left',
  },
  'env.controls': {
    selector: '.instructionable-env-controls',
    position: 'bottom-left',
  },
  'object.wormhole': {
    selector: '.instructionable-object-wormhole',
    position: 'bottom-left',
  },
  'object.diamond': {
    selector: '.instructionable-object-diamond',
    position: 'bottom-left',
  },
  'object.asteroid': {
    selector: '.instructionable-object-asteroid',
    position: 'bottom-left',
  },
  'object.meteoroid': {
    selector: '.instructionable-object-meteoroid',
    position: 'bottom-left',
  },
  'diamonds-status': {
    selector: '.instructionable-diamonds-status',
    position: 'bottom-left',
  },
  'energy-status': {
    selector: '.instructionable-energy-status',
    position: 'bottom-left',
  },
  'action-limit': {
    selector: '.instructionable-action-limit',
    position: 'bottom-left',
  },
  'block.fly': {
    selector: '.instructionable-block-fly',
    position: 'bottom-left',
  },
  'block.shoot': {
    selector: '.instructionable-block-shoot',
    position: 'bottom-left',
  },
  'block.repeat': {
    selector: '.instructionable-block-repeat',
    position: 'bottom-left',
  },
  'block.while': {
    selector: '.instructionable-block-while',
    position: 'bottom-left',
  },
  'block.color': {
    selector: '.instructionable-block-color',
    position: 'bottom-left',
  },
  'block.position': {
    selector: '.instructionable-block-position',
    position: 'bottom-left',
  },
  'block.if': {
    selector: '.instructionable-block-if',
    position: 'bottom-left',
  },
  'block.if-else': {
    selector: '.instructionable-block-if-else',
    position: 'bottom-left',
  },
};


function parseInstruction(data) {
  const instructionId = data['instruction_id'];
  if (viewData[instructionId] === undefined) {
    console.warn(`Missing view data for instruction '${instructionId}'`);
  }
  const instruction = {
    ...viewData[instructionId],
    id: instructionId,
  };

  return instruction;
}


// TODO: factor out to some common utils (core.entities?)
function createEntityMap(list) {
  const map = {};
  for (const entity of list) {
    map[entity.id] = entity;
  }
  return map;
}
