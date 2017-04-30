import React from 'react';
import Dialog from 'material-ui/Dialog';
import NextTaskButtonContainer from '../containers/NextTaskButtonContainer';


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
    }
    return (
      <Dialog
        title={message}
        actions={[<NextTaskButtonContainer />]}
        open={this.props.open}
        onRequestClose={this.props.handleClose}
        contentStyle={{ textAlign: 'center' }}
        actionsContainerStyle={{ textAlign: 'center' }}
      >
      </Dialog>
    );
  }
}
