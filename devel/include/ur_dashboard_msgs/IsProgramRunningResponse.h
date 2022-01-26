// Generated by gencpp from file ur_dashboard_msgs/IsProgramRunningResponse.msg
// DO NOT EDIT!


#ifndef UR_DASHBOARD_MSGS_MESSAGE_ISPROGRAMRUNNINGRESPONSE_H
#define UR_DASHBOARD_MSGS_MESSAGE_ISPROGRAMRUNNINGRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ur_dashboard_msgs
{
template <class ContainerAllocator>
struct IsProgramRunningResponse_
{
  typedef IsProgramRunningResponse_<ContainerAllocator> Type;

  IsProgramRunningResponse_()
    : answer()
    , program_running(false)
    , success(false)  {
    }
  IsProgramRunningResponse_(const ContainerAllocator& _alloc)
    : answer(_alloc)
    , program_running(false)
    , success(false)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _answer_type;
  _answer_type answer;

   typedef uint8_t _program_running_type;
  _program_running_type program_running;

   typedef uint8_t _success_type;
  _success_type success;





  typedef boost::shared_ptr< ::ur_dashboard_msgs::IsProgramRunningResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ur_dashboard_msgs::IsProgramRunningResponse_<ContainerAllocator> const> ConstPtr;

}; // struct IsProgramRunningResponse_

typedef ::ur_dashboard_msgs::IsProgramRunningResponse_<std::allocator<void> > IsProgramRunningResponse;

typedef boost::shared_ptr< ::ur_dashboard_msgs::IsProgramRunningResponse > IsProgramRunningResponsePtr;
typedef boost::shared_ptr< ::ur_dashboard_msgs::IsProgramRunningResponse const> IsProgramRunningResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ur_dashboard_msgs::IsProgramRunningResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ur_dashboard_msgs::IsProgramRunningResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace ur_dashboard_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'ur_dashboard_msgs': ['/home/jay/my_ws/src/Universal_Robots_ROS_Driver/ur_dashboard_msgs/msg', '/home/jay/my_ws/devel/share/ur_dashboard_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::ur_dashboard_msgs::IsProgramRunningResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ur_dashboard_msgs::IsProgramRunningResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ur_dashboard_msgs::IsProgramRunningResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ur_dashboard_msgs::IsProgramRunningResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ur_dashboard_msgs::IsProgramRunningResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ur_dashboard_msgs::IsProgramRunningResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ur_dashboard_msgs::IsProgramRunningResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "290f0cb02c3a44353957f0a92f954209";
  }

  static const char* value(const ::ur_dashboard_msgs::IsProgramRunningResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x290f0cb02c3a4435ULL;
  static const uint64_t static_value2 = 0x3957f0a92f954209ULL;
};

template<class ContainerAllocator>
struct DataType< ::ur_dashboard_msgs::IsProgramRunningResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ur_dashboard_msgs/IsProgramRunningResponse";
  }

  static const char* value(const ::ur_dashboard_msgs::IsProgramRunningResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ur_dashboard_msgs::IsProgramRunningResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string answer\n\
bool program_running\n\
bool success\n\
\n\
";
  }

  static const char* value(const ::ur_dashboard_msgs::IsProgramRunningResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ur_dashboard_msgs::IsProgramRunningResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.answer);
      stream.next(m.program_running);
      stream.next(m.success);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct IsProgramRunningResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ur_dashboard_msgs::IsProgramRunningResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ur_dashboard_msgs::IsProgramRunningResponse_<ContainerAllocator>& v)
  {
    s << indent << "answer: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.answer);
    s << indent << "program_running: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.program_running);
    s << indent << "success: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.success);
  }
};

} // namespace message_operations
} // namespace ros

#endif // UR_DASHBOARD_MSGS_MESSAGE_ISPROGRAMRUNNINGRESPONSE_H
