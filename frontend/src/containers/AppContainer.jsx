import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import App from '../components/App';
import { fetchStaticData, startSession } from '../actions/api';
import { isLoaded } from '../selectors/app';


const propTypes = {
  loaded: PropTypes.bool.isRequired,
  children: PropTypes.node,
  fetchStaticData: PropTypes.func,
  startSession: PropTypes.func,
};


const defaultProps = {
  loaded: false,
};


@connect(state => ({
  loaded: isLoaded(state),
}), {
  fetchStaticData,
  startSession,
})
class AppContainer extends React.Component {
  componentDidMount() {
    this.props.fetchStaticData();
    this.props.startSession();
  }

  render() {
    if (!this.props.loaded) {
      return null;
    }
    return (
      <App>
        { this.props.children }
      </App>
    );
  }
}

AppContainer.propTypes = propTypes;
AppContainer.defaultProps = defaultProps;

export default AppContainer;
