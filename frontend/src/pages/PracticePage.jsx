import React from 'react';
import { connect } from 'react-redux';
import { TaskEnvironmentContainer, flocsSelector, flocsActionCreators } from 'flocs-visual-components';
import { getTaskForEnv, start, solveTaskAndRecommend } from '../actions/practiceActions';
import PracticeContainer from '../containers/PracticeContainer';

const practiceTaskEnvironmentId = 'single';

function getProps(state, props) {
  return {
    taskId: props.routeParams.taskId,
  };
}

@connect(getProps, { getTaskForEnv })
export default class PracticePage extends React.Component {
  componentWillMount() {
    this.props.getTaskForEnv(practiceTaskEnvironmentId, this.props.taskId);
  }

  componentWillReceiveProps(props) {
    if (props.taskId !== this.props.taskId) {
      this.props.getTaskForEnv(practiceTaskEnvironmentId, props.taskId);
    }
  }

  render() {
    return (
      <PracticeContainer taskEnvironmentId={practiceTaskEnvironmentId} />
    );
  }
}


