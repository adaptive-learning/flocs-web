import React from 'react';
import ReactDOM from 'react-dom';
import { Route, IndexRoute } from 'react-router';
import TaskEditorContainer from './containers/TaskEditorContainer';
import AppContainer from './containers/AppContainer';
import HomePage from './pages/HomePage';
import PracticePage from './pages/PracticePage';
import TasksTableContainer from './containers/TasksTableContainer';
import FlocsProvider from './FlocsProvider';
import { globalConfiguration, configureStore } from './config';


globalConfiguration();

const store = configureStore();

const routes = (
  <Route path="/" component={AppContainer}>
    <IndexRoute component={HomePage} />
    <Route path="/tasks" component={TasksTableContainer} />
    <Route path="/task/:taskId" component={PracticePage} />
    <Route path="/task-editor" component={TaskEditorContainer} />
  </Route>
);

const app = (
  <FlocsProvider store={store} router>
    {routes}
  </FlocsProvider>
);

const mountElement = document.getElementById('flocsApp');
ReactDOM.render(app, mountElement);
