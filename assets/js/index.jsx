import React from 'react'
import ReactDOM from 'react-dom'
import { createStore, applyMiddleware } from 'redux'
import { Provider } from 'react-redux';
import routes from './config/routes'
import reducers from './reducers'
import createLogger from 'redux-logger'
import { syncHistoryWithStore } from 'react-router-redux'
import { Router, Route, hashHistory } from 'react-router'

const logger = createLogger();
const store = createStore(reducers, applyMiddleware(logger))

const history = syncHistoryWithStore(hashHistory, store);

const app = (
  <Provider store={store}>
    <Router history={history}>
      {routes}
    </Router>
  </Provider>
);

const mountElement = document.getElementById('flocsApp')

ReactDOM.render(app, mountElement);
