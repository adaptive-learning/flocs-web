export function getPractice(state) {
  return state.practice;
}

export function getRecommendedTask(state) {
  const practice = getPractice(state);
  let task = null;
  const taskId = state.practice.recommendation;
  if (taskId) {
    task = {
      taskId,
      url: `/task/${taskId}`
    };
  }
  return task;
}
