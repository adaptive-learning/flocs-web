import React from 'react'
import ReactDOM from 'react-dom'
import routes from './config/routes'
import FlocsProvider from './FlocsProvider';
import { globalConfiguration, configureStore } from './config';

// axios config - TODO: move to config.js
import './config/axiosConfig';

globalConfiguration();
const store = configureStore();

const app = (
  <FlocsProvider store={store} router>
    {routes}
  </FlocsProvider>
);

const mountElement = document.getElementById('flocsApp')

ReactDOM.render(app, mountElement);
