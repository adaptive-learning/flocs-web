import React from 'react';
import { connect } from 'react-redux';
import { startPractice } from '../actions/practiceActions';
import PracticeContainer from '../containers/PracticeContainer';

const practiceTaskEnvironmentId = 'single';

function getProps(state, props) {
  return {
    taskId: props.routeParams.taskId,
  };
}

@connect(getProps, { startPractice })
export default class PracticePage extends React.Component {
  componentWillMount() {
    this.props.startPractice(practiceTaskEnvironmentId, this.props.taskId);
  }

  componentWillReceiveProps(props) {
    if (props.taskId !== this.props.taskId) {
      this.props.startPractice(practiceTaskEnvironmentId, props.taskId);
    }
  }

  render() {
    return (
      <div
        style={{
          position: 'absolute',
          top: 64,  // TODO: unhardcode using app height in flocs-theme
          bottom: 0,
          left: 0,
          right: 0,
        }}
      >
        <PracticeContainer taskEnvironmentId={practiceTaskEnvironmentId} />
      </div>
    );
  }
}


