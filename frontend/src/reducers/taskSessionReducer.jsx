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
                solve: action.payload.data.solve,
            }
        }
        case "FETCH_TASK_FULFILLED": {
            // process returned task
            let task = {};
            task['setting'] = jsonToObject(action.payload.data.setting);
            task['solution'] = jsonToObject(action.payload.data.solution);
            task['task_id'] = action.payload.data.task_id;
            return {...state, task: task}
        }
        case "GET_TASK_FULFILLED": {
            let task = {};
            task['setting'] = jsonToObject(action.payload.data.setting);
            task['solution'] = jsonToObject(action.payload.data.solution);
            task['task_id'] = action.payload.data.task_id;
            return {...state, task: task}
        }
    }

    return state
}

function jsonToObject(jsonStr) {
    return JSON.parse(jsonStr.replace(/'/g, "\""));
}
