import React from 'react';
import { Modal, Button } from 'react-bootstrap'
import { Link } from 'react-router'

import { connect } from 'react-redux'

// actions
import { solveTaskAndRecommend, nextTask } from '../actions/practiceActions'

@connect((store) => {
    return {
        recommended: store.practice.recommendation
    }
})
export default class CompleteTaskModal extends React.Component {

    componentDidMount() {
        this.props.dispatch(solveTaskAndRecommend())
    }

    render() {
        return (
            <div className="static-modal">
                <Modal.Dialog>
                    <Modal.Header>
                        <Modal.Title>Výborně!</Modal.Title>
                    </Modal.Header>

                    <Modal.Body>
                        Úloha vyřešena
                    </Modal.Body>

                    <Modal.Footer>
                        { this.props.recommended && (
                          <Link to={`/task/${this.props.recommended}`}>
                              <Button bsStyle="primary" > Jít na další </Button>
                          </Link>
                        )}
                    </Modal.Footer>

                </Modal.Dialog>
            </div>
        )
  }
}

