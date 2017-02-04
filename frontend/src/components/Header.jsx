import React from 'react';
import { Navbar } from 'react-bootstrap'
import logo from 'images/logo.png'

const style = {backgroundColor: 'darkblue', margin: 0};

export default class Header extends React.Component {
  render() {
      return (
          <Navbar style={style}>
              <Navbar.Header>
                      <a href="#"><img src={ logo }/></a>
              </Navbar.Header>
          </Navbar>
      )
  }
}

