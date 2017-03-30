import React from 'react';
import { connect } from 'react-redux';
import muiThemeable from 'material-ui/styles/muiThemeable';
import TasksTable from '../components/TasksTable';
import { fetchTasks } from '../actions/tasks';


function mapStateToProps(state) {
  return {
    tasks: Object.values(state.tasks),
  };
}


@connect(mapStateToProps, { fetchTasks })
@muiThemeable()
export default class TasksTableContainer extends React.Component {
  componentWillMount() {
    this.props.fetchTasks();
  }

  render() {
    const longPageContentStyle = {
      maxWidth: 1200,
      margin: '20px auto',
      backgroundColor: this.props.muiTheme.palette.canvasColor,
    };
    return (
      <div style={longPageContentStyle}>
        <TasksTable tasks={this.props.tasks} urlBase="/task/" />
      </div>
    );
  }
}
