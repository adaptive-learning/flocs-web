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
                    { this.props.children }
                </Row>
            </Grid>
        )
    }
}
