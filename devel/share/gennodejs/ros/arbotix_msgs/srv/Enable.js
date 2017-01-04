// Auto-generated. Do not edit!

// (in-package arbotix_msgs.srv)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class EnableRequest {
  constructor() {
    this.enable = false;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type EnableRequest
    // Serialize message field [enable]
    bufferInfo = _serializer.bool(obj.enable, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type EnableRequest
    let tmp;
    let len;
    let data = new EnableRequest();
    // Deserialize message field [enable]
    tmp = _deserializer.bool(buffer);
    data.enable = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'arbotix_msgs/EnableRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8c1211af706069c994c06e00eb59ac9e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool enable
    
    `;
  }

};

class EnableResponse {
  constructor() {
    this.state = false;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type EnableResponse
    // Serialize message field [state]
    bufferInfo = _serializer.bool(obj.state, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type EnableResponse
    let tmp;
    let len;
    let data = new EnableResponse();
    // Deserialize message field [state]
    tmp = _deserializer.bool(buffer);
    data.state = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'arbotix_msgs/EnableResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '001fde3cab9e313a150416ff09c08ee4';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool state
    
    
    `;
  }

};

module.exports = {
  Request: EnableRequest,
  Response: EnableResponse
};
