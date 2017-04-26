export function isLoaded(state) {
  return state.app.staticDataLoaded && state.app.studentLoaded;
}

export function inMode(state, mode) {
  // TODO: check that mode is one of the valid modes
  // TODO: move mode to state.app
  return state.menu.mode === mode;
}
