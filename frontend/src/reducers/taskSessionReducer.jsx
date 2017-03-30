import React from 'react';


export function taskSessionReducer(state={
    id: null,
    taskUrl: null,
    solve: null,
    task: {},
}, action) {
    switch (action.type) {
        case "FETCH_TASK_SESSION_FULFILLED": {
            return {...state,
                id: action.payload.data.task_session_id,
                taskUrl: action.payload.data.task,
            }
        }
        case "FETCH_TASK_FULFILLED": {
            const taskData = action.payload.data;
            const task = {
              taskId: taskData['task_id'],
              categoryId: taskData['category'],
              url: taskData.url,
              setting: jsonToObject(taskData.setting),
              solution: jsonToObject(taskData.setting),
            };
            return { ...state, task }
        }
    }

    return state
}

function jsonToObject(jsonStr) {
    return JSON.parse(jsonStr.replace(/'/g, "\""));
}
