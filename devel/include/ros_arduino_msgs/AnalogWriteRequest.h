// Generated by gencpp from file ros_arduino_msgs/AnalogWriteRequest.msg
// DO NOT EDIT!


#ifndef ROS_ARDUINO_MSGS_MESSAGE_ANALOGWRITEREQUEST_H
#define ROS_ARDUINO_MSGS_MESSAGE_ANALOGWRITEREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ros_arduino_msgs
{
template <class ContainerAllocator>
struct AnalogWriteRequest_
{
  typedef AnalogWriteRequest_<ContainerAllocator> Type;

  AnalogWriteRequest_()
    : pin(0)
    , value(0)  {
    }
  AnalogWriteRequest_(const ContainerAllocator& _alloc)
    : pin(0)
    , value(0)  {
  (void)_alloc;
    }



   typedef uint8_t _pin_type;
  _pin_type pin;

   typedef uint16_t _value_type;
  _value_type value;




  typedef boost::shared_ptr< ::ros_arduino_msgs::AnalogWriteRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ros_arduino_msgs::AnalogWriteRequest_<ContainerAllocator> const> ConstPtr;

}; // struct AnalogWriteRequest_

typedef ::ros_arduino_msgs::AnalogWriteRequest_<std::allocator<void> > AnalogWriteRequest;

typedef boost::shared_ptr< ::ros_arduino_msgs::AnalogWriteRequest > AnalogWriteRequestPtr;
typedef boost::shared_ptr< ::ros_arduino_msgs::AnalogWriteRequest const> AnalogWriteRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ros_arduino_msgs::AnalogWriteRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ros_arduino_msgs::AnalogWriteRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace ros_arduino_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'ros_arduino_msgs': ['/home/ly/catkin_ws/src/ros_arduino_bridge/ros_arduino_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::ros_arduino_msgs::AnalogWriteRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ros_arduino_msgs::AnalogWriteRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ros_arduino_msgs::AnalogWriteRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ros_arduino_msgs::AnalogWriteRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ros_arduino_msgs::AnalogWriteRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ros_arduino_msgs::AnalogWriteRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ros_arduino_msgs::AnalogWriteRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "8bdf3293d28cac28419ebc4ff41dad0d";
  }

  static const char* value(const ::ros_arduino_msgs::AnalogWriteRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x8bdf3293d28cac28ULL;
  static const uint64_t static_value2 = 0x419ebc4ff41dad0dULL;
};

template<class ContainerAllocator>
struct DataType< ::ros_arduino_msgs::AnalogWriteRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ros_arduino_msgs/AnalogWriteRequest";
  }

  static const char* value(const ::ros_arduino_msgs::AnalogWriteRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ros_arduino_msgs::AnalogWriteRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint8 pin\n\
uint16 value\n\
";
  }

  static const char* value(const ::ros_arduino_msgs::AnalogWriteRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ros_arduino_msgs::AnalogWriteRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.pin);
      stream.next(m.value);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct AnalogWriteRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ros_arduino_msgs::AnalogWriteRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ros_arduino_msgs::AnalogWriteRequest_<ContainerAllocator>& v)
  {
    s << indent << "pin: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.pin);
    s << indent << "value: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.value);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROS_ARDUINO_MSGS_MESSAGE_ANALOGWRITEREQUEST_H
