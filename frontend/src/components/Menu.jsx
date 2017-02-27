import React from 'react';
import Drawer from 'material-ui/Drawer';
import MenuItem from 'material-ui/MenuItem';
import Divider from 'material-ui/Divider';
import { Link } from 'react-router';


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
        {/*
        <MenuItem>Log in</MenuItem>
        <MenuItem>Sign up</MenuItem>
        <Divider />
        */}
        <MenuItem
          containerElement={<Link to="/" />}
        >
          Home
        </MenuItem>
        {this.props.recommendedTask !== null &&
          <MenuItem
            containerElement={<Link to={this.props.recommendedTask.url} />}
          >
            Practice
          </MenuItem>
        }
        <MenuItem
          containerElement={<Link to="/tasks" />}
        >
          Tasks
        </MenuItem>
        <MenuItem
          containerElement={<Link to="/task-editor" />}
        >
          Task Editor
        </MenuItem>
      </Drawer>
    );
  }
}
