// Auto-generated. Do not edit!

// (in-package ros_arduino_msgs.msg)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------

class ArduinoConstants {
  constructor() {
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type ArduinoConstants
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type ArduinoConstants
    let tmp;
    let len;
    let data = new ArduinoConstants();
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a message object
    return 'ros_arduino_msgs/ArduinoConstants';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6ca092be59914d9e8dd11612f0a5c895';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Arduino-style constants
    uint8 LOW=0
    uint8 HIGH=1
    uint8 INPUT=0
    uint8 OUTPUT=1
    
    `;
  }

};

// Constants for message
ArduinoConstants.Constants = {
  LOW: 0,
  HIGH: 1,
  INPUT: 0,
  OUTPUT: 1,
}

module.exports = ArduinoConstants;
