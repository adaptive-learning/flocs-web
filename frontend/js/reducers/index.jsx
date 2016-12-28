import { combineReducers } from 'redux';
import { routerReducer } from 'react-router-redux';
import { flocsComponentsReducer } from 'flocs-visual-components';
import { practiceReducer } from './practiceReducer';
import { taskInstanceReducer } from './taskInstanceReducer';
import { tasksReducer } from './tasksReducer';

const reducers = combineReducers({
  tasks: tasksReducer,
  taskInstance: taskInstanceReducer,
  practice: practiceReducer,
  flocsComponents: flocsComponentsReducer,
  routing: routerReducer
});

export default reducers;

