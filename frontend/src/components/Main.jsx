import React from 'react';
import { connect } from 'react-redux'
import { Grid, Row } from 'react-bootstrap'
import Header from './Header'


export default class Main extends React.Component {
    render() {
        return (
            <Grid fluid>
                <Row>
                    <Header/>
                </Row>
                <Row>
                  <div style={{ position: 'absolute', top: 81, bottom: 0, left: 0, right: 0 }}>
                    { this.props.children }
                  </div>
                </Row>
            </Grid>
        )
    }
}
