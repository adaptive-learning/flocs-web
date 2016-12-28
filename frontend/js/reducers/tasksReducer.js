export function tasksReducer(state={}, action) {
  switch (action.type) {
    case "FETCH_TASKS_FULFILLED": {
      const tasksList = action.payload.data.map(parseTask);
          // TODO: send parsed from the server already (?)
      let tasks = {};
      for (var task of tasksList) {
        tasks[task.taskId] = task;
      }
      return tasks;
    }
  }
  return state;
}

function parseTask(taskData) {
  const task = {
    taskId: taskData['task_id'],
    url: taskData.url,
    setting: jsonToObject(taskData.setting),
    solution: jsonToObject(taskData.setting),
  };
  return task;
}

function jsonToObject(jsonStr) {
    return JSON.parse(jsonStr.replace(/'/g, "\""));
}
