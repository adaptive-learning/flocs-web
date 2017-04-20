import { combineReducers } from 'redux';
import { intlReducer } from 'react-intl-redux';
import { routerReducer } from 'react-router-redux';
import reduceBlocks from './blocks';
import reduceCategories from './categories';
import reduceTasks from './tasks';
import reduceInstructions from './instructions';
import reduceStudent from './student';


import reduceTaskEnvironments from './taskEnvironments';
import reduceTaskEditor from './taskEditor';
import { practiceReducer } from './practiceReducer';
import { taskSessionReducer } from './taskSessionReducer';
import menuReducer from './menu';


export const reducers = combineReducers({
  blocks: reduceBlocks,
  categories: reduceCategories,
  tasks: reduceTasks,
  instructions: reduceInstructions,
  // TODO: reducers for other entities
  student: reduceStudent,

  taskEnvironments: reduceTaskEnvironments,
  taskEditor: reduceTaskEditor,
  taskSession: taskSessionReducer,
  practice: practiceReducer,
  menu: menuReducer,
  intl: intlReducer,
  routing: routerReducer,
});


export default reducers;
