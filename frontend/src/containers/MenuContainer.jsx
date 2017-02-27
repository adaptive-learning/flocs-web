import React from 'react';
import { connect } from 'react-redux';
import { setOpenMenu } from '../actions/menu';
import Menu from '../components/Menu';


@connect(state => ({
  open: state.menu.open
}), {
  setOpenMenu
})
class MenuContainer extends React.Component {
  constructor(props) {
    super(props);
    this.setOpen = this.props.setOpenMenu.bind(this);
  }

  render(){
    return (
      <Menu
        open={this.props.open}
        setOpen={this.setOpen}
      />
  )}
}

export default MenuContainer;
