// Auto-generated. Do not edit!

// (in-package arbotix_msgs.msg)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class Digital {
  constructor() {
    this.header = new std_msgs.msg.Header();
    this.value = 0;
    this.direction = 0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type Digital
    // Serialize message field [header]
    bufferInfo = std_msgs.msg.Header.serialize(obj.header, bufferInfo);
    // Serialize message field [value]
    bufferInfo = _serializer.uint8(obj.value, bufferInfo);
    // Serialize message field [direction]
    bufferInfo = _serializer.uint8(obj.direction, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type Digital
    let tmp;
    let len;
    let data = new Digital();
    // Deserialize message field [header]
    tmp = std_msgs.msg.Header.deserialize(buffer);
    data.header = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [value]
    tmp = _deserializer.uint8(buffer);
    data.value = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [direction]
    tmp = _deserializer.uint8(buffer);
    data.direction = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a message object
    return 'arbotix_msgs/Digital';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '84d79480c76268c7cdf109dc588e00c4';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Reading or command to a single digital IO pin.
    Header header
    
    # value of pin
    uint8 LOW=0
    uint8 HIGH=255
    
    uint8 value
    
    # direction of pin
    uint8 INPUT=0
    uint8 OUTPUT=255
    
    uint8 direction
    
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    # 0: no frame
    # 1: global frame
    string frame_id
    
    `;
  }

};

// Constants for message
Digital.Constants = {
  LOW: 0,
  HIGH: 255,
  INPUT: 0,
  OUTPUT: 255,
}

module.exports = Digital;
