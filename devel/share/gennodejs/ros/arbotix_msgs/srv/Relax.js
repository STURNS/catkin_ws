// Auto-generated. Do not edit!

// (in-package arbotix_msgs.srv)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class RelaxRequest {
  constructor() {
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type RelaxRequest
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type RelaxRequest
    let tmp;
    let len;
    let data = new RelaxRequest();
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'arbotix_msgs/RelaxRequest';
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

class RelaxResponse {
  constructor() {
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type RelaxResponse
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type RelaxResponse
    let tmp;
    let len;
    let data = new RelaxResponse();
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'arbotix_msgs/RelaxResponse';
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
  Request: RelaxRequest,
  Response: RelaxResponse
};
