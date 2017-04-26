import { LOCATION_CHANGE } from 'react-router-redux';
import { FETCH_STATIC_DATA_FULFILLED,
         UPDATE_STUDENT_FULFILLED } from '../action-types';


const initial = {
  mode: 'intro',
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
    case LOCATION_CHANGE:
      return {
        ...state,
        mode: getMode(action.payload.pathname),
      };
    default:
      return state;
  }
}


function getMode(path) {
  const parts = path.split('/');
  const topPage = parts[1];
  const mode = (!topPage) ? 'intro' : topPage;
  return mode;
}
