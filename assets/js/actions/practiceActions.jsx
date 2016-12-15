import axios from 'axios'

// TODO: factor out to store
const practiceUrl = "http://localhost:8000/api/practice/";

import { flocsActionCreators } from 'flocs-visual-components';
import { fetchTaskInstance, fetchTask } from './taskInstanceActions'

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
            dispatch(flocsActionCreators.setTask(taskEnvId, getState().taskInstance.task))
        )
    })
}

export function solveTaskAndRecommend() {
    return ((dispatch, getState) => {
        return dispatch(solveTaskByUrl(getState().taskInstance.solve)
        ).then(() =>
            dispatch(recommend())
        )
    })
}

export function nextTask(taskEnvId, taskId) {
    return ((dispatch, getState) => {
        return dispatch(startTask(typeof taskId === "undefined" ? getState().practice.recommendation : taskId)
        ).then(() =>
            dispatch(fetchTaskInstance(getState().practice.taskInstanceUrl))
        ).then(() =>
            dispatch(fetchTask(getState().taskInstance.taskUrl))
        ).then(() =>
            dispatch(flocsActionCreators.setTask(taskEnvId, getState().taskInstance.task))
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

