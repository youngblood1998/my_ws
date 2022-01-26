// Generated by gencpp from file easy_handeye_msgs/SelectTargetPoseRequest.msg
// DO NOT EDIT!


#ifndef EASY_HANDEYE_MSGS_MESSAGE_SELECTTARGETPOSEREQUEST_H
#define EASY_HANDEYE_MSGS_MESSAGE_SELECTTARGETPOSEREQUEST_H


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
struct SelectTargetPoseRequest_
{
  typedef SelectTargetPoseRequest_<ContainerAllocator> Type;

  SelectTargetPoseRequest_()
    : target_pose_index(0)  {
    }
  SelectTargetPoseRequest_(const ContainerAllocator& _alloc)
    : target_pose_index(0)  {
  (void)_alloc;
    }



   typedef int64_t _target_pose_index_type;
  _target_pose_index_type target_pose_index;





  typedef boost::shared_ptr< ::easy_handeye_msgs::SelectTargetPoseRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::easy_handeye_msgs::SelectTargetPoseRequest_<ContainerAllocator> const> ConstPtr;

}; // struct SelectTargetPoseRequest_

typedef ::easy_handeye_msgs::SelectTargetPoseRequest_<std::allocator<void> > SelectTargetPoseRequest;

typedef boost::shared_ptr< ::easy_handeye_msgs::SelectTargetPoseRequest > SelectTargetPoseRequestPtr;
typedef boost::shared_ptr< ::easy_handeye_msgs::SelectTargetPoseRequest const> SelectTargetPoseRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::easy_handeye_msgs::SelectTargetPoseRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::easy_handeye_msgs::SelectTargetPoseRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace easy_handeye_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'easy_handeye_msgs': ['/home/jay/my_ws/src/easy_handeye/easy_handeye_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::easy_handeye_msgs::SelectTargetPoseRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::easy_handeye_msgs::SelectTargetPoseRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::easy_handeye_msgs::SelectTargetPoseRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::easy_handeye_msgs::SelectTargetPoseRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::easy_handeye_msgs::SelectTargetPoseRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::easy_handeye_msgs::SelectTargetPoseRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::easy_handeye_msgs::SelectTargetPoseRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "2fc5759f103cd28837dc44dadf87b7f9";
  }

  static const char* value(const ::easy_handeye_msgs::SelectTargetPoseRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x2fc5759f103cd288ULL;
  static const uint64_t static_value2 = 0x37dc44dadf87b7f9ULL;
};

template<class ContainerAllocator>
struct DataType< ::easy_handeye_msgs::SelectTargetPoseRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "easy_handeye_msgs/SelectTargetPoseRequest";
  }

  static const char* value(const ::easy_handeye_msgs::SelectTargetPoseRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::easy_handeye_msgs::SelectTargetPoseRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int64 target_pose_index\n\
";
  }

  static const char* value(const ::easy_handeye_msgs::SelectTargetPoseRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::easy_handeye_msgs::SelectTargetPoseRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.target_pose_index);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SelectTargetPoseRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::easy_handeye_msgs::SelectTargetPoseRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::easy_handeye_msgs::SelectTargetPoseRequest_<ContainerAllocator>& v)
  {
    s << indent << "target_pose_index: ";
    Printer<int64_t>::stream(s, indent + "  ", v.target_pose_index);
  }
};

} // namespace message_operations
} // namespace ros

#endif // EASY_HANDEYE_MSGS_MESSAGE_SELECTTARGETPOSEREQUEST_H