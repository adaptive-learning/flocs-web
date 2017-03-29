import React, { PropTypes } from 'react';
import AceEditor from 'react-ace';
import Toggle from 'material-ui/Toggle';
import { List, ListItem } from 'material-ui/List';
import Paper from 'material-ui/Paper';
import Divider from 'material-ui/Divider';
import IconDescription from 'material-ui/svg-icons/action/description';
import IconUpload from 'material-ui/svg-icons/content/unarchive';
import IconDownload from 'material-ui/svg-icons/content/move-to-inbox';

import 'brace/theme/solarized_light';
import 'brace/keybinding/vim';
import '../core/spaceWorldHighlighter';


export default function SettingEditor({
  spaceWorldText,
  isValid,
  onChange,
  taskId,
  onTaskIdChange,
  category,
  onCategoryChange,
  energy,
  onEnergyChange,
  actionsLimit,
  onActionsLimitChange,
  vimMode,
  onSwitchMode,
  onImport,
  onExport,
  blocklyEditorType,
  onEditorTypeChange,
}) {
  const annotations = [];
  if (!isValid) {
    annotations.push({ row: 0, column: 0, type: 'error', text: 'Invalid setting' });
  }

  return (
    <div style={{ overflowX: 'hidden' }}>
      <div style={{ display: 'table' }}>
        <div style={{ display: 'table-row' }}>
          <span style={{ display: 'table-cell' }}>
            taskId:
          </span>
          <input
            style={{ display: 'table-cell' }}
            type="text"
            value={taskId}
            onChange={onTaskIdChange}
          />
        </div>
        <div style={{ display: 'table-row' }}>
          <span style={{ display: 'table-cell' }}>
            category:
          </span>
          <input
            style={{ display: 'table-cell' }}
            type="text"
            value={category}
            onChange={onCategoryChange}
          />
        </div>
        <div style={{ display: 'table-row' }}>
          <span style={{ display: 'table-cell' }}>
            energy:
          </span>
          <input
            style={{ display: 'table-cell' }}
            type="text"
            value={energy || ''}
            onChange={onEnergyChange}
          />
        </div>
        <div style={{ display: 'table-row' }}>
          <span style={{ display: 'table-cell' }}>
            actionsLimit:
          </span>
          <input
            style={{ display: 'table-cell' }}
            type="text"
            value={actionsLimit || ''}
            onChange={onActionsLimitChange}
          />
        </div>
      </div>
      <AceEditor
        value={spaceWorldText}
        onChange={onChange}
        mode="spaceworld"
        theme="solarized_light"
        fontSize={18}
        keyboardHandler={vimMode ? 'vim' : null}
        annotations={annotations}
        editorProps={{ $blockScrolling: true }}
        width="100%"
        height="300px"
        style={{ display: 'block' }}
      />
      <div>
        <Paper style={{ width: 350, margin: 10 }}>
          <List>
            <ListItem
              primaryText="Vim SpaceWorld editor"
              rightToggle={<Toggle toggled={vimMode} onToggle={onSwitchMode} />}
            />
            <ListItem
              primaryText="Blockly editor"
              rightToggle={<Toggle toggled={blocklyEditorType} onToggle={onEditorTypeChange} />}
            />
          </List>
          <Divider />
          <List>
            <ListItem primaryText="Import task" onClick={onImport} leftIcon={<IconUpload />} />
            <ListItem primaryText="Export task" onClick={onExport} leftIcon={<IconDownload />} />
          </List>
          <Divider />
          <List>
            <ListItem
              href="https://github.com/adaptive-learning/flocs-visual-components/blob/master/docs/space-world.md"
              target="_blank"
              rel="noreferrer noopener"
              primaryText="Open SpaceWorld desription"
              leftIcon={<IconDescription />}
            />
          </List>
        </Paper>
      </div>
    </div>
  );
}

SettingEditor.propTypes = {
  spaceWorldText: PropTypes.string.isRequired,
  isValid: PropTypes.bool.isRequired,
  onChange: PropTypes.func.isRequired,
  taskId: PropTypes.string.isRequired,
  onTaskIdChange: PropTypes.func.isRequired,
  category: PropTypes.string.isRequired,
  onCategoryChange: PropTypes.func.isRequired,
  energy: PropTypes.number,
  onEnergyChange: PropTypes.func.isRequired,
  actionsLimit: PropTypes.number,
  onActionsLimitChange: PropTypes.func.isRequired,
  vimMode: PropTypes.bool.isRequired,
  onSwitchMode: PropTypes.func.isRequired,
  onImport: PropTypes.func.isRequired,
  onExport: PropTypes.func.isRequired,
  blocklyEditorType: PropTypes.bool.isRequired,
  onEditorTypeChange: PropTypes.func.isRequired,
};
