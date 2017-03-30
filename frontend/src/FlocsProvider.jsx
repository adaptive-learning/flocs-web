import React, { PropTypes } from 'react';
import { Provider } from 'react-intl-redux';
import { Router, browserHistory } from 'react-router';
import { syncHistoryWithStore, routerReducer } from 'react-router-redux';
import { configureStore } from './config';
import FlocsThemeProvider from './theme/FlocsThemeProvider';


/**
 * Provides context for flocs components (store, localization, theme)
 */
export default function FlocsProvider({ children, store, router }) {
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
        {routedChildren}
      </FlocsThemeProvider>
    </Provider>
  );
}

FlocsProvider.propTypes = {
  children: PropTypes.node,
  router: PropTypes.bool,
};

FlocsProvider.defaultProps = {
  children: null,
  router: false,
};
