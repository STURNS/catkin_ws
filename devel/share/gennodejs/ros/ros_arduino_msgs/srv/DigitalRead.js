// Auto-generated. Do not edit!

// (in-package ros_arduino_msgs.srv)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class DigitalReadRequest {
  constructor() {
    this.pin = 0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type DigitalReadRequest
    // Serialize message field [pin]
    bufferInfo = _serializer.uint8(obj.pin, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type DigitalReadRequest
    let tmp;
    let len;
    let data = new DigitalReadRequest();
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
    return 'ros_arduino_msgs/DigitalReadRequest';
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

class DigitalReadResponse {
  constructor() {
    this.value = false;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type DigitalReadResponse
    // Serialize message field [value]
    bufferInfo = _serializer.bool(obj.value, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type DigitalReadResponse
    let tmp;
    let len;
    let data = new DigitalReadResponse();
    // Deserialize message field [value]
    tmp = _deserializer.bool(buffer);
    data.value = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'ros_arduino_msgs/DigitalReadResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e431d687bf4b2c65fbd94b12ae0cb5d9';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool value
    
    
    `;
  }

};

module.exports = {
  Request: DigitalReadRequest,
  Response: DigitalReadResponse
};
