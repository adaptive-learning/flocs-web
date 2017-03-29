import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import muiThemeable from 'material-ui/styles/muiThemeable';
import HelpIcon from 'material-ui/svg-icons/action/help';
import IconButton from 'material-ui/IconButton';
import Joyride from 'react-joyride';
import 'react-joyride/lib/react-joyride-compiled.css';
import { translate } from '../localization';
import { showInstructions, seenInstruction } from '../actions/instructions';


// TODO: move to selectors
function getScheduledInstructions(state) {
  const scheduledInstructionIds = state.instructionLayer.scheduledInstructions;
  const instructions = scheduledInstructionIds.map(id => state.instructions[id]);
  return instructions;
}

const getProps = (state) => ({
  activeInstructionIndex: state.instructionLayer.activeInstructionIndex,
  scheduledInstructions: getScheduledInstructions(state),
});
const actionCreators = { showInstructions, seenInstruction };

@connect(getProps, actionCreators)
@muiThemeable()
class InstructionsContainer extends React.Component {
  static propTypes = {
    muiTheme: PropTypes.object,
    scheduledInstructions: PropTypes.array,
    activeInstructionIndex: PropTypes.number,
    showInstructions: PropTypes.func,
    seenInstruction: PropTypes.func,
  };

  constructor(props) {
    super(props);
    // this.showInstructions = props.showInstructions.bind(this);
    this.showInstructions = () => {
      if (this.props.activeInstructionIndex == null) {
        this.props.showInstructions();
      }
    };
    this.seenInstruction = props.seenInstruction.bind(this);
    this.handleJoyrideChange = this.handleJoyrideChange.bind(this);
    this.setInstructions(props.scheduledInstructions);
  }

  componentWillReceiveProps(nextProps) {
    this.setInstructions(nextProps.scheduledInstructions);
  }

  componentDidUpdate(prevProps) {
    if (prevProps.activeInstructionIndex === null && this.props.activeInstructionIndex !== null) {
      this.joyride.reset(true);
    }
  }

  setInstructions(instructions) {
    this.steps = instructions.map(instruction => ({
      text: translate(`instruction.${instruction.instructionId}`),
      selector: instruction.selector,  // '.instructionable-spaceworld',
      position: instruction.position, // 'bottom-left',
      type: 'hover',
      style: {
        mainColor: this.props.muiTheme.palette.primary1Color,
        beacon: {
          // offsetX: 15, offsetY: -20,
          inner: this.props.muiTheme.palette.accent1Color,
          outer: this.props.muiTheme.palette.accent1Color,
        },
      },
    }));
  }

  handleJoyrideChange({ type, index }) {
    switch (type) {
      case 'step:after':
        this.seenInstruction(index);
      // no default
    }
  }

  render() {
    const blocklyTrashcanColor = '#576065';
    const active = this.props.activeInstructionIndex != null;
    return (
      <div>
        <Joyride
          ref={(ref) => { this.joyride = ref; }}
          steps={this.steps}
          type="continuous"
          run={active}
          autoStart={active}
          showBackButton={false}
          debug={false}
          holePadding={2}
          locale={{
            back: translate('Previous'),
            close: translate('I understand'),
            next: translate('I understand'),
            last: translate('I understand'),
            skip: 'Skip',
          }}
          callback={this.handleJoyrideChange}
        />
        <IconButton
          onClick={this.showInstructions}
          style={{
            position: 'fixed',
            bottom: 31,
            right: 110,
            zIndex: 100,
            width: 60,
            height: 60,
            padding: 0,
          }}
          iconStyle={{
            width: 60,
            height: 60,
          }}
        >
          <HelpIcon color={blocklyTrashcanColor} hoverColor="#fff" />
        </IconButton>
      </div>
    );
  }

}


export default InstructionsContainer;
