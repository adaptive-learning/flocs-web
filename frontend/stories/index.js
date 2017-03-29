import React from 'react';
import { storiesOf, action, linkTo } from '@kadira/storybook';
import Welcome from './Welcome';
import BlocklyEditor from '../src/components/BlocklyEditor';
import CodeEditor from '../src/components/CodeEditor';


storiesOf('Welcome', module)
  .add('to Storybook', () => (
    <Welcome showApp={linkTo('CodeEditor')}/>
  ));


storiesOf('BlocklyEditor', module)
  .add('fixed size', () => (
    <div style={{ position: 'absolute', top: 0, bottom: 0, left: 0, right: 0 }} >
      <div style={{ backgroundColor: 'blue', height: '50px', width: '100%' }} />
      <span
        style={{
          display: 'inline-block',
          position: 'absolute',
          backgroundColor: 'red',
          top: '50px',
          bottom: '0px',
          left: '0px',
          right: '300px',
        }}
      >
        <BlocklyEditor
          onChange={action('onChange')}
        />
      </span>
      <span
        style={{
          display: 'inline-block',
          position: 'absolute',
          right: 0,
          width: '300px',
          top: '50px',
          bottom: 0,
          backgroundColor: 'yellow',
        }}
      />
    </div>
  ));

storiesOf('CodeEditor', module)
  .add('fixed size', () => (
    <div style={{ position: 'absolute', width: 600, height: 600 }}>
      <CodeEditor
        code="print('Los Karlos was here!')"
        onChange={action('onChange')}
      />
    </div>
  ))
  .add('full screen', () => (
    <div style={{ position: 'absolute', top: 0, bottom: 0, width: '100%' }}>
      <CodeEditor
        code="print('Where is the punched pocket?')"
        onChange={action('onChange')}
      />
    </div>
  ));
