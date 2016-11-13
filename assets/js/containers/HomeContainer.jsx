import { connect } from 'react-redux';
import Main from '../components/Home';


function mapStateToProps(state, props) {
  return {
  };
}

const MainContainer = connect(
  mapStateToProps,
)(Main);

export default MainContainer;
