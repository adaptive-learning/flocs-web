import React from 'react';
import { connect } from 'react-redux';
import TaskEnvironmentContainer from './TaskEnvironmentContainer';
import { getGameState } from '../selectors/gameState' ;
import { getTaskForEnv, solveTaskAndRecommend } from '../actions/practiceActions';
import CompleteTaskModal from '../components/CompleteTaskModal';

function getProps(state, props) {
  return {
    taskEnvironmentId: props.taskEnvironmentId,
    taskCompletionDialogPosition: props.taskCompletionDialogPosition,
    solved: state.practice.stage === "ATTEMPTED" ? getGameState(state, props.taskEnvironmentId).stage == "solved" : false,
  }
}

@connect(getProps)
export default class PracticeContainer extends React.Component {
  componentWillReceiveProps(props) {
    if (!this.props.solved && props.solved) {
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


