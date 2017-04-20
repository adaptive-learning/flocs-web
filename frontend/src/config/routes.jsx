import React from 'react';
import { Route, IndexRoute } from 'react-router';
import TaskEditorContainer from '../containers/TaskEditorContainer';
import AppContainer from '../containers/AppContainer';
import HomePage from '../pages/HomePage';
import PracticePage from '../pages/PracticePage';
import TasksTableContainer from '../containers/TasksTableContainer';

const routes = (
  <Route path="/" component={AppContainer}>
    <IndexRoute component={HomePage} />
    <Route path="/tasks" component={TasksTableContainer} />
    <Route path="/task/:taskId" component={PracticePage} />
    <Route path="/task-editor" component={TaskEditorContainer} />
  </Route>
);

export default routes;
