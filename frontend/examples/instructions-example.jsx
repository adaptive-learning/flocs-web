import React, { PropTypes } from 'react';
import ReactDOM from 'react-dom';
import { connect } from 'react-redux';
import { FlocsProvider,
         TaskEnvironmentContainer,
         flocsActionCreators,
         parseSpaceWorld } from 'flocs-visual-components';

function createAppComponent() {
  const task = {
    taskId: 'ladder',
    categoryId: 'repeat',
    setting: {
      fields: parseSpaceWorld(`
        |b |bA|bW|bA|b |
        |kM|kA|kM|kA|kM|
        |kD|kA|kD|kA|k |
        |kW|kA|k |kA|k |
        |k |kA|kS|kA|k |`),
      energy: 2,
      actionsLimit: 2,
    },
  };
  const taskEnvId = 'single';

  class PracticeEnvironment extends React.Component {
    componentWillMount() {
      this.props.setTask(taskEnvId, task);
    }

    render() {
      return (
        <div style={{ position: 'absolute', top: 0, bottom: 0, left: 0, right: 0 }} >
          <TaskEnvironmentContainer taskEnvironmentId={taskEnvId} />
        </div>
      );
    }
  }
  PracticeEnvironment.propTypes = {
    setTask: PropTypes.func.isRequired,
  };

  const actionCreators = { setTask: flocsActionCreators.setTask };
  const PracticeEnvironmentContainer = connect(null, actionCreators)(PracticeEnvironment);
  const appComponent = (
    <FlocsProvider>
      <PracticeEnvironmentContainer />
    </FlocsProvider>
  );
  return appComponent;
}


const mountElement = document.getElementById('instructionsExample');
if (mountElement !== null) {
  ReactDOM.render(createAppComponent(), mountElement);
}
