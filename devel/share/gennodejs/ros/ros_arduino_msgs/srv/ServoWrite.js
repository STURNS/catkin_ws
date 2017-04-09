// Auto-generated. Do not edit!

// (in-package ros_arduino_msgs.srv)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class ServoWriteRequest {
  constructor() {
    this.id = 0;
    this.value = 0.0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type ServoWriteRequest
    // Serialize message field [id]
    bufferInfo = _serializer.uint8(obj.id, bufferInfo);
    // Serialize message field [value]
    bufferInfo = _serializer.float32(obj.value, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type ServoWriteRequest
    let tmp;
    let len;
    let data = new ServoWriteRequest();
    // Deserialize message field [id]
    tmp = _deserializer.uint8(buffer);
    data.id = tmp.data;
    buffer = tmp.buffer;
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
    return 'ros_arduino_msgs/ServoWriteRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f90a4a27fdac2d3886d60d19d2b742b2';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint8 id
    float32 value
    
    `;
  }

};

class ServoWriteResponse {
  constructor() {
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type ServoWriteResponse
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type ServoWriteResponse
    let tmp;
    let len;
    let data = new ServoWriteResponse();
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'ros_arduino_msgs/ServoWriteResponse';
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
  Request: ServoWriteRequest,
  Response: ServoWriteResponse
};
