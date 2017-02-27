import React from 'react';
import AppBar from 'material-ui/AppBar';
import muiThemeable from 'material-ui/styles/muiThemeable';
import logo from 'images/logo.png'


@muiThemeable()
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
          backgroundColor: this.props.muiTheme.palette.primary1Color,
          margin: 0,
        }}
        onLeftIconButtonTouchTap={this.props.onMenuIconTouchTap}
      />
    );
  }
}
