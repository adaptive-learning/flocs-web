import React from 'react';
import { connect } from 'react-redux';
import { TaskEnvironmentContainer, flocsSelector, flocsActionCreators } from 'flocs-visual-components';
import { getTaskForEnv, start, solveTaskAndRecommend } from '../actions/practiceActions';
import CompleteTaskModal from '../components/CompleteTaskModal';

function getProps(state, props) {
  return {
    taskEnvironmentId: props.taskEnvironmentId,
    taskCompletionDialogPosition: props.taskCompletionDialogPosition,
    solved: state.practice.stage === "ATTEMPTED" ? flocsSelector.getGameState(state, props.taskEnvironmentId).stage == "solved" : false,
  }
}

@connect(getProps)
export default class PracticeContainer extends React.Component {
  componentWillReceiveProps(props) {
    if (props.solved) {
      this.props.dispatch(solveTaskAndRecommend())
    }
  }

  render(){
    return (
      <div>
        <div style={this.props.containerStyle}>
          <TaskEnvironmentContainer taskEnvironmentId={this.props.taskEnvironmentId} />
        </div>
        <CompleteTaskModal
          open={this.props.solved}
          position={this.props.taskCompletionDialogPosition}
        />
      </div>
  )}
}


PracticeContainer.defaultProps = {
  taskCompletionDialogPosition: 'modal',
  containerStyle: {},
};


