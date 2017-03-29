import { combineReducers } from 'redux';
import { intlReducer } from 'react-intl-redux';
import { routerReducer } from 'react-router-redux';
import reduceTaskEnvironments from './taskEnvironments';
import reduceTaskEditor from './taskEditor';
import { reduceInstructions, reduceInstructionLayer } from './instructions';
import { reduceStudent } from './student';
import { practiceReducer } from './practiceReducer';
import { taskSessionReducer } from './taskSessionReducer';
import { tasksReducer } from './tasksReducer';
import menuReducer from './menu';


export const reducers = combineReducers({
  student: reduceStudent,
  taskEnvironments: reduceTaskEnvironments,
  taskEditor: reduceTaskEditor,
  instructions: reduceInstructions,
  instructionLayer: reduceInstructionLayer,
  tasks: tasksReducer,
  taskSession: taskSessionReducer,
  practice: practiceReducer,
  menu: menuReducer,
  intl: intlReducer,
  routing: routerReducer,
});


export default reducers;
