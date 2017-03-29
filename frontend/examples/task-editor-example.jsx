import React from 'react';
import ReactDOM from 'react-dom';
import { FlocsProvider,
         TaskEditorContainer } from 'flocs-visual-components';


function createAppComponent() {
  const appComponent = (
    <FlocsProvider>
      <TaskEditorContainer />
    </FlocsProvider>
  );
  return appComponent;
}


const mountElement = document.getElementById('taskEditorExample');
if (mountElement !== null) {
  ReactDOM.render(createAppComponent(), mountElement);
}
