import React, { PropTypes } from 'react';
import { Link } from 'react-router';
import RaisedButton from 'material-ui/RaisedButton';
import TaskName from './TaskName';


export default function NextTaskButton({ task }) {
  let visibility = 'hidden';
  let taskId = '';
  let url = '#';
  console.log('task is', task);
  if (task !== null) {
    visibility = true;
    taskId = task.taskId;
    url = task.url;
  }
  return (
    <span style={{ visibility, display: 'inline-block' }}>
      <div> Doporučená úloha:</div>
      <Link to={url}>
        <RaisedButton label={<TaskName taskId={taskId} />} primary={true} />
      </Link>
    </span>
  );
}


NextTaskButton.propTypes = {
  task: PropTypes.object,
};
