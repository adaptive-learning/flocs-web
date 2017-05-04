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
        level: action.payload.level,
        credits: action.payload.credits,
        activeCredits: action.payload.activeCredits,
        practiceOverviewUrl: action.payload.practiceOverviewUrl,
        reportProgramEditUrl: action.payload.reportProgramEditUrl,
        reportProgramExecutionUrl: action.payload.reportProgramExecutionUrl,
      };
    default:
      return state;
  }
}
