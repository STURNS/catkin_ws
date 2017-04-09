// Auto-generated. Do not edit!

// (in-package ros_arduino_msgs.srv)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class AnalogReadRequest {
  constructor() {
    this.pin = 0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type AnalogReadRequest
    // Serialize message field [pin]
    bufferInfo = _serializer.uint8(obj.pin, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type AnalogReadRequest
    let tmp;
    let len;
    let data = new AnalogReadRequest();
    // Deserialize message field [pin]
    tmp = _deserializer.uint8(buffer);
    data.pin = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'ros_arduino_msgs/AnalogReadRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '41386d6ac585eedbab7b4d4f9192cbcc';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint8 pin
    
    `;
  }

};

class AnalogReadResponse {
  constructor() {
    this.value = 0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type AnalogReadResponse
    // Serialize message field [value]
    bufferInfo = _serializer.uint16(obj.value, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type AnalogReadResponse
    let tmp;
    let len;
    let data = new AnalogReadResponse();
    // Deserialize message field [value]
    tmp = _deserializer.uint16(buffer);
    data.value = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'ros_arduino_msgs/AnalogReadResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6e68bf91459258a84dab807f5c768df7';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint16 value
    
    
    `;
  }

};

module.exports = {
  Request: AnalogReadRequest,
  Response: AnalogReadResponse
};
