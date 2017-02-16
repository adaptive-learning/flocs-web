import React from 'react'
import ReactDOM from 'react-dom'
import routes from './config/routes'
import reducers from './reducers'
import { Router, browserHistory } from 'react-router'
import { FlocsProvider } from 'flocs-visual-components';

// include bootstrap
import 'bootstrap/dist/css/bootstrap.css';

// axios config
import './config/axiosConfig'

const app = (
  <FlocsProvider reducers={reducers}>
    <Router history={browserHistory}>
      {routes}
    </Router>
  </FlocsProvider>
);

const mountElement = document.getElementById('flocsApp')

ReactDOM.render(app, mountElement);
