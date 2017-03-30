/**
 * Api for reporting core actions which happend in the world we model
 */

import axios from 'axios';


export function reportSeenInstruction(instructionId) {
  return ((state, dispatch) => {
    const data = {
      type: 'see-instruction',
      data: {
        'student-id': state.student.studentId, // TODO: use selector
        'instruction-id': instructionId,
      },
    };
    axios.post('/api/actions/', data),
  });

}

