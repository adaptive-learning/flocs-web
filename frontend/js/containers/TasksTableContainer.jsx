import React from 'react';
import { connect } from 'react-redux';
import { TasksTable } from 'flocs-visual-components';
import { fetchTasks } from '../actions/tasks';


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
      <TasksTable tasks={this.props.tasks} urlBase="/task-preview/" />
    );
  }
}
