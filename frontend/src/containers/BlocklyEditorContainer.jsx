import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import BlocklyEditor from '../components/BlocklyEditor';
import { getRoboAst, getEditorSessionId, getActionsLimit, getToolbox } from '../selectors/taskEnvironment';
import { changeRoboAst } from '../actions/taskEnvironment';
import { expandBlocks } from '../core/toolbox';


class BlocklyEditorWrapper extends React.Component {
  constructor(props) {
    super(props);
    this.changeRoboAst = this.props.changeRoboAst.bind(this, this.props.taskEnvironmentId);
  }

  resize() {
    this.blocklyEditor.resize();
  }

  render() {
    return (
      <BlocklyEditor
        ref={ref => { this.blocklyEditor = ref; }}
        roboAst={this.props.roboAst}
        toolboxBlocks={expandBlocks(this.props.toolbox)}
        actionsLimit={this.props.actionsLimit}
        editorSessionId={this.props.editorSessionId}
        onChange={this.changeRoboAst}
      />
    );
  }
}

BlocklyEditorWrapper.propTypes = {
  taskEnvironmentId: PropTypes.string.isRequired,
  toolbox: PropTypes.array.isRequired,
  editorSessionId: PropTypes.number,
  roboAst: PropTypes.object.isRequired,
  actionsLimit: PropTypes.number,
  changeRoboAst: PropTypes.func.isRequired,
};

function mapStateToProps(state, props) {
  const { taskEnvironmentId } = props;
  const roboAst = getRoboAst(state, taskEnvironmentId);
  const editorSessionId = getEditorSessionId(state, taskEnvironmentId);
  const { limit: actionsLimit } = getActionsLimit(state, taskEnvironmentId);
  const toolbox = getToolbox(state, taskEnvironmentId);
  return { taskEnvironmentId, toolbox, roboAst, actionsLimit, editorSessionId };
}


const actionCreators = { changeRoboAst };
const BlocklyEditorContainer = connect(mapStateToProps,
                                       actionCreators,
                                       null,
                                       { withRef: true })(BlocklyEditorWrapper);
export default BlocklyEditorContainer;
