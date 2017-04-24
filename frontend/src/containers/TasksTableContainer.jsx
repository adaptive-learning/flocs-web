import React from 'react';
import { connect } from 'react-redux';
import muiThemeable from 'material-ui/styles/muiThemeable';
import TasksTable from '../components/TasksTable';
import { fetchPraticeOverview } from '../actions/api';


function mapStateToProps(state) {
  return {
    tasks: state.tasks,
    categories: state.categories,
    recommendation: state.recommendation,
  };
}


@connect(mapStateToProps, { fetchPraticeOverview })
@muiThemeable()
export default class TasksTableContainer extends React.Component {
  componentWillMount() {
    this.props.fetchPraticeOverview();
  }

  render() {
    const { tasks, categories } = this.props;
    const allCategoryIds = Object.keys(categories);
    const compareCategoryIds = (a, b) => categories[a].level - categories[b].level;
    const orderedCategoryIds = allCategoryIds.sort(compareCategoryIds);
    const tasksInCategories = orderedCategoryIds.map(categoryId => ({
      category: categories[categoryId],
      tasks: categories[categoryId].tasks.map(id => tasks[id]),
    }));

    // TODO: move styling to a component
    const longPageContentStyle = {
      maxWidth: 1200,
      margin: '20px auto',
      backgroundColor: this.props.muiTheme.palette.canvasColor,
    };
    return (
      <div style={longPageContentStyle}>
        <TasksTable
          tasksInCategories={tasksInCategories}
          urlBase="/task/"
          recommendation={this.props.recommendation}
        />
      </div>
    );
  }
}
