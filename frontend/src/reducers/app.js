import { FETCH_STATIC_DATA_FULFILLED } from '../action-types';

const initial = {
  loading: true,
};

export default function reduceStudent(state = initial, action) {
  switch (action.type) {
    case FETCH_STATIC_DATA_FULFILLED:
      return {
        ...state,
        loading: false,
      };
    default:
      return state;
  }
}
