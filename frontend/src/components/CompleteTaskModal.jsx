import React from 'react';
import Dialog from 'material-ui/Dialog';
import { Link } from 'react-router'
import { connect } from 'react-redux'
import NextTaskButtonContainer from '../containers/NextTaskButtonContainer';

// actions
import { solveTaskAndRecommend, nextTask } from '../actions/practiceActions'

// TODO separate logic and presentation (component and container)
@connect((state, props) => {
  return {
    ...props,
    recommended: state.practice.recommendation
  }
})
export default class CompleteTaskModal extends React.Component {
  render() {
    if (this.props.position === 'hidden') {
      return null;
    }
    const message = 'Výborně, úloha vyřešena!';
    if (this.props.position !== 'modal') {
      if (!this.props.open) {
        return null;
      }
      return (
        <div>
          <div>{message}</div>
          <div>
            <NextTaskButtonContainer />
          </div>
        </div>
      );
    };
    return (
      <Dialog
        title={message}
        actions={[<NextTaskButtonContainer />]}
        open={this.props.open}
        contentStyle={{ textAlign: 'center' }}
        actionsContainerStyle={{ textAlign: 'center' }}
      >
      </Dialog>
    );
  }
}

