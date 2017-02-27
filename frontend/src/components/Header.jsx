import React from 'react';
import AppBar from 'material-ui/AppBar';
import logo from 'images/logo.png'

export default class Header extends React.Component {
  render() {
    const logoImg = (
      <img
        src={ logo }
        style={{
          height: '100%',
          padding: 14,
          boxSizing: 'border-box',
        }}
      />
    );
    return (
      <AppBar
        title={logoImg}
        iconClassNameRight="muidocs-icon-navigation-expand-more"
        style={{
          backgroundColor: 'darkblue',
          margin: 0,
        }}
        onLeftIconButtonTouchTap={this.props.onMenuIconTouchTap}
      />
    );
  }
}
