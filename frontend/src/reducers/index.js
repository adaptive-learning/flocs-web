import { combineReducers } from 'redux';
import { intlReducer } from 'react-intl-redux';
import { routerReducer } from 'react-router-redux';
import reduceApp from './app';
import reduceBlocks from './blocks';
import reduceCategories from './categories';
import reduceTasks from './tasks';
import reduceInstructions from './instructions';
import reduceToolboxes from './toolboxes';
import reduceStudent from './student';
import reduceRecommendation from './recommendation';


import reduceTaskEnvironments from './taskEnvironments';
import reduceTaskEditor from './taskEditor';
import { practiceReducer } from './practiceReducer';
import { taskSessionReducer } from './taskSessionReducer';
import menuReducer from './menu';


export const reducers = combineReducers({
  app: reduceApp,
  blocks: reduceBlocks,
  categories: reduceCategories,
  tasks: reduceTasks,
  instructions: reduceInstructions,
  toolboxes: reduceToolboxes,
  // TODO: reducers for other entities
  student: reduceStudent,
  recommendation: reduceRecommendation,

  taskEnvironments: reduceTaskEnvironments,
  taskEditor: reduceTaskEditor,
  taskSession: taskSessionReducer,
  practice: practiceReducer,
  menu: menuReducer,
  intl: intlReducer,
  routing: routerReducer,
});


export default reducers;
