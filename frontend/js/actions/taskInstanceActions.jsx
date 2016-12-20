import axios from 'axios'

// TODO: factor out to store
const taskInstanceUrl = "http://localhost:8000/api/task_instances/";
const taskUrl = "http://localhost:8000/api/tasks/";

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
