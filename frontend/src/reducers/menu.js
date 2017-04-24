import { LOCATION_CHANGE } from 'react-router-redux';

const initialState = {
  mode: 'intro',
  open: false,
};

export default function menuReducer(state = initialState, action) {
  switch (action.type) {
    case 'MENU.SET_OPEN':
      return {
        ...state,
        open: action.payload.open,
      };
    case LOCATION_CHANGE:
      return {
        ...state,
        mode: getMode(action.payload.pathname),
        open: false,
      };
  }
  return state;
}


function getMode(path) {
  const parts = path.split('/');
  const topPage = parts[1];
  const mode = (!topPage) ? 'intro' : topPage;
  return mode;
}
