import axios from 'axios'

// TODO: factor out to store
const practiceUrl = "/api/practice/";

import { flocsActionCreators } from 'flocs-visual-components';
import { fetchTaskSession, fetchTask } from './taskSessionActions'

export function start(taskEnvId) {
    return ((dispatch) => {
        return dispatch(recommend()).then(() =>
            dispatch(nextTask(taskEnvId))
        )
    })
}

export function getTaskForEnv(taskEnvId, taskId) {
    return ((dispatch, getState) => {
        return dispatch(nextTask(taskEnvId, taskId)
        ).then(() =>
            dispatch(flocsActionCreators.setTask(taskEnvId, getState().taskSession.task))
        )
    })
}

export function solveTaskAndRecommend() {
    return ((dispatch, getState) => {
        return dispatch(solveTaskByUrl(getState().taskSession.solve)
        ).then(() =>
            dispatch(recommend())
        )
    })
}

export function nextTask(taskEnvId, taskId) {
    return ((dispatch, getState) => {
        return dispatch(startTask(typeof taskId === "undefined" ? getState().practice.recommendation : taskId)
        ).then(() =>
            dispatch(fetchTaskSession(getState().practice.taskSessionUrl))
        ).then(() =>
            dispatch(fetchTask(getState().taskSession.taskUrl))
        ).then(() =>
            dispatch(flocsActionCreators.setTask(taskEnvId, getState().taskSession.task))
        )
    })
}

export function recommend() {
    return {
        type: "RECOMMEND",
        payload: axios.get(practiceUrl + 'recommend/')
    }
}

// PRIVATE
function startTask(taskId) {
    return {
        type: "START_TASK",
        payload: axios.post(practiceUrl + 'start_task/' + taskId + '/')
    }
}

function solveTaskByUrl(url) {
    return {
        type: "SOLVE_TASK",
        payload: axios.post(url)
    }
}

