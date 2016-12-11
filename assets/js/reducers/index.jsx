import { combineReducers } from 'redux'
import { routerReducer } from 'react-router-redux'
import { flocsComponentsReducer } from 'flocs-visual-components'
import { practiceReducer } from './practiceReducer'

const reducers = combineReducers({
  task: practiceReducer,
  flocsComponents: flocsComponentsReducer,
  routing: routerReducer
});

export default reducers;

