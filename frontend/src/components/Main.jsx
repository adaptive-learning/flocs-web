import React from 'react';
import { connect } from 'react-redux'
import HeaderContainer from '../containers/HeaderContainer';
import MenuContainer from '../containers/MenuContainer';


export default class Main extends React.Component {
  render() {
    return (
      <div>
        <HeaderContainer />
        <MenuContainer />
        <div style={{ position: 'absolute', top: 81, bottom: 0, left: 0, right: 0 }}>
          { this.props.children }
        </div>
      </div>
    )
  }
}
