import React, { PropTypes } from 'react';
import { Line as ProgressBar } from 'rc-progress';

const propTypes = {
  level: PropTypes.number.isRequired,
  activeCredits: PropTypes.number.isRequired,
  maxCredits: PropTypes.number.isRequired,
  mini: PropTypes.bool,
};

const defaultProps = {
  mini: false,
};

export default class LevelBar extends React.Component {
  render() {
    const percent = 100 * this.props.activeCredits / this.props.maxCredits;
    return (
      <span>
        <span style={{ fontSize: 18 }}>
          L{ this.props.level }
        </span>
        <span
          style={{
            display: 'inline-block',
            minWidth: 50,
            marginLeft: 8,
            fontSize: 12,
            lineHeight: '9px',
            textAlign: 'center'
          }}
        >
          {this.props.activeCredits} / {this.props.maxCredits}
          <ProgressBar
            percent={percent}
            strokeWidth={8}
            strokeColor="#E3E3E3"
            trailColor="#F3F3F3"
          />
        </span>
      </span>
    );
  }
}

LevelBar.propTypes = propTypes;
LevelBar.defaultProps = defaultProps;
