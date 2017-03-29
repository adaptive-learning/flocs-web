import { SHOW_INSTRUCTIONS,
         SEEN_INSTRUCTION } from '../action-types';

export function showInstructions() {
  return {
    type: SHOW_INSTRUCTIONS,
    payload: {},
  };
}


export function seenInstruction(index) {
  return {
    type: SEEN_INSTRUCTION,
    payload: { index },
  };
}
