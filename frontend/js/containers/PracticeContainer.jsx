import React from 'react';
import { connect } from 'react-redux';
import { TaskEnvironmentContainer, flocsSelector, flocsActionCreators } from 'flocs-visual-components';
import { getTaskForEnv, start } from '../actions/practiceActions';
import CompleteTaskModal from '../components/CompleteTaskModal';

// set single task environment
const taskEnvId = "single";

@connect((state, props) => {
  return {
    taskId: props.routeParams.taskId,
    solved: state.practice.stage === "ATTEMPTED" ? flocsSelector.getGameState(state, "single").stage == "solved" : false,
  }
})
export default class PracticeContainer extends React.Component {
  componentWillMount() {
    this.props.dispatch(getTaskForEnv(taskEnvId, this.props.taskId));
  }

  componentWillReceiveProps(props) {
    if (props.taskId !== this.props.taskId) {
      props.dispatch(getTaskForEnv(taskEnvId, props.taskId));
    }
  }

  render(){
    return (
      <div>
        <TaskEnvironmentContainer taskEnvironmentId={taskEnvId} />
        { this.props.solved && (
          <CompleteTaskModal />
        )}
      </div>
  )}
}


