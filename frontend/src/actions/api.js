/**
 * Api for communication with the backend
 */

import axios from 'axios';
import { FETCH_STATIC_DATA,
         FETCH_PRACTICE_OVERVIEW,
         UPDATE_STUDENT,
         START_SESSION,
         START_TASK } from '../action-types';


export function fetchStaticData() {
  const entityNames = ['blocks', 'toolboxes', 'categories', 'tasks', 'levels', 'instructions'];
  const urls = entityNames.map(name => `/api/${name}`);
  const requests = urls.map(url => axios.get(url));
  return {
    type: FETCH_STATIC_DATA,
    payload: axios.all(requests).then(results => {
      const namedResults = {};
      for (const [i, name] of entityNames.entries()) {
        namedResults[name] = results[i].data;
      }
      return namedResults;
    }),
  };
}


export function startSession() {
  return dispatch => {
    const action = {
      type: START_SESSION,
      payload: postAction('start-session').then(parseStartSessionResponse),
    };
    return dispatch(action)
      .then(() => dispatch(updateStudent()))
      .then(() => dispatch(fetchPraticeOverview()));
  };
}


export function startTask(taskId) {
  return dispatch => {
    const action = {
      type: START_TASK,
      payload: postAction('start-task', {'task-id': taskId}).then(parseStartTaskResponse),
    };
    return dispatch(action);
  };
}


function postAction(type, data = {}) {
  const requestData = {
    type,
    data: JSON.stringify(data),
  };
  return axios.post('/api/actions/', requestData);
}


function parseStartSessionResponse(response) {
  const data = response.data.data;  // response data -> action data
  return {
    studentId: data['student_id'],
    sessionId: data['session_id'],
  };
}


function parseStartTaskResponse(response) {
  const data = response.data.data;  // response data -> action data
  return {
    taskSessionId: data['task_session_id'],
  };
}


function updateStudent() {
  return (dispatch, getState) => dispatch({
    type: UPDATE_STUDENT,
    payload: axios.get(getStudentUrl(getState())).then(parseStudentResponse),
  });
}


export function fetchPraticeOverview() {
  return (dispatch, getState) => dispatch({
    type: FETCH_PRACTICE_OVERVIEW,
    payload: axios.get(getPracticeOverviewUrl(getState())).then(parsePracticeOverviewResponse),
  });
}


// TODO: move to selectors
function getStudentUrl(state) {
  const { id } = state.student;
  return `/api/students/${id}/`;
}

function getPracticeOverviewUrl(state) {
  return state.student.practiceOverviewUrl;
}


function parseStudentResponse(response) {
  const { data } = response;
  return {
    credits: data['credits'],
    seenInstructions: data['seen_instructions'],
    practiceOverviewUrl: data['practice_overview'],
  };
}


function parsePracticeOverviewResponse(response) {
  const { data } = response;
  return {
    level: data['level'],
    credits: data['credits'],
    activeCredits: data['active_credits'],
    tasks: data['tasks'],
    recommendation: data['recommendation'],
  };
}
