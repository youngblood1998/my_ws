
"use strict";

let MasterboardDataMsg = require('./MasterboardDataMsg.js');
let RobotModeDataMsg = require('./RobotModeDataMsg.js');
let RobotStateRTMsg = require('./RobotStateRTMsg.js');
let ToolDataMsg = require('./ToolDataMsg.js');
let IOStates = require('./IOStates.js');
let Digital = require('./Digital.js');
let Analog = require('./Analog.js');

module.exports = {
  MasterboardDataMsg: MasterboardDataMsg,
  RobotModeDataMsg: RobotModeDataMsg,
  RobotStateRTMsg: RobotStateRTMsg,
  ToolDataMsg: ToolDataMsg,
  IOStates: IOStates,
  Digital: Digital,
  Analog: Analog,
};
