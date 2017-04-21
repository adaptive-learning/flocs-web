/**
 * Api for communication with the backend
 */

import axios from 'axios';
import { FETCH_STATIC_DATA,
         FETCH_PRACTICE_OVERVIEW,
         UPDATE_STUDENT,
         START_SESSION,
         START_TASK,
         SOLVE_TASK,
         SEE_INSTRUCTION } from '../action-types';


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


// TODO: factor out non-api (taskEnvironment) part
export function startTask(taskId, taskEnvironmentId) {
  return dispatch => {
    const data = { 'task-id': taskId };
    const action = {
      type: START_TASK,
      payload: postAction('start-task', data)
        .then(parseStartTaskResponse)
        .then(payload => ({ ...payload, taskEnvironmentId })),
    };
    return dispatch(action);
  };
}


// TODO: factor out non-api (taskEnvironment) part
export function solveTask(taskSessionId, taskEnvironmentId) {
  return dispatch => {
    const data = { 'task-session-id': taskSessionId };
    const action = {
      type: SOLVE_TASK,
      payload: postAction('solve-task', data)
        .then(parseSolveTaskResponse)
        .then(payload => ({ ...payload, taskEnvironmentId })),
    };
    return dispatch(action).then(() => dispatch(updateStudent()));
  };
}


export function seeInstruction(instructionId) {
  return dispatch => {
    const data = { 'instruction-id': instructionId };
    const action = {
      type: SEE_INSTRUCTION,
      payload: postAction('see-instruction', data),
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


function parseSolveTaskResponse(_response) {
  // const data = response.data.data;  // response data -> action data
  return {};
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
