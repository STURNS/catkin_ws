// Auto-generated. Do not edit!

// (in-package arbotix_msgs.srv)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class SetupChannelRequest {
  constructor() {
    this.topic_name = '';
    this.pin = 0;
    this.value = 0;
    this.rate = 0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type SetupChannelRequest
    // Serialize message field [topic_name]
    bufferInfo = _serializer.string(obj.topic_name, bufferInfo);
    // Serialize message field [pin]
    bufferInfo = _serializer.uint8(obj.pin, bufferInfo);
    // Serialize message field [value]
    bufferInfo = _serializer.uint8(obj.value, bufferInfo);
    // Serialize message field [rate]
    bufferInfo = _serializer.uint8(obj.rate, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type SetupChannelRequest
    let tmp;
    let len;
    let data = new SetupChannelRequest();
    // Deserialize message field [topic_name]
    tmp = _deserializer.string(buffer);
    data.topic_name = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [pin]
    tmp = _deserializer.uint8(buffer);
    data.pin = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [value]
    tmp = _deserializer.uint8(buffer);
    data.value = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [rate]
    tmp = _deserializer.uint8(buffer);
    data.rate = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'arbotix_msgs/SetupChannelRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c65e58d8b3b4d406126f6dc829a6011f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    string topic_name
    uint8 pin
    uint8 value
    uint8 rate
    
    `;
  }

};

class SetupChannelResponse {
  constructor() {
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type SetupChannelResponse
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type SetupChannelResponse
    let tmp;
    let len;
    let data = new SetupChannelResponse();
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'arbotix_msgs/SetupChannelResponse';
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
  Request: SetupChannelRequest,
  Response: SetupChannelResponse
};
