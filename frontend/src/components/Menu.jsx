import React from 'react';
import Drawer from 'material-ui/Drawer';
import MenuItem from 'material-ui/MenuItem';
import Divider from 'material-ui/Divider';

export default class Menu extends React.Component {
  constructor(props) {
    super(props);
    this.setOpen = this.props.setOpen.bind(this);
  }

  render() {
    return (
      <Drawer
        docked={false}
        open={this.props.open}
        onRequestChange={this.setOpen}
      >
        <MenuItem>Log in</MenuItem>
        <MenuItem>Sign up</MenuItem>
        <Divider />
        <MenuItem>Home</MenuItem>
        <MenuItem>Practice</MenuItem>
        <MenuItem>Tasks</MenuItem>
        <MenuItem>Task Editor</MenuItem>
      </Drawer>
    );
  }
}
