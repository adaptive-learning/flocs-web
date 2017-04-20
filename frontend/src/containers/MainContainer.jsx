import React from 'react';
import { connect } from 'react-redux';
import Main from '../components/Main';
// import { getOrCreateStudent } from '../actions/student';
import { fetchStaticData, startSession } from '../actions/api';


@connect(state => ({
}), {
  fetchStaticData,
  startSession,
})
class MainContainer extends React.Component {
  constructor(props) {
    super(props);
    // this.setOpen = this.props.setOpenMenu.bind(this);
    console.log('constructor');
  }

  componentWillMount() {
    // console.log('will mount -> TODO: load student info');
    // this.props.getOrCreateStudent();
  }

  componentDidMount() {
    this.props.fetchStaticData();
    this.props.startSession();
    // TODO: load practice overview (with recommendation...)
  }

  render() {
    return (
      <Main>
        { this.props.children }
      </Main>
    );
  }
}

export default MainContainer;
