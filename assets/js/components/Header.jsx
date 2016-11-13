import React from 'react';
import reactCSS from 'reactcss'


export default class Header extends React.Component {
  render() {

    const styles = reactCSS({
      'default': {
        title: {
          color: 'white',
          fontSize: '3em',
          position: 'relative',
          left: '5%'
        },
        header: {
          background: '#00004d',
          position: 'absolute',
          top: '0px',
          right: '0px',
          left: '0px'
        }
      }
    })

    return (
      <div style={ styles.header }>
        <h1 style={ styles.title }>ROBOMISE</h1>
      </div>
    )
  }
}

