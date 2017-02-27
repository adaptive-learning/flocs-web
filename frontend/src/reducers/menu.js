const initialState = {
  open: false,
};

export default function menuReducer(state = initialState, action) {
  switch (action.type) {
    case 'MENU.SET_OPEN':
      return {
        ...state,
        open: action.payload.open,
      };
  }
  return state;
}
