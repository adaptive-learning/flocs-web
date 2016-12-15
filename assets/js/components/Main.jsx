import React from 'react';
import { connect } from 'react-redux'
import { Grid, Row } from 'react-bootstrap'

import Header from './Header'
import CompleteTaskModal from '../components/CompleteTaskModal'

import { flocsSelector } from 'flocs-visual-components';


@connect((state) => {
    return {
        solved: state.practice.stage === "ATTEMPTED" ? flocsSelector.getGameState(state, "single").stage == "solved" : false
    };
})
export default class Main extends React.Component {
    render() {
        return (
            <Grid>
                <Row>
                    <Header/>
                </Row>
                <Row>
                    { this.props.children }

                    { this.props.solved ? (
                        <CompleteTaskModal />
                    ): (null)}
                </Row>
            </Grid>
        )
    }
}