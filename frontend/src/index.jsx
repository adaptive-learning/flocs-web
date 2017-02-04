import React from 'react'
import ReactDOM from 'react-dom'
import thunk from 'redux-thunk';
import { createStore, applyMiddleware } from 'redux'
import { Provider } from 'react-redux';
import routes from './config/routes'
import reducers from './reducers'
import createLogger from 'redux-logger'
import promise from 'redux-promise-middleware'
import { Router, browserHistory } from 'react-router'
import { FlocsProvider } from 'flocs-visual-components';

// include bootstrap
import 'bootstrap/dist/css/bootstrap.css';

// axios config
import './config/axiosConfig'

const logger = createLogger();

const store = createStore(reducers, applyMiddleware(promise(), thunk, logger));

const app = (
  <Provider store={store}>
    <FlocsProvider>
      <Router history={browserHistory}>
        {routes}
      </Router>
    </FlocsProvider>
  </Provider>
);

const mountElement = document.getElementById('flocsApp')

ReactDOM.render(app, mountElement);
