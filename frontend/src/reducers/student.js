import { START_SESSION_FULFILLED,
         UPDATE_STUDENT_FULFILLED } from '../action-types';


export default function reduceStudent(state = {}, action) {
  switch (action.type) {
    case START_SESSION_FULFILLED:
      return {
        ...state,
        id: action.payload.studentId,
      };
    case UPDATE_STUDENT_FULFILLED:
      return {
        ...state,
        credits: action.payload.credits,
        practiceOverviewUrl: action.payload.practiceOverviewUrl,
      };
    default:
      return state;
  }
}
