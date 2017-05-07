import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import Home from '../components/Home';
import { setTaskById } from '../actions/taskEnvironment';
import { isSpaceWorldDemoSolved } from '../selectors/home';


const propTypes = {
  recommendation: PropTypes.object,
  setTaskById: PropTypes.func,
};


@connect(state => ({
  spaceWorldDemoSolved: isSpaceWorldDemoSolved(state),
}), { setTaskById })
export default class HomeContainer extends React.Component {
  componentDidMount() {
    this.props.setTaskById('home-commands', 'beware-of-asteroid');
    this.props.setTaskById('home-program', 'turning-right');
  }

  render() {
    return (
      <Home spaceWorldDemoSolved={this.props.spaceWorldDemoSolved} />
    );
  }
}

HomeContainer.propTypes = propTypes;
