import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import createPromiseMiddleware from 'redux-promise-middleware';
import createLoggerMiddleware from 'redux-logger';
import rootReducer from './reducers';
import { getLocalizationSetting } from './localization';
import { initGlobalBlockly } from './core/blockly';
import { initGlobalTheme } from './theme';



export function globalConfiguration() {
  initGlobalTheme();
  initGlobalBlockly();
}


export function configureStore(initialState) {
  const initialStateWithLocalization = {
    ...initialState,
    intl: getLocalizationSetting(),
  };
  const promise = createPromiseMiddleware();
  const logger = createLoggerMiddleware();
  const middleware = applyMiddleware(promise, thunk, logger);
  const store = createStore(rootReducer, initialStateWithLocalization, middleware);

  if (module.hot) {
    // Enable Webpack hot module replacement for reducers
    module.hot.accept('./reducers', () => {
      const nextRootReducer = require('./reducers/index').reducers;
      store.replaceReducer(nextRootReducer);
    });
  }

  return store;
}
