// Auto-generated. Do not edit!

// (in-package ros_arduino_msgs.srv)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class AnalogWriteRequest {
  constructor() {
    this.pin = 0;
    this.value = 0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type AnalogWriteRequest
    // Serialize message field [pin]
    bufferInfo = _serializer.uint8(obj.pin, bufferInfo);
    // Serialize message field [value]
    bufferInfo = _serializer.uint16(obj.value, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type AnalogWriteRequest
    let tmp;
    let len;
    let data = new AnalogWriteRequest();
    // Deserialize message field [pin]
    tmp = _deserializer.uint8(buffer);
    data.pin = tmp.data;
    buffer = tmp.buffer;
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
    return 'ros_arduino_msgs/AnalogWriteRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8bdf3293d28cac28419ebc4ff41dad0d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint8 pin
    uint16 value
    
    `;
  }

};

class AnalogWriteResponse {
  constructor() {
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type AnalogWriteResponse
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type AnalogWriteResponse
    let tmp;
    let len;
    let data = new AnalogWriteResponse();
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'ros_arduino_msgs/AnalogWriteResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    
    `;
  }

};

module.exports = {
  Request: AnalogWriteRequest,
  Response: AnalogWriteResponse
};
