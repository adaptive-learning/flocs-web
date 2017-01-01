import React from 'react';
import { Route, IndexRoute } from 'react-router';
import { TaskEditorContainer } from 'flocs-visual-components';
import Main from '../components/Main';
import Home from '../components/Home';
import PracticeContainer from '../containers/PracticeContainer';
import TasksTableContainer from '../containers/TasksTableContainer';
import TaskPreviewContainer from '../containers/TaskPreviewContainer';

const routes = (
    <Route path='/' component={Main}>
        <IndexRoute component={Home} />
        <Route path='/tasks' component={TasksTableContainer} />
        <Route path='/task/:taskId' component={PracticeContainer} />
        <Route path='/task-preview/:taskId' component={TaskPreviewContainer} />
        <Route path='/task-editor' component={TaskEditorContainer} />
    </Route>
);

export default routes;
