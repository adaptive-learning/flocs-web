import React, { PropTypes } from 'react';
import { Link } from 'react-router';
import { FormattedMessage } from 'react-intl';
import { Card, CardTitle, CardText } from 'material-ui/Card';
import { GridList, GridTile } from 'material-ui/GridList';
import TaskName from './TaskName';
import { theme } from '../theme';
import { translate } from '../localization';


export default function TaskTable({ urlBase, tasksInCategories }) {
  return (
    <div>
      { tasksInCategories.map(({ category, tasks }) =>
        <CategoryTasks
          key={category.id}
          urlBase={urlBase}
          category={category}
          tasks={tasks}
        />)
      }
    </div>
  );
}

TaskTable.propTypes = {
  urlBase: PropTypes.string,
  tasksInCategories: PropTypes.array.isRequired,
};

TaskTable.defaultProps = {
  urlBase: '/task/',
};


function CategoryTasks({ category, tasks, urlBase }) {
  if (tasks.length === 0) {
    return null;
  }
  return (
    <Card style={{ margin: 10 }}>
      <CardTitle
        title={<FormattedMessage id={`category.${category.id}`} />}
        subtitle={`Level ${category.level}`}
      />
      <CardText>
        <GridList
          cellHeight={120}
          cols={Math.min(5, Math.floor(window.innerWidth / 300))}
          style={{
            display: 'flex',
            flexWrap: 'wrap',
          }}
        >
          {tasks.map((task) => (
            <Link key={task.id} to={`${urlBase}${task.id}`}>
              <GridTile
                title={<TaskName taskId={task.id} />}
                subtitle={formatSolvingTime(task.time)}
              >
                <div
                  style={{
                    backgroundColor:
                      (task.solved) ? theme.palette.successColor : theme.palette.primary3Color,
                    width: '100%',
                    height: '100%',
                  }}
                />
              </GridTile>
            </Link>
          ))}
        </GridList>
      </CardText>
    </Card>
  );
}


CategoryTasks.propTypes = {
  category: PropTypes.object.isRequired,
  tasks: PropTypes.array.isRequired,
  urlBase: PropTypes.string,
};


function formatSolvingTime(time) {
  if (time == null) {
    return translate('not tackled');
  }
  // remove hours part if 0
  const parts = time.split(':');
  if (parts[0] === '00') {
    return parts.slice(1).join(':');
  }
  return time;
}
