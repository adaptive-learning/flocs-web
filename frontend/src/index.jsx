import React from 'react'
import ReactDOM from 'react-dom'
import routes from './config/routes'
import reducers from './reducers'
import { FlocsProvider } from 'flocs-visual-components';

// axios config
import './config/axiosConfig'


const app = (
  <FlocsProvider router reducers={reducers}>
    {routes}
  </FlocsProvider>
);

const mountElement = document.getElementById('flocsApp')

ReactDOM.render(app, mountElement);
