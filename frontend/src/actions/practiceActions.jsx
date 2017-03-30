import axios from 'axios'

// TODO: factor out to store
const practiceUrl = "/api/practice/";

import { setTask as setTaskInTaskEnvironment } from './taskEnvironment';
import { fetchTaskSession, fetchTask } from './taskSessionActions'
import { solveTask } from './actions';


export function startPractice(taskEnvId, taskId) {
  return ((dispatch, getState) => {
    return dispatch(startTask(typeof taskId === "undefined" ? getState().practice.recommendation : taskId)
    ).then(() =>
        dispatch(fetchTaskSession(getState().practice.taskSessionUrl))
    ).then(() =>
        dispatch(fetchTask(getState().taskSession.taskUrl))
    ).then(() =>
        dispatch(setTaskInTaskEnvironment(taskEnvId, getState().taskSession.task))
    )
  });
}


export function setTask(taskEnvId, taskId) {
  return ((dispatch, getState) => {
    return dispatch(fetchTask(`/api/tasks/${taskId}`)).then(
      // TODO: unhack - no task session is actualy created on server, so avoid
      // passing data through task session state
      () => dispatch(setTaskInTaskEnvironment(taskEnvId, getState().taskSession.task))
    );
  });
}


export function solveTaskAndRecommend() {
    return ((dispatch, getState) => {
        return dispatch(solveTask(getState().taskSession.id))
          .then(() => dispatch(recommend()));
    });
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
