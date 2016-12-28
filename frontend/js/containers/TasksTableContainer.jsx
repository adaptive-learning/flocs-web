import React from 'react';
import { connect } from 'react-redux';
import { TasksTable } from 'flocs-visual-components';
import { fetchTasks } from '../actions/tasks';


const task1 = {
  taskId: 'first',
  setting: {
    fields: [[['b', []], ['b', []], ['b', []], ['b', []], ['b', []]],
              [['k', []], ['k', []], ['k', ['S']], ['k', []], ['k', []]]],
  },
};
const task2 = {
  taskId: 'second',
  setting: {
    fields: [[['b', []], ['b', ['A']], ['b', ['M']], ['b', ['A']], ['b', []]],
            [['k', []], ['k', ['A']], ['k', []], ['k', ['A']], ['k', []]],
            [['k', []], ['k', ['A']], ['k', ['M']], ['k', ['A']], ['k', []]],
            [['k', []], ['k', ['A']], ['k', []], ['k', ['A']], ['k', []]],
            [['k', []], ['k', ['A']], ['k', ['M']], ['k', ['A']], ['k', []]],
            [['k', []], ['k', ['A']], ['k', []], ['k', ['A']], ['k', []]],
            [['k', []], ['k', ['A']], ['k', ['M']], ['k', ['A']], ['k', []]],
            [['k', []], ['k', ['A']], ['k', []], ['k', ['A']], ['k', []]],
            [['k', []], ['k', ['A']], ['k', ['S']], ['k', ['A']], ['k', []]]],
  },
};



function mapStateToProps(state) {
  return {
    tasks: state.tasks,
  };
}


@connect(mapStateToProps, { fetchTasks })
export default class TasksTableContainer extends React.Component {
  componentWillMount() {
    this.props.fetchTasks();
  }

  render(){
    return (
      <TasksTable tasks={this.props.tasks} urlBase="/task/" />
    );
  }
}
