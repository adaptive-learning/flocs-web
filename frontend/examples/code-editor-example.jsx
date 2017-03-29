import React from 'react';
import ReactDOM from 'react-dom';
import { FlocsProvider, CodeEditor } from 'flocs-visual-components';

function handleChange(newCode) {
  console.log('new code:', newCode);
}

// CodeEditor fills 100% width and height of its parent
const component = (
  <FlocsProvider>
    <div style={{ position: 'absolute', top: 0, bottom: 0, width: '100%' }}>
      <CodeEditor
        code="print('Los Karlos was here!')"
        onChange={handleChange}
      />
    </div>
  </FlocsProvider>
);

const mountElement = document.getElementById('codeEditorExample');
if (mountElement !== null) {
  ReactDOM.render(component, mountElement);
}
