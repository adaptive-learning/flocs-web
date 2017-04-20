import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import App from '../components/App';
import { fetchStaticData, startSession } from '../actions/api';


const propTypes = {
  loading: PropTypes.bool.isRequired,
  children: PropTypes.node,
  fetchStaticData: PropTypes.func,
  startSession: PropTypes.func,
};


const defaultProps = {
  loading: true,
};


@connect(state => ({
  loading: state.app.loading,  // TODO: use a selector
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
    if (this.props.loading) {
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
