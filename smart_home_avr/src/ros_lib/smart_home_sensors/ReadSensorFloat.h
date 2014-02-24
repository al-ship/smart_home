#ifndef _ROS_SERVICE_ReadSensorFloat_h
#define _ROS_SERVICE_ReadSensorFloat_h
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace smart_home_sensors
{

static const char READSENSORFLOAT[] = "smart_home_sensors/ReadSensorFloat";

  class ReadSensorFloatRequest : public ros::Msg
  {
    public:
      int32_t num;

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_num;
      u_num.real = this->num;
      *(outbuffer + offset + 0) = (u_num.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_num.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_num.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_num.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->num);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_num;
      u_num.base = 0;
      u_num.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_num.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_num.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_num.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->num = u_num.real;
      offset += sizeof(this->num);
     return offset;
    }

    const char * getType(){ return READSENSORFLOAT; };
    const char * getMD5(){ return "54b3c80efd6fae6e6ffff8a4b9facd69"; };

  };

  class ReadSensorFloatResponse : public ros::Msg
  {
    public:
      float value;

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_value;
      u_value.real = this->value;
      *(outbuffer + offset + 0) = (u_value.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_value.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_value.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_value.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->value);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_value;
      u_value.base = 0;
      u_value.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_value.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_value.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_value.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->value = u_value.real;
      offset += sizeof(this->value);
     return offset;
    }

    const char * getType(){ return READSENSORFLOAT; };
    const char * getMD5(){ return "0aca93dcf6d857f0e5a0dc6be1eaa9fb"; };

  };

  class ReadSensorFloat {
    public:
    typedef ReadSensorFloatRequest Request;
    typedef ReadSensorFloatResponse Response;
  };

}
#endif
