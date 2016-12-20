webpackHotUpdate(0,{

/***/ 638:
/***/ function(module, exports, __webpack_require__) {

	'use strict';

	Object.defineProperty(exports, "__esModule", {
	    value: true
	});
	exports.default = undefined;

	var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

	var _dec, _class;

	// actions


	// flocs visual components


	var _react = __webpack_require__(78);

	var _react2 = _interopRequireDefault(_react);

	var _reactRedux = __webpack_require__(275);

	var _reactBootstrap = __webpack_require__(347);

	var _practiceActions = __webpack_require__(600);

	var _flocsVisualComponents = __webpack_require__(626);

	function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

	function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

	function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

	function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

	// set single task environment
	var taskEnvId = "single";

	var TaskEnvironment = (_dec = (0, _reactRedux.connect)(function (state, props) {
	    return {
	        taskId: props.routeParams.taskId
	    };
	}), _dec(_class = function (_React$Component) {
	    _inherits(TaskEnvironment, _React$Component);

	    function TaskEnvironment() {
	        _classCallCheck(this, TaskEnvironment);

	        return _possibleConstructorReturn(this, (TaskEnvironment.__proto__ || Object.getPrototypeOf(TaskEnvironment)).apply(this, arguments));
	    }

	    _createClass(TaskEnvironment, [{
	        key: 'componentWillMount',
	        value: function componentWillMount() {
	            // Start session
	            this.props.dispatch(_flocsVisualComponents.flocsActionCreators.createTaskEnvironment(taskEnvId));
	            if (typeof this.props.taskId === 'undefined') {
	                this.props.dispatch((0, _practiceActions.start)(taskEnvId));
	            } else {
	                this.props.dispatch((0, _practiceActions.getTaskForEnv)(taskEnvId, this.props.taskId));
	            }
	        }
	    }, {
	        key: 'componentWillReceiveProps',
	        value: function componentWillReceiveProps(props) {
	            props.dispatch((0, _practiceActions.getTaskForEnv)(taskEnvId, props.taskId));
	        }
	    }, {
	        key: 'render',
	        value: function render() {
	            return _react2.default.createElement(
	                'div',
	                null,
	                _react2.default.createElement(
	                    _reactBootstrap.Col,
	                    { xs: 6, md: 6 },
	                    _react2.default.createElement(_flocsVisualComponents.CodeEditorContainer, { taskEnvironmentId: taskEnvId })
	                ),
	                _react2.default.createElement(
	                    _reactBootstrap.Col,
	                    { xs: 6, md: 6 },
	                    _react2.default.createElement(_flocsVisualComponents.SpaceGameContainer, { taskEnvironmentId: taskEnvId })
	                ),
	                'ahoj'
	            );
	        }
	    }]);

	    return TaskEnvironment;
	}(_react2.default.Component)) || _class);
	exports.default = TaskEnvironment;
	;

	var _temp = function () {
	    if (typeof __REACT_HOT_LOADER__ === 'undefined') {
	        return;
	    }

	    __REACT_HOT_LOADER__.register(taskEnvId, 'taskEnvId', '/home/xmauritz/work/python/flocs-web/frontend/js/components/TaskEnvironment.jsx');

	    __REACT_HOT_LOADER__.register(TaskEnvironment, 'TaskEnvironment', '/home/xmauritz/work/python/flocs-web/frontend/js/components/TaskEnvironment.jsx');
	}();

	;

/***/ }

})