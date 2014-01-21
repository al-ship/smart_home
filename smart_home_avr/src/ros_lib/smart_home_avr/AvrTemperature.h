#ifndef _ROS_SERVICE_AvrTemperature_h
#define _ROS_SERVICE_AvrTemperature_h
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace smart_home_avr
{

static const char AVRTEMPERATURE[] = "smart_home_avr/AvrTemperature";

  class AvrTemperatureRequest : public ros::Msg
  {
    public:
      float input;

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_input;
      u_input.real = this->input;
      *(outbuffer + offset + 0) = (u_input.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_input.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_input.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_input.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->input);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_input;
      u_input.base = 0;
      u_input.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_input.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_input.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_input.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->input = u_input.real;
      offset += sizeof(this->input);
     return offset;
    }

    const char * getType(){ return AVRTEMPERATURE; };
    const char * getMD5(){ return "79c3c282188d9b61edcde55d5577527e"; };

  };

  class AvrTemperatureResponse : public ros::Msg
  {
    public:
      float output;

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_output;
      u_output.real = this->output;
      *(outbuffer + offset + 0) = (u_output.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_output.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_output.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_output.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->output);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_output;
      u_output.base = 0;
      u_output.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_output.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_output.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_output.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->output = u_output.real;
      offset += sizeof(this->output);
     return offset;
    }

    const char * getType(){ return AVRTEMPERATURE; };
    const char * getMD5(){ return "dc04e8385a5c2f792e8299232db8e2eb"; };

  };

  class AvrTemperature {
    public:
    typedef AvrTemperatureRequest Request;
    typedef AvrTemperatureResponse Response;
  };

}
#endif
