/**
 * Api for posting core actions which happend in the world we model
 */

import axios from 'axios';


export function seeInstruction(instructionId) {
  return ((state, dispatch) => {
    const data = {
      type: 'see-instruction',
      data: {
        'student-id': state.flocsComponents.student.studentId, // TODO: use selector
        'instruction-id': instructionId,
      },
    };
    axios.post('/api/actions/see-instruction', data),
  });

}

