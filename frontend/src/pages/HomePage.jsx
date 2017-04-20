import React from 'react';
import { connect } from 'react-redux';


function getProps(state, props) {
  return {};
}

@connect(getProps, {})
export default class HomePage extends React.Component {
  render() {
    console.log('home page render')
    return (
      <div>
        home page
      </div>
    );
  }
}
