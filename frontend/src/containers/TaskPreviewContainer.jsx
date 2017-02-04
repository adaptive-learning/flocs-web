import React from 'react';
import { connect } from 'react-redux'
import { TaskEnvironmentContainer, flocsActionCreators } from 'flocs-visual-components';

import { getTaskForEnv } from '../actions/practiceActions'

const taskEnvId = "single";


function mapStateToProps(state, props) {
  return {
    taskId: props.routeParams.taskId,
  };
}

const actionCreators = {
  getTaskForEnv,
  createTaskEnvironment: flocsActionCreators.createTaskEnvironment,
}

@connect(mapStateToProps, actionCreators)
export default class TaskPreviewContainer extends React.Component {

    componentWillMount() {
      this.props.createTaskEnvironment(taskEnvId);
      this.props.getTaskForEnv(taskEnvId, this.props.taskId);
    }

    render(){
      return (
        <TaskEnvironmentContainer taskEnvironmentId={taskEnvId} />
      )
    }
}


