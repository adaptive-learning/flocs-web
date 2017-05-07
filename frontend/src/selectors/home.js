import { isSolved } from '../selectors/gameState';

const spaceWorldDemoEnvironmentName = 'home-commands';

export function isSpaceWorldDemoSolved(state) {
  return isSolved(state, spaceWorldDemoEnvironmentName);
}
