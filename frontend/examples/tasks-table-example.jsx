import React, { PropTypes } from 'react';
import ReactDOM from 'react-dom';
import { Route } from 'react-router';
import { FlocsProvider, TasksTable } from 'flocs-visual-components';

const mountElement = document.getElementById('tasksTableExample');
/* eslint-disable no-inner-declarations */
if (mountElement !== null) {
  const tasks = [
    {
      taskId: 'one-step-forward',
      categoryId: 'moves',
      setting: {},
    },
    {
      taskId: 'two-steps-forward',
      categoryId: 'moves',
      setting: {},
    },
    {
      taskId: 'three-steps-forward',
      categoryId: 'moves',
      setting: {},
    },
    {
      taskId: 'turning-left',
      categoryId: 'moves',
      setting: {},
    },
    {
      taskId: 'turning-right',
      categoryId: 'moves',
      setting: {},
    },
    {
      taskId: 'turning-left-and-right',
      categoryId: 'moves',
      setting: {},
    },
    {
      taskId: 'ladder',
      categoryId: 'repeat',
      setting: {},
    },
    {
      taskId: 'zig-zag',
      categoryId: 'repeat',
      setting: {},
    },
  ];


  function TaskEnvironmentContainer({ params }) {
    return (
      <pre>
        {JSON.stringify(tasks[params.taskId])}
      </pre>
    );
  }

  TaskEnvironmentContainer.propTypes = {
    params: PropTypes.object.isRequired,
  };

  function TasksTableContainer() {
    return (
      <TasksTable tasks={tasks} urlBase="/task/" />
    );
  }

  const tasksTableContainer = (
    <FlocsProvider router>
      <Route path="/tasks-table-example.html" component={TasksTableContainer} />
      <Route path="/task/:taskId" component={TaskEnvironmentContainer} />
    </FlocsProvider>
  );
  ReactDOM.render(tasksTableContainer, mountElement);
}
