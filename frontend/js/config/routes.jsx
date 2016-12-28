import React from 'react';
import { Route, IndexRoute } from 'react-router';
import Main from '../components/Main';
import Home from '../components/Home';
import TaskEnvironment from '../components/TaskEnvironment';
import TasksTableContainer from '../containers/TasksTableContainer';

const routes = (
    <Route path='/' component={Main}>
        <IndexRoute component={Home} />
        <Route path='/tasks' component={TasksTableContainer} />
        <Route path='/task/:taskId' component={TaskEnvironment} />
    </Route>
);

export default routes;
