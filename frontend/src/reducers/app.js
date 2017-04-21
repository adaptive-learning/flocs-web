import { FETCH_STATIC_DATA_FULFILLED,
         UPDATE_STUDENT_FULFILLED } from '../action-types';

const initial = {
  staticDataLoaded: false,
  studentLoaded: false,
};

export default function reduceApp(state = initial, action) {
  switch (action.type) {
    case FETCH_STATIC_DATA_FULFILLED:
      return {
        ...state,
        staticDataLoaded: true,
      };
    case UPDATE_STUDENT_FULFILLED:
      return {
        ...state,
        studentLoaded: true,
      };
    default:
      return state;
  }
}
