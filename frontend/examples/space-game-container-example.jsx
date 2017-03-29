import React, { PropTypes } from 'react';
import ReactDOM from 'react-dom';
import { connect } from 'react-redux';
import { FlocsProvider,
         SpaceGameContainer,
         flocsActionCreators,
         flocsSelector,
         parseSpaceWorld } from 'flocs-visual-components';

function createAppComponent() {
  const task = {
    taskId: 'two-steps-forward',
    categoryId: 'moves',
    setting: {
      fields: parseSpaceWorld(`
        |b |b |b |b |b |
        |k |k |k |k |k |
        |k |k |kS|k |k |`),
    },
  };
  const taskEnvId = 'demo';

  class SpaceGameDemoWrapper extends React.Component {
    componentWillMount() {
      this.props.setTask(taskEnvId, task);
    }

    render() {
      const { taskSolved } = this.props;
      return (
        <div>
          <SpaceGameContainer
            taskEnvironmentId="demo"
            controls={['fly', 'left', 'right', 'reset']}
          />
          {taskSolved &&
            <p>Task solved!</p>
          }
        </div>
      );
    }
  }
  SpaceGameDemoWrapper.propTypes = {
    taskSolved: PropTypes.bool.isRequired,
    setTask: PropTypes.func.isRequired,
  };

  function getProps(state) {
    const gameState = flocsSelector.getGameState(state, taskEnvId);
    const taskSolved = gameState.stage === 'solved';
    return { taskSolved };
  }
  const actionCreators = { setTask: flocsActionCreators.setTask };
  const SpaceGameDemoContainer = connect(getProps, actionCreators)(SpaceGameDemoWrapper);

  const appComponent = (
    <FlocsProvider>
      <SpaceGameDemoContainer />
    </FlocsProvider>
  );
  return appComponent;
}

const mountElement = document.getElementById('spaceGameContainerExample');
if (mountElement !== null) {
  ReactDOM.render(createAppComponent(), mountElement);
}
