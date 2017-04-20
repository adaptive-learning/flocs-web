import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import Home from '../components/Home';
import { setTaskById } from '../actions/taskEnvironment';


const propTypes = {
  recommendation: PropTypes.object,
  setTaskById: PropTypes.func,
};


@connect(store => ({
  recommendation: store.recommendation,  // TODO: remove if not needed
}), { setTaskById })
export default class HomeContainer extends React.Component {
  componentDidMount() {
    this.props.setTaskById('home-commands', 'beware-of-asteroid');
    this.props.setTaskById('home-program', 'turning-right');
  }

  render() {
    return (
      <Home recommendation={this.props.recommendation} />
    );
  }
}

HomeContainer.propTypes = propTypes;
