// Generated by gencpp from file robotiq_ft_sensor/ft_sensor.msg
// DO NOT EDIT!


#ifndef ROBOTIQ_FT_SENSOR_MESSAGE_FT_SENSOR_H
#define ROBOTIQ_FT_SENSOR_MESSAGE_FT_SENSOR_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace robotiq_ft_sensor
{
template <class ContainerAllocator>
struct ft_sensor_
{
  typedef ft_sensor_<ContainerAllocator> Type;

  ft_sensor_()
    : Fx(0.0)
    , Fy(0.0)
    , Fz(0.0)
    , Mx(0.0)
    , My(0.0)
    , Mz(0.0)  {
    }
  ft_sensor_(const ContainerAllocator& _alloc)
    : Fx(0.0)
    , Fy(0.0)
    , Fz(0.0)
    , Mx(0.0)
    , My(0.0)
    , Mz(0.0)  {
  (void)_alloc;
    }



   typedef float _Fx_type;
  _Fx_type Fx;

   typedef float _Fy_type;
  _Fy_type Fy;

   typedef float _Fz_type;
  _Fz_type Fz;

   typedef float _Mx_type;
  _Mx_type Mx;

   typedef float _My_type;
  _My_type My;

   typedef float _Mz_type;
  _Mz_type Mz;





  typedef boost::shared_ptr< ::robotiq_ft_sensor::ft_sensor_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::robotiq_ft_sensor::ft_sensor_<ContainerAllocator> const> ConstPtr;

}; // struct ft_sensor_

typedef ::robotiq_ft_sensor::ft_sensor_<std::allocator<void> > ft_sensor;

typedef boost::shared_ptr< ::robotiq_ft_sensor::ft_sensor > ft_sensorPtr;
typedef boost::shared_ptr< ::robotiq_ft_sensor::ft_sensor const> ft_sensorConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::robotiq_ft_sensor::ft_sensor_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::robotiq_ft_sensor::ft_sensor_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace robotiq_ft_sensor

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'robotiq_ft_sensor': ['/home/jay/my_ws/src/robotiq/robotiq_ft_sensor/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::robotiq_ft_sensor::ft_sensor_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::robotiq_ft_sensor::ft_sensor_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robotiq_ft_sensor::ft_sensor_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robotiq_ft_sensor::ft_sensor_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robotiq_ft_sensor::ft_sensor_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robotiq_ft_sensor::ft_sensor_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::robotiq_ft_sensor::ft_sensor_<ContainerAllocator> >
{
  static const char* value()
  {
    return "060fd5fcbaefcff9daec9d5bb2d41714";
  }

  static const char* value(const ::robotiq_ft_sensor::ft_sensor_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x060fd5fcbaefcff9ULL;
  static const uint64_t static_value2 = 0xdaec9d5bb2d41714ULL;
};

template<class ContainerAllocator>
struct DataType< ::robotiq_ft_sensor::ft_sensor_<ContainerAllocator> >
{
  static const char* value()
  {
    return "robotiq_ft_sensor/ft_sensor";
  }

  static const char* value(const ::robotiq_ft_sensor::ft_sensor_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::robotiq_ft_sensor::ft_sensor_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 Fx\n\
float32 Fy\n\
float32 Fz\n\
float32 Mx\n\
float32 My\n\
float32 Mz\n\
";
  }

  static const char* value(const ::robotiq_ft_sensor::ft_sensor_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::robotiq_ft_sensor::ft_sensor_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.Fx);
      stream.next(m.Fy);
      stream.next(m.Fz);
      stream.next(m.Mx);
      stream.next(m.My);
      stream.next(m.Mz);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ft_sensor_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::robotiq_ft_sensor::ft_sensor_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::robotiq_ft_sensor::ft_sensor_<ContainerAllocator>& v)
  {
    s << indent << "Fx: ";
    Printer<float>::stream(s, indent + "  ", v.Fx);
    s << indent << "Fy: ";
    Printer<float>::stream(s, indent + "  ", v.Fy);
    s << indent << "Fz: ";
    Printer<float>::stream(s, indent + "  ", v.Fz);
    s << indent << "Mx: ";
    Printer<float>::stream(s, indent + "  ", v.Mx);
    s << indent << "My: ";
    Printer<float>::stream(s, indent + "  ", v.My);
    s << indent << "Mz: ";
    Printer<float>::stream(s, indent + "  ", v.Mz);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROBOTIQ_FT_SENSOR_MESSAGE_FT_SENSOR_H
