import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import TaskEnvironmentContainer from './TaskEnvironmentContainer';
import { isSolved } from '../selectors/gameState';
import { startTaskInTaskEnvironment } from '../actions/taskEnvironment';
import CompleteTaskModal from '../components/CompleteTaskModal';

function getProps(state, props) {
  return {
    taskEnvironmentId: props.taskEnvironmentId,
    taskId: props.taskId,
    taskCompletionDialogPosition: props.taskCompletionDialogPosition,
    solved: isSolved(state, props.taskEnvironmentId),
  };
}

@connect(getProps, { startTaskInTaskEnvironment })
export default class PracticeContainer extends React.Component {
  componentWillMount() {
    this.startTask();
  }

  componentWillReceiveProps(props) {
    // if (!this.props.solved && props.solved) {
    //   this.props.dispatch(solveTaskAndRecommend())
    // }
    if (props.taskId !== this.props.taskId) {
      this.startTask();
    }
  }

  startTask() {
    this.props.startTaskInTaskEnvironment(this.props.taskEnvironmentId, this.props.taskId);
  }

  render() {
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
    );
  }
}


PracticeContainer.propTypes = {
  taskEnvironmentId: PropTypes.string,
  taskId: PropTypes.string,
  solved: PropTypes.bool,
  startTaskInTaskEnvironment: PropTypes.func,
  taskCompletionDialogPosition: PropTypes.string,
  containerStyle: PropTypes.object,
};


PracticeContainer.defaultProps = {
  taskCompletionDialogPosition: 'modal',
  containerStyle: {},
};

