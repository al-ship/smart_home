#ifndef _ROS_SERVICE_AvrHumidity_h
#define _ROS_SERVICE_AvrHumidity_h
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace smart_home_avr
{

static const char AVRHUMIDITY[] = "smart_home_avr/AvrHumidity";

  class AvrHumidityRequest : public ros::Msg
  {
    public:
      int8_t input;

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        int8_t real;
        uint8_t base;
      } u_input;
      u_input.real = this->input;
      *(outbuffer + offset + 0) = (u_input.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->input);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        int8_t real;
        uint8_t base;
      } u_input;
      u_input.base = 0;
      u_input.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->input = u_input.real;
      offset += sizeof(this->input);
     return offset;
    }

    const char * getType(){ return AVRHUMIDITY; };
    const char * getMD5(){ return "1491ea77b99fb7b24d088237597e6386"; };

  };

  class AvrHumidityResponse : public ros::Msg
  {
    public:
      int8_t output;

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        int8_t real;
        uint8_t base;
      } u_output;
      u_output.real = this->output;
      *(outbuffer + offset + 0) = (u_output.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->output);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        int8_t real;
        uint8_t base;
      } u_output;
      u_output.base = 0;
      u_output.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->output = u_output.real;
      offset += sizeof(this->output);
     return offset;
    }

    const char * getType(){ return AVRHUMIDITY; };
    const char * getMD5(){ return "dac95e5e93a827d01a2335b08084600d"; };

  };

  class AvrHumidity {
    public:
    typedef AvrHumidityRequest Request;
    typedef AvrHumidityResponse Response;
  };

}
#endif
