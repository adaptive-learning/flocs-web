import { FETCH_STATIC_DATA_FULFILLED } from '../action-types';


export default function reduceTasks(state = {}, action) {
  switch (action.type) {
    case FETCH_STATIC_DATA_FULFILLED: {
      const taskList = action.payload.tasks.map(parseTask);
      const tasks = {};
      for (const task of taskList) {
        tasks[task.id] = task;
      }
      return tasks;
    }
  }
  return state;
}

function parseTask(data) {
  const task = {
    id: data['task_id'],
    category: data['category'],
    setting: jsonToObject(data.setting),
    solution: jsonToObject(data.setting),
  };
  return task;
}

function jsonToObject(jsonStr) {
  return JSON.parse(jsonStr.replace(/'/g, '"'));
}
