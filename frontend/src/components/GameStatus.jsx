import React, { PropTypes } from 'react';
import TaskName from './TaskName';
import Icon from './Icon';

export default function GameStatus({ taskId, solved, dead, diamonds, energy, actions }) {
  return (
    <span style={{ display: 'block' }}>
      <span style={{ display: 'block' }}>
        <TaskName taskId={taskId} />
        {solved && <span style={{ float: 'right' }}>&#10003;</span>}
        {dead && <span style={{ float: 'right' }}>&#10005;</span>}
      </span>
      <span style={{ display: 'block' }}>
        { diamonds.total > 0 &&
          <span className="instructionable-diamonds-status">
            <Icon name="diamond" /> {diamonds.taken}/{diamonds.total}&nbsp;&nbsp;
          </span>
        }
        { energy.full !== null &&
          <span className="instructionable-energy-status">
            <Icon name="energy" /> {energy.current}/{energy.full}&nbsp;&nbsp;
          </span>
        }
        { actions.limit !== null &&
          <span className="instructionable-action-limit">
            <Icon name="actions" /> {actions.used}/{actions.limit}&nbsp;&nbsp;
          </span>
        }
      </span>
    </span>
  );
}

GameStatus.propTypes = {
  taskId: PropTypes.string.isRequired,
  diamonds: PropTypes.object.isRequired,
  energy: PropTypes.object.isRequired,
  actions: PropTypes.object.isRequired,
  solved: PropTypes.bool,
  dead: PropTypes.bool,
};

GameStatus.defaultProps = {
  solved: false,
  dead: false,
};
