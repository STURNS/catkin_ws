// Auto-generated. Do not edit!

// (in-package ros_arduino_msgs.srv)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class DigitalSetDirectionRequest {
  constructor() {
    this.pin = 0;
    this.direction = false;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type DigitalSetDirectionRequest
    // Serialize message field [pin]
    bufferInfo = _serializer.uint8(obj.pin, bufferInfo);
    // Serialize message field [direction]
    bufferInfo = _serializer.bool(obj.direction, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type DigitalSetDirectionRequest
    let tmp;
    let len;
    let data = new DigitalSetDirectionRequest();
    // Deserialize message field [pin]
    tmp = _deserializer.uint8(buffer);
    data.pin = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [direction]
    tmp = _deserializer.bool(buffer);
    data.direction = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'ros_arduino_msgs/DigitalSetDirectionRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b10eff5e5e7e4623e1ee840cec92b372';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint8 pin
    bool direction
    
    `;
  }

};

class DigitalSetDirectionResponse {
  constructor() {
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type DigitalSetDirectionResponse
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type DigitalSetDirectionResponse
    let tmp;
    let len;
    let data = new DigitalSetDirectionResponse();
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'ros_arduino_msgs/DigitalSetDirectionResponse';
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
  Request: DigitalSetDirectionRequest,
  Response: DigitalSetDirectionResponse
};
