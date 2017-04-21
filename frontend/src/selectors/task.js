export function getCategoryId(state, taskId) {
  return state.tasks[taskId].category;
}
