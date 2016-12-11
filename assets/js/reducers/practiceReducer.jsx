import React from 'react';


export function practiceReducer(state={
    task: {},
}, action) {
    switch (action.type) {
        case "START" : {
            return {...state, task: action.payload}
        }
    }

    return state
}
