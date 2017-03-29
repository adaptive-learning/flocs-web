import React from 'react';
import ReactDOM from 'react-dom';
import { FlocsProvider, SpaceGame, parseSpaceWorld } from 'flocs-visual-components';

function handleControlClicked(control) {
  console.log('control:', control);
}

const gameState = {
  fields: parseSpaceWorld(`\
    |b |bM|bS|b |b |
    |k |k |k |kA|k |
    |kA|k |k |k |k |
    |k |kM|k |k |k |
    |k |k |k |k |kM|`),
  stage: 'solved',
  diamonds: { taken: 2, total: 2 },
  energy: { current: 1, full: 2 },
};

const component = (
  <FlocsProvider>
    <SpaceGame
      gameState={gameState}
      onControlClicked={handleControlClicked}
    />
  </FlocsProvider>
);

const mountElement = document.getElementById('spaceGameExample');
if (mountElement !== null) {
  ReactDOM.render(component, mountElement);
}
