import axios from 'axios'

// TODO: factor out to store
const practiceUrl = "http://localhost:8000/api/practice/";

import { flocsActionCreators } from 'flocs-visual-components';


export function start(taskEnvId) {
    return function(dispatch) {
        return fetchNextTask().then(
            (response) => {
                // process returned task
                let task = {};
                task['setting'] = jsonToObject(response.data.setting);
                task['solution'] = jsonToObject(response.data.solution);
                task['task_id'] = response.data.task_id;
                // set task in environment
                dispatch(flocsActionCreators.setTask(taskEnvId, task));
                // start practicing
                dispatch({type: "START", payload: task})
            })
    }
}

function fetchNextTask() {
    return axios.post(practiceUrl + 'start/')
        .then(function (response) {
            const ti_url = response.data.task_instance;
            return axios.get(ti_url)
        }).then(function (response) {
            const taskUrl = response.data.task;
            return axios.get(taskUrl, {params: {format: "json"}})
        });
}

function jsonToObject(jsonStr) {
    return JSON.parse(jsonStr.replace(/'/g, "\""));
}
