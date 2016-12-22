import axios from 'axios'

// TODO: factor out to store
const taskInstanceUrl = "/api/task_instances/";
const taskUrl = "/api/tasks/";

export function fetchTaskInstance(url) {
    return {
        type: "FETCH_TASK_INSTANCE",
        payload: axios.get(url)
    }
}

export function fetchTask(url) {
    return {
        type: "FETCH_TASK",
        payload: axios.get(url)
    }
}
