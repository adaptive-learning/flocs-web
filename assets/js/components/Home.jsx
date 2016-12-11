import React from 'react';
import { Grid, Row } from 'react-bootstrap'

import Header from './Header'
import Workspace from './Workspace'


export default class Main extends React.Component {
    render() {
        return (
            <Grid>
                <Row>
                    <Header/>
                </Row>
                <Row>
                    <Workspace />
                </Row>
            </Grid>
        )
    }
}