import { combineReducers } from 'redux'
import { routerReducer } from 'react-router-redux'
import { flocsComponentsReducer } from 'flocs-visual-components'
import { practiceReducer } from './practiceReducer'
import { taskInstanceReducer } from './taskInstanceReducer'

const reducers = combineReducers({
  taskInstance: taskInstanceReducer,
  practice: practiceReducer,
  flocsComponents: flocsComponentsReducer,
  routing: routerReducer
});

export default reducers;

