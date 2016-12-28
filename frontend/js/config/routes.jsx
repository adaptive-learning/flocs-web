import React from 'react';
import { Route, IndexRoute } from 'react-router';
import Main from '../components/Main';
import Home from '../components/Home';
import TaskEnvironment from '../components/TaskEnvironment';
import TasksTableContainer from '../containers/TasksTableContainer';
import TaskPreviewContainer from '../containers/TaskPreviewContainer';

const routes = (
    <Route path='/' component={Main}>
        <IndexRoute component={Home} />
        <Route path='/tasks' component={TasksTableContainer} />
        <Route path='/task/:taskId' component={TaskEnvironment} />
        <Route path='/task-preview/:taskId' component={TaskPreviewContainer} />
    </Route>
);

export default routes;
