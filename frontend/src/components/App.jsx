import React, { PropTypes } from 'react';
import HeaderContainer from '../containers/HeaderContainer';
import MenuContainer from '../containers/MenuContainer';

const propTypes = {
  children: PropTypes.node,
};

export default class App extends React.Component {
  render() {
    return (
      <div
        style={{
          backgroundImage: 'url(/static/images/background-space.png)',
          backgroundSize: '500px auto',
          backgroundColor: '#111122',
          paddingBottom: 5,
        }}
      >
        <HeaderContainer />
        <MenuContainer />
        { this.props.children }
      </div>
    );
  }
}


App.propTypes = propTypes;
