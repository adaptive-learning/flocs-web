import React from 'react';
import { connect } from 'react-redux'
import { Col } from 'react-bootstrap'

// actions
import { start } from '../actions/practiceActions'

// flocs visual components
import { CodeEditorContainer, SpaceGameContainer, flocsActionCreators } from 'flocs-visual-components';

// set single task environment
const taskEnvId = "single";

@connect((state) => {
    return {
        task: state.task.task,
        ok: state.task.ok
    };
})
export default class TaskEnvironment extends React.Component {
    constructor(props) {
        super(props);
        // Start session
        props.dispatch(start(taskEnvId));
        props.dispatch(flocsActionCreators.createTaskEnvironment(taskEnvId));
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


