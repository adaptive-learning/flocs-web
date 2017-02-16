import { routerReducer } from 'react-router-redux';
import { practiceReducer } from './practiceReducer';
import { taskSessionReducer } from './taskSessionReducer';
import { tasksReducer } from './tasksReducer';

const reducers = {
  tasks: tasksReducer,
  taskSession: taskSessionReducer,
  practice: practiceReducer,
  routing: routerReducer
};

export default reducers;

