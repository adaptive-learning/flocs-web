import React, { PropTypes } from 'react';
import { Provider, intlReducer } from 'react-intl-redux';
import { Router, browserHistory } from 'react-router';
import { syncHistoryWithStore, routerReducer } from 'react-router-redux';
import { getLocalizationSetting } from './localization';
import { configureStore } from './config';
import FlocsThemeProvider from './theme/FlocsThemeProvider';
import InstructionsContainer from './containers/InstructionsContainer';


/**
 * Provides context for flocs components (store, localization, theme)
 */
export default function FlocsProvider({ children, store, router }) {
  const initialState = {
    intl: getLocalizationSetting(),
  };
  // const store = configureStore(initialState);
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
};

FlocsProvider.defaultProps = {
  children: null,
  router: false,
};
