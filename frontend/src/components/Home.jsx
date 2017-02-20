import React from 'react';
import { connect } from 'react-redux'
import { Link } from 'react-router'
import Paper from 'material-ui/Paper';
import RaisedButton from 'material-ui/RaisedButton';
import Divider from 'material-ui/Divider';
import {Card, CardActions, CardHeader, CardMedia, CardTitle, CardText} from 'material-ui/Card';
import { recommend, getTaskForEnv } from '../actions/practiceActions'
import NextTaskButtonContainer from '../containers/NextTaskButtonContainer';
import PracticeContainer from '../containers/PracticeContainer';

@connect((store) => {
    return {
        recommended: store.practice.recommendation
    }
})
export default class Home extends React.Component {

  componentDidMount() {
    this.props.dispatch(getTaskForEnv('home', 'turning-right'));
    this.props.dispatch(recommend());
  }

  render() {
      if (this.props.recommended == undefined) {
          return null
      }
      return (
        <Paper style={paperStyle}>
          <div>
            <PracticeContainer
              taskEnvironmentId="home"
              containerStyle={{ position: 'relative', height: 320, border: '5px solid #999' }}
              taskCompletionDialogPosition="below"
            />
          </div>
          <Divider style={{ marginTop: 20, marginBottom: 20 }} />
          <Card>
            <CardTitle title="Prozkoumej vesmír a posbírej všechny diamanty!" />
          </Card>
          <Card>
            <CardTitle title="Nauč se ovládat vesmírnou loď pomocí počítačových programů" />
          </Card>
          <Card>
            <CardTitle title="Hra je poháněna umělou inteligencí, díky které se hra přizpůsobuje tvým dovednostem" />
          </Card>
          <Card>
            <CardTitle title="Aplikaci vyvíjí tým Adaptabilního učení na Fakultě informatiky Masarykovy Univerzity" />
          </Card>
          <Card>
            <CardText>
              <NextTaskButtonContainer />
            </CardText>
          </Card>
        </Paper>
      )
  }
}


const paperStyle = {
  maxWidth: 1000,
  margin: '20px auto',
  padding: 10,
  textAlign: 'center',
  display: 'block',
};


