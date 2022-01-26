// Generated by gencpp from file easy_handeye_msgs/SetAlgorithmRequest.msg
// DO NOT EDIT!


#ifndef EASY_HANDEYE_MSGS_MESSAGE_SETALGORITHMREQUEST_H
#define EASY_HANDEYE_MSGS_MESSAGE_SETALGORITHMREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace easy_handeye_msgs
{
template <class ContainerAllocator>
struct SetAlgorithmRequest_
{
  typedef SetAlgorithmRequest_<ContainerAllocator> Type;

  SetAlgorithmRequest_()
    : new_algorithm()  {
    }
  SetAlgorithmRequest_(const ContainerAllocator& _alloc)
    : new_algorithm(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _new_algorithm_type;
  _new_algorithm_type new_algorithm;





  typedef boost::shared_ptr< ::easy_handeye_msgs::SetAlgorithmRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::easy_handeye_msgs::SetAlgorithmRequest_<ContainerAllocator> const> ConstPtr;

}; // struct SetAlgorithmRequest_

typedef ::easy_handeye_msgs::SetAlgorithmRequest_<std::allocator<void> > SetAlgorithmRequest;

typedef boost::shared_ptr< ::easy_handeye_msgs::SetAlgorithmRequest > SetAlgorithmRequestPtr;
typedef boost::shared_ptr< ::easy_handeye_msgs::SetAlgorithmRequest const> SetAlgorithmRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::easy_handeye_msgs::SetAlgorithmRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::easy_handeye_msgs::SetAlgorithmRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace easy_handeye_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'easy_handeye_msgs': ['/home/jay/my_ws/src/easy_handeye/easy_handeye_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::easy_handeye_msgs::SetAlgorithmRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::easy_handeye_msgs::SetAlgorithmRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::easy_handeye_msgs::SetAlgorithmRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::easy_handeye_msgs::SetAlgorithmRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::easy_handeye_msgs::SetAlgorithmRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::easy_handeye_msgs::SetAlgorithmRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::easy_handeye_msgs::SetAlgorithmRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bcf2c7015a5a5f87cc2ad71d611e1d20";
  }

  static const char* value(const ::easy_handeye_msgs::SetAlgorithmRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xbcf2c7015a5a5f87ULL;
  static const uint64_t static_value2 = 0xcc2ad71d611e1d20ULL;
};

template<class ContainerAllocator>
struct DataType< ::easy_handeye_msgs::SetAlgorithmRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "easy_handeye_msgs/SetAlgorithmRequest";
  }

  static const char* value(const ::easy_handeye_msgs::SetAlgorithmRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::easy_handeye_msgs::SetAlgorithmRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string new_algorithm\n\
";
  }

  static const char* value(const ::easy_handeye_msgs::SetAlgorithmRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::easy_handeye_msgs::SetAlgorithmRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.new_algorithm);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SetAlgorithmRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::easy_handeye_msgs::SetAlgorithmRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::easy_handeye_msgs::SetAlgorithmRequest_<ContainerAllocator>& v)
  {
    s << indent << "new_algorithm: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.new_algorithm);
  }
};

} // namespace message_operations
} // namespace ros

#endif // EASY_HANDEYE_MSGS_MESSAGE_SETALGORITHMREQUEST_H
