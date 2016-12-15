import React from 'react';


export function practiceReducer(state={
    stage: "LOADING",
    recommendation: null,
    taskInstanceUrl: null,
}, action) {
    switch (action.type) {
        case "RECOMMEND_FULFILLED": {
            return {...state, recommendation: action.payload.data.task_id}
        }
        case "START_TASK_FULFILLED": {
            return {...state, taskInstanceUrl: action.payload.data.task_instance, stage: "STARTING"}
        }
        case "FLOCS.TASK_ATTEMPTED": {
            return {...state, stage: "ATTEMPTED"}
        }
        case "FLOCS.SET_TASK": {
            return {...state, stage: "PRACTICING"}
        }
        case "NEXT_TASK": {
            return {...state, stage: "LOADING"}
        }
    }

    return state
}
