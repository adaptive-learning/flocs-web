import { SET_STUDENT, } from '../action-types';


const initialState = {
  seenInstructions: [],
};


export function reduceStudent(state = initialState, action) {
  switch (action.type) {
    case SET_STUDENT:
      return {
        ...state,
        studentId: action.payload['student_id'],
        seenInstructions: action.payload['seen_instructions'],
        taskSessions: action.payload['task_sessions'],
      };
    default:
      return state;
  }
}
