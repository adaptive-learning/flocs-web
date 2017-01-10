import axios from 'axios'

// TODO: factor out to store
const taskSessionUrl = "/api/task_sessions/";
const taskUrl = "/api/tasks/";

export function fetchTaskSession(url) {
    return {
        type: "FETCH_TASK_SESSION",
        payload: axios.get(url)
    }
}

export function fetchTask(url) {
    return {
        type: "FETCH_TASK",
        payload: axios.get(url)
    }
}
