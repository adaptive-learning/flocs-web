import React from 'react';
import { connect } from 'react-redux'
import Header from './Header'


export default class Main extends React.Component {
  render() {
    return (
      <div>
        <Header/>
        <div style={{ position: 'absolute', top: 81, bottom: 0, left: 0, right: 0 }}>
          { this.props.children }
        </div>
      </div>
    )
  }
}
