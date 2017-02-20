import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import NextTaskButton from '../components/NextTaskButton';

function getProps(state) {
  // TODO: if the recommendation is same as the current task, discard it
  let task = null;
  const taskId = state.practice.recommendation;
  if (taskId) {
    task = {
      taskId,
      url: `task/${taskId}`
    };
  }
  return { task };
}

@connect(getProps)
class NextTaskButtonContainer extends React.Component {
  render() {
    if (!this.props.task) {
      return null;
    }
    return (
      <NextTaskButton task={this.props.task} />
    );
  }
}

NextTaskButtonContainer.propTypes = {
  task: PropTypes.object,
};

export default NextTaskButtonContainer;
