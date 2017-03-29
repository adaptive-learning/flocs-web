const ordering = [
  'env.space-world',
  'env.toolbox',
  'env.snapping',
  'env.controls',
  'object.asteroid',
  'object.meteoroid',
  'object.diamond',
  'object.wormhole',
  'diamonds-status',
  'energy-status',
  'action-limit',
  'block.fly',
  'block.shoot',
  'block.repeat',
  'block.while',
  'block.color',
  'block.position',
  'block.if',
  'block.if-else',
];


export function getInstructions(task) {
  // return ['env.snapping', 'action-limit'];
  return ordering.filter(instruction => containsInstruction(task, instruction));
}


function containsInstruction(task, instruction) {
  switch (instruction) {
    case 'env.space-world':
    case 'env.toolbox':
    case 'env.snapping':
    case 'env.controls':
      return true;
    case 'object.asteroid':
      return containsObject(task, 'A');
    case 'object.meteoroid':
      return containsObject(task, 'M');
    case 'object.wormhole':
      return containsObject(task, 'W');
    case 'object.diamond':
    case 'diamonds-status':
      return containsObject(task, 'D');
    case 'energy-status':
      return task.setting.energy != null;
    case 'action-limit':
      return task.setting.actionsLimit != null;
  // TODO: use solution to filter block instructions
    case 'block.fly':
    case 'block.shoot':
    case 'block.repeat':
    case 'block.while':
    case 'block.color':
    case 'block.position':
    case 'block.if':
    case 'block.if-else':
      return true;
    default:
      throw new Error(`Missing containsInstruction definition for ${instruction}`);
  }
}


function containsObject(task, objectLabel) {
  const allLabels = task.setting.fields.map(
    row => row.map(field => field[0] + field[1].join('')).join('')).join('');
  return allLabels.indexOf(objectLabel) >= 0;
}
