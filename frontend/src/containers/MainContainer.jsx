import React from 'react';
import { connect } from 'react-redux';
import Main from '../components/Main';
import { getOrCreateStudent } from '../actions/student';


@connect(state => ({
}), {
  getOrCreateStudent,
})
class MainContainer extends React.Component {
  constructor(props) {
    super(props);
    // this.setOpen = this.props.setOpenMenu.bind(this);
    console.log('constructor');
  }

  componentWillMount() {
    console.log('will mount -> TODO: load student info');
    this.props.getOrCreateStudent();
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
