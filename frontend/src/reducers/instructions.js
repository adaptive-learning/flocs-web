import {
  FETCH_STATIC_DATA_FULFILLED,
  UPDATE_STUDENT_FULFILLED,
  SET_TASK,
  SEE_INSTRUCTION_PENDING,
  // SHOW_INSTRUCTIONS,
  } from '../action-types';
import { getRelevantInstructions } from '../selectors/instructions';


const initial = {
  byId: {},
  all: [],
  seen: [],
  scheduled: [],
  activeIndex: null,
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
      const relevantInstructions = getRelevantInstructions(state, action.payload.task);
      return {
        ...state,
        activeIndex: (relevantInstructions.length > 0) ? 0 : null,
        scheduled: relevantInstructions,
      };
    }
    case SEE_INSTRUCTION_PENDING: {
      console.log('see instruction pending', action.payload);
      return state;
    }
    // case SHOW_INSTRUCTIONS: {
    //   return {
    //     ...state,
    //     activeInstructionIndex: state.activeInstructionIndex ? state.activeInstructionIndex : 0,
    //   };
    // }
    // case SEEN_INSTRUCTION: {
    //   let nextInstructionIndex = action.payload.index + 1;
    //   if (nextInstructionIndex >= state.scheduledInstructions.length) {
    //     nextInstructionIndex = null;
    //   }
    //   return {
    //     ...state,
    //     activeInstructionIndex: nextInstructionIndex,
    //   };
    // }
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
