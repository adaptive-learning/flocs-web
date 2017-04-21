export function isLoaded(state) {
  return state.app.staticDataLoaded && state.app.studentLoaded;
}
