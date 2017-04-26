import { combineReducers } from 'redux';
import { intlReducer } from 'react-intl-redux';
import { routerReducer } from 'react-router-redux';
import reduceApp from './app';
import reduceBlocks from './blocks';
import reduceCategories from './categories';
import reduceInstructions from './instructions';
import reduceLevels from './levels';
import reduceTasks from './tasks';
import reduceToolboxes from './toolboxes';
import reduceStudent from './student';
import reduceRecommendation from './recommendation';


import reduceTaskEnvironments from './taskEnvironments';
import reduceTaskEditor from './taskEditor';
import { taskSessionReducer } from './taskSessionReducer';
import menuReducer from './menu';


export const reducers = combineReducers({
  app: reduceApp,
  blocks: reduceBlocks,
  categories: reduceCategories,
  instructions: reduceInstructions,
  levels: reduceLevels,
  tasks: reduceTasks,
  toolboxes: reduceToolboxes,
  student: reduceStudent,
  recommendation: reduceRecommendation,

  taskEnvironments: reduceTaskEnvironments,
  taskEditor: reduceTaskEditor,
  taskSession: taskSessionReducer,
  menu: menuReducer,
  intl: intlReducer,
  routing: routerReducer,
});


export default reducers;
