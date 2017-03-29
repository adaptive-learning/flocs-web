import React, { PropTypes } from 'react';
import { Provider, intlReducer } from 'react-intl-redux';
import { Router, browserHistory } from 'react-router';
import { syncHistoryWithStore, routerReducer } from 'react-router-redux';
import { createStore, combineReducers, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import createPromiseMiddleware from 'redux-promise-middleware';
import createLoggerMiddleware from 'redux-logger';
import { getLocalizationSetting } from './localization';
import FlocsThemeProvider from './theme/FlocsThemeProvider';
import InstructionsContainer from './containers/InstructionsContainer';


/**
 * Provides context for flocs components (store, localization, theme)
 */
export default function FlocsProvider({ children, router, reducers }) {
  const initialState = {
    intl: getLocalizationSetting(),
  };
  const promise = createPromiseMiddleware();
  const logger = createLoggerMiddleware();
  const middleware = applyMiddleware(promise, thunk, logger);
  const store = createStore(reducers, initialState, middleware);
  let routedChildren = children;
  if (router) {
    const history = syncHistoryWithStore(browserHistory, store);
    routedChildren = (
      <Router history={history}>
        {children}
      </Router>
    );
  }

  return (
    <Provider store={store}>
      <FlocsThemeProvider>
        <InstructionsContainer />
        {routedChildren}
      </FlocsThemeProvider>
    </Provider>
  );
}

FlocsProvider.propTypes = {
  children: PropTypes.node,
  router: PropTypes.bool,
  reducers: PropTypes.func,
};

FlocsProvider.defaultProps = {
  children: null,
  reducers: {},
  router: false,
};
