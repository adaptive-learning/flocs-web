import React, { PropTypes } from 'react';
import { Link } from 'react-router';
import { FormattedMessage } from 'react-intl';
import { Card, CardTitle, CardText } from 'material-ui/Card';
import { GridList, GridTile } from 'material-ui/GridList';
import TaskName from './TaskName';
import { theme } from '../theme';

// TODO: unhardcode categories
/* eslint-disable quote-props */
const categories = {
  moves: {
    categoryId: 'moves',
    levelId: 1,
  },
  world: {
    categoryId: 'world',
    levelId: 2,
  },
  repeat: {
    categoryId: 'repeat',
    levelId: 3,
  },
  'while': {
    categoryId: 'while',
    levelId: 4,
  },
  loops: {
    categoryId: 'loops',
    levelId: 5,
  },
  'if': {
    categoryId: 'if',
    levelId: 6,
  },
  comparing: {
    categoryId: 'comparing',
    levelId: 7,
  },
  'if-else': {
    categoryId: 'if-else',
    levelId: 8,
  },
  'final-challenge': {
    categoryId: 'final-challenge',
    levelId: 9,
  },
  uncategorized: {
    categoryId: 'uncategorized',
    levelId: 10,
  },
};

export default function TaskTable({ urlBase, tasks }) {
  const allCategoryIds = Object.keys(categories);
  const compareCategoryIds = (a, b) => categories[a].levelId - categories[b].levelId;
  const sortedCategoryIds = allCategoryIds.sort(compareCategoryIds);
  return (
    <div>
      { sortedCategoryIds.map(categoryId =>
        <CategoryTasks
          key={categoryId}
          urlBase={urlBase}
          category={categories[categoryId]}
          tasks={tasks.filter(task => task.categoryId === categoryId)}
        />)
      }
    </div>
  );
}

TaskTable.propTypes = {
  urlBase: PropTypes.string,
  tasks: PropTypes.array.isRequired,
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
        title={<FormattedMessage id={`category.${category.categoryId}`} />}
        subtitle={`Level ${category.levelId}`}
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
            <Link key={task.taskId} to={`${urlBase}${task.taskId}`}>
              <GridTile
                title={<TaskName taskId={task.taskId} />}
                subtitle={'2:30'}
              >
                <div
                  style={{
                    backgroundColor: theme.palette.primary3Color,
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
