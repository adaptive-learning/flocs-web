import React from 'react';
import { Route, IndexRoute } from 'react-router';
import { TaskEditorContainer } from 'flocs-visual-components';
import MainContainer from '../containers/MainContainer';
import Home from '../components/Home';
import PracticePage from '../pages/PracticePage';
import TasksTableContainer from '../containers/TasksTableContainer';

const routes = (
    <Route path='/' component={MainContainer}>
        <IndexRoute component={Home} />
        <Route path='/tasks' component={TasksTableContainer} />
        <Route path='/task/:taskId' component={PracticePage} />
        <Route path='/task-editor' component={TaskEditorContainer} />
    </Route>
);

export default routes;
