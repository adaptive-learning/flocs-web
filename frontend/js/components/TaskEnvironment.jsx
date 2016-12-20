import React from 'react';
import { connect } from 'react-redux'
import { Col } from 'react-bootstrap'

// actions
import { getTaskForEnv, start } from '../actions/practiceActions'

// flocs visual components
import { CodeEditorContainer, SpaceGameContainer, flocsActionCreators } from 'flocs-visual-components';

// set single task environment
const taskEnvId = "single";

@connect((state, props) => {
    return {
        taskId: props.routeParams.taskId
    }
})
export default class TaskEnvironment extends React.Component {

    componentWillMount() {
        // Start session
        this.props.dispatch(flocsActionCreators.createTaskEnvironment(taskEnvId));
        if (typeof this.props.taskId === 'undefined') {
            this.props.dispatch(start(taskEnvId))
        } else {
            this.props.dispatch(getTaskForEnv(taskEnvId, this.props.taskId));
        }
    }

    componentWillReceiveProps(props) {
        props.dispatch(getTaskForEnv(taskEnvId, props.taskId));
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
            </div>
    )}
}


