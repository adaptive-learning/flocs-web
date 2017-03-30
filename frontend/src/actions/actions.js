/**
 * Api for reporting core actions which happend in the world we model
 */

import axios from 'axios';
import { SOLVE_TASK } from '../action-types';


export function solveTask(taskSessionId) {
  return ((state, dispatch) => {
    const data = {
      type: 'solve-task',
      data: JSON.stringify({
        'task-session-id': taskSessionId,
      }),
    };
    return {
      type: SOLVE_TASK,
      payload: axios.post('/api/actions/', data),
    };
  });
}


export function reportSeenInstruction(instructionId) {
  return ((state, dispatch) => {
    const data = {
      type: 'see-instruction',
      data: JSON.stringify({
        'student-id': state.student.studentId, // TODO: use selector
        'instruction-id': instructionId,
      }),
    };
    return axios.post('/api/actions/', data);
  });
}
