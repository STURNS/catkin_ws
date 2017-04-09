// Auto-generated. Do not edit!

// (in-package ros_arduino_msgs.srv)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class DigitalWriteRequest {
  constructor() {
    this.pin = 0;
    this.value = false;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type DigitalWriteRequest
    // Serialize message field [pin]
    bufferInfo = _serializer.uint8(obj.pin, bufferInfo);
    // Serialize message field [value]
    bufferInfo = _serializer.bool(obj.value, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type DigitalWriteRequest
    let tmp;
    let len;
    let data = new DigitalWriteRequest();
    // Deserialize message field [pin]
    tmp = _deserializer.uint8(buffer);
    data.pin = tmp.data;
    buffer = tmp.buffer;
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
    return 'ros_arduino_msgs/DigitalWriteRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '9965f904e6efea32066b0a4a77246056';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint8 pin
    bool value
    
    `;
  }

};

class DigitalWriteResponse {
  constructor() {
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type DigitalWriteResponse
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type DigitalWriteResponse
    let tmp;
    let len;
    let data = new DigitalWriteResponse();
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'ros_arduino_msgs/DigitalWriteResponse';
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
  Request: DigitalWriteRequest,
  Response: DigitalWriteResponse
};
