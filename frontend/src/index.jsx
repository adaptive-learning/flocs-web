import React from 'react'
import ReactDOM from 'react-dom'
import routes from './config/routes'
import reducers from './reducers'
import { initGlobalBlockly } from './core/blockly';
import { initGlobalTheme } from './theme';
import FlocsProvider from './FlocsProvider';

// axios config
import './config/axiosConfig'

// global initializations
initGlobalTheme();
initGlobalBlockly();


const app = (
  <FlocsProvider router reducers={reducers}>
    {routes}
  </FlocsProvider>
);

const mountElement = document.getElementById('flocsApp')

ReactDOM.render(app, mountElement);
