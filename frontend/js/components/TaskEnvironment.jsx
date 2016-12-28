import React from 'react';
import { connect } from 'react-redux';
import { Col } from 'react-bootstrap';
import { CodeEditorContainer, SpaceGameContainer, flocsSelector, flocsActionCreators } from 'flocs-visual-components';
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
export default class TaskEnvironment extends React.Component {

  componentWillMount() {
    this.props.dispatch(flocsActionCreators.createTaskEnvironment(taskEnvId));
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
        <Col xs={6} md={6}>
            <CodeEditorContainer taskEnvironmentId={taskEnvId}/>
        </Col>
        <Col xs={6} md={6}>
            <SpaceGameContainer taskEnvironmentId={taskEnvId}/>
        </Col>
        { this.props.solved && (
          <CompleteTaskModal />
        )}
      </div>
  )}
}


