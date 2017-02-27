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
        <div
          style={{
            position: 'absolute',
            top: 64,  // TODO: unhardcode using app height in flocs-theme
            bottom: 0,
            left: 0,
            right: 0,
          }}
        >
          <div
            style={{
              position: 'absolute',
              width: '100%',
              backgroundImage: `url(/static/images/background-space.png)`,
              backgroundSize: '500px auto',
              backgroundColor: '#111122',
            }}
          >
            { this.props.children }
          </div>
        </div>
      </div>
    )
  }
}
