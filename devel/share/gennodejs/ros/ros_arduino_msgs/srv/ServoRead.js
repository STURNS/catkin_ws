// Auto-generated. Do not edit!

// (in-package ros_arduino_msgs.srv)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class ServoReadRequest {
  constructor() {
    this.id = 0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type ServoReadRequest
    // Serialize message field [id]
    bufferInfo = _serializer.uint8(obj.id, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type ServoReadRequest
    let tmp;
    let len;
    let data = new ServoReadRequest();
    // Deserialize message field [id]
    tmp = _deserializer.uint8(buffer);
    data.id = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'ros_arduino_msgs/ServoReadRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '541b98e964705918fa8eb206b65347b3';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint8 id
    
    `;
  }

};

class ServoReadResponse {
  constructor() {
    this.value = 0.0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type ServoReadResponse
    // Serialize message field [value]
    bufferInfo = _serializer.float32(obj.value, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type ServoReadResponse
    let tmp;
    let len;
    let data = new ServoReadResponse();
    // Deserialize message field [value]
    tmp = _deserializer.float32(buffer);
    data.value = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'ros_arduino_msgs/ServoReadResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0aca93dcf6d857f0e5a0dc6be1eaa9fb';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 value
    
    
    `;
  }

};

module.exports = {
  Request: ServoReadRequest,
  Response: ServoReadResponse
};
