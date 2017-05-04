import React from 'react';
import { connect } from 'react-redux';
import { setOpenMenu } from '../actions/menu';
import { getLevelInfo } from '../selectors/student';
import Header from '../components/Header';


@connect(state => ({
  levelInfo: getLevelInfo(state),
}), {
  setOpenMenu
})
class HeaderContainer extends React.Component {
  constructor(props) {
    super(props);
    this.openMenu = this.props.setOpenMenu.bind(this, true);
  }

  render(){
    return (
      <Header
        onMenuIconTouchTap={this.openMenu}
        levelInfo={this.props.levelInfo}
      />
  )}
}

export default HeaderContainer;
