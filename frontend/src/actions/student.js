import axios from 'axios';
import { flocsActionCreators } from 'flocs-visual-components';


export function getOrCreateStudent() {
  return ((dispatch) => {
    return axios.post('/api/practice/get_or_create_student')
      .then((response) => axios.get(response.data['student_url']))
      .then((response) => dispatch(flocsActionCreators.setStudent(response.data)))
  });
}
