import { SHOW_INSTRUCTIONS,
         SEEN_INSTRUCTION } from '../action-types';

export function showInstructions() {
  return {
    type: SHOW_INSTRUCTIONS,
    payload: {},
  };
}


export function seenInstruction(instructionId) {
  return {
    type: SEEN_INSTRUCTION,
    payload: { instructionId },
  };
  // TODO: report seen instruction
}
