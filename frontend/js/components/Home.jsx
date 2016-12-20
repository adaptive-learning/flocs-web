import React from 'react';
import { Button } from 'react-bootstrap'
import { recommend } from '../actions/practiceActions'
import { connect } from 'react-redux'
import { Link } from 'react-router'


@connect((store) => {
    return {
        recommended: store.practice.recommendation
    }
})
export default class Home extends React.Component {

    componentDidMount() {
       this.props.dispatch(recommend())
    }

  render() {
      if (this.props.recommended == undefined) {
          return null
      }
      return (
              <Link to={`/task/${this.props.recommended}`}>
                  <Button bsStyle="primary"> Vyleťte do vesmíru! </Button>
              </Link>
      )
  }
}

