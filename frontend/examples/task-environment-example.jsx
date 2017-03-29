import React, { PropTypes } from 'react';
import ReactDOM from 'react-dom';
import { connect } from 'react-redux';
import { FlocsProvider,
         TaskEnvironmentContainer,
         flocsActionCreators,
         flocsActionTypes,
         flocsSelector,
         parseSpaceWorld } from 'flocs-visual-components';

function createAppComponent() {
  // definiton of two example tasks
  const task1 = {
    taskId: 'two-steps-forward',
    categoryId: 'moves',
    setting: {
      fields: parseSpaceWorld(`
        |b |b |b |b |b |
        |k |k |k |k |k |
        |k |k |kS|k |k |`),
    },
  };

  const task2 = {
    taskId: 'ladder',
    categoryId: 'repeat',
    setting: {
      fields: parseSpaceWorld(`
        |b |bA|bM|bA|b |
        |k |kA|k |kA|k |
        |k |kA|kM|kA|k |
        |k |kA|k |kA|k |
        |k |kA|kM|kA|k |
        |k |kA|k |kA|k |
        |k |kA|kM|kA|k |
        |k |kA|k |kA|k |
        |k |kA|kS|kA|k |`),
      energy: 4,
      actionsLimit: 2,
    },
  };
  const tasks = [task1, task2];
  const taskEnvId = 'single';

  // component for task environment with next-task button
  class PracticeEnvironment extends React.Component {
    constructor(props) {
      super(props);
      this.setNextTask = this.setNextTask.bind(this);
      this.setNextTask();
    }

    setNextTask() {
      // for our demo, we will simply loop over the two tasks
      const task = tasks[this.props.taskIndex % 2];
      this.props.setTask(taskEnvId, task);
    }

    render() {
      const { taskSolved } = this.props;
      return (
        <div style={{ position: 'absolute', top: 0, bottom: 0, left: 0, right: 0 }} >
          <TaskEnvironmentContainer taskEnvironmentId={taskEnvId} />
          {taskSolved &&
            <div style={{ position: 'fixed', bottom: 10, left: 10 }} >
              <button onClick={this.setNextTask}>Next task</button>
            </div>
          }
        </div>
      );
    }
  }
  PracticeEnvironment.propTypes = {
    taskSolved: PropTypes.bool.isRequired,
    taskIndex: PropTypes.number.isRequired,
    setTask: PropTypes.func.isRequired,
  };

  // create redux container for your environment subscribing to store
  function mapStateToProps(state) {
    const gameState = flocsSelector.getGameState(state, taskEnvId);
    const taskSolved = gameState.stage === 'solved';
    const taskIndex = state.myApp.taskIndex;
    return { taskSolved, taskIndex };
  }
  const actionCreators = { setTask: flocsActionCreators.setTask };
  const PracticeEnvironmentContainer = connect(mapStateToProps,
                                               actionCreators)(PracticeEnvironment);
  // create your root app component
  const appComponent = (
    <FlocsProvider reducers={{ myApp: myAppReducer }}>
      <PracticeEnvironmentContainer />
    </FlocsProvider>
  );
  return appComponent;
}


// you can make your reducer respond to actions dispatch by flocsComponents
function myAppReducer(state = { taskIndex: 0, attempted: false }, action) {
  switch (action.type) {
    case flocsActionTypes.SET_TASK:
      console.log('myAppReducer responding to new task');
      return {
        taskIndex: state.taskIndex + 1,
        attempted: false,
      };
    case flocsActionTypes.TASK_ATTEMPTED:
      console.log('myAppReducer responding to attempted task');
      return {
        ...state,
        attempted: true,
      };
    default:
      return state;
  }
}


const mountElement = document.getElementById('taskEnvironmentExample');
if (mountElement !== null) {
  ReactDOM.render(createAppComponent(), mountElement);
}
