import React, { PropTypes } from 'react';
import { Link } from 'react-router';
import RaisedButton from 'material-ui/RaisedButton';
import { TaskName } from 'flocs-visual-components';


export default function NextTaskButton({ task }) {
  return (
    <span style={{ display: 'inline-block' }}>
      <div> Doporučená úloha:</div>
      <Link to={task.url}>
        <RaisedButton label={<TaskName taskId={task.taskId} />} primary={true} />
      </Link>
    </span>
  );
}


NextTaskButton.propTypes = {
  task: PropTypes.object.isRequired,
};
