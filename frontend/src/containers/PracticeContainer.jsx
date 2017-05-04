import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import TaskEnvironmentContainer from './TaskEnvironmentContainer';
import { isSolved } from '../selectors/gameState';
import { isTaskCompletionDialogOpen } from '../selectors/taskEnvironment';
import { getLevelInfo } from '../selectors/student';
import { startTaskInTaskEnvironment, closeTaskCompletionDialog } from '../actions/taskEnvironment';
import CompleteTaskModal from '../components/CompleteTaskModal';

function getProps(state, props) {
  return {
    taskEnvironmentId: props.taskEnvironmentId,
    taskId: props.taskId,
    solved: isSolved(state, props.taskEnvironmentId),
    taskCompletionDialogPosition: props.taskCompletionDialogPosition,
    isTaskCompletionDialogOpen: isTaskCompletionDialogOpen(state, props.taskEnvironmentId),
    levelInfo: getLevelInfo(state),
  };
}

@connect(getProps, { startTaskInTaskEnvironment, closeTaskCompletionDialog })
export default class PracticeContainer extends React.Component {
  constructor(props) {
    super(props);
    this.closeTaskCompletionDialog = this.props.closeTaskCompletionDialog.bind(this, this.props.taskEnvironmentId);
  }

  componentWillMount() {
    this.startTask(this.props.taskId);
  }

  componentWillReceiveProps(props) {
    //if (!this.props.solved && props.solved) {
    //  this.solveTask();
    //}
    if (this.props.taskId !== props.taskId) {
      this.startTask(props.taskId);
    }
  }

  startTask(taskId) {
    this.props.startTaskInTaskEnvironment(this.props.taskEnvironmentId, taskId);
  }

  render() {
    return (
      <div>
        <div style={this.props.containerStyle}>
          <TaskEnvironmentContainer taskEnvironmentId={this.props.taskEnvironmentId} />
        </div>
        <CompleteTaskModal
          open={this.props.isTaskCompletionDialogOpen}
          position={this.props.taskCompletionDialogPosition}
          handleClose={this.closeTaskCompletionDialog}
          levelInfo={this.props.levelInfo}
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
  solveTaskInTaskEnvironment: PropTypes.func,
  taskCompletionDialogPosition: PropTypes.string,
  containerStyle: PropTypes.object,
};


PracticeContainer.defaultProps = {
  taskCompletionDialogPosition: 'modal',
  containerStyle: {},
};

