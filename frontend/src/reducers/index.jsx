import { combineReducers } from 'redux';
import { routerReducer } from 'react-router-redux';
import { flocsComponentsReducer } from 'flocs-visual-components';
import { practiceReducer } from './practiceReducer';
import { taskSessionReducer } from './taskSessionReducer';
import { tasksReducer } from './tasksReducer';

const reducers = combineReducers({
  tasks: tasksReducer,
  taskSession: taskSessionReducer,
  practice: practiceReducer,
  flocsComponents: flocsComponentsReducer,
  routing: routerReducer
});

export default reducers;

