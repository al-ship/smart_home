#ifndef _ROS_SERVICE_AvrReadPin_h
#define _ROS_SERVICE_AvrReadPin_h
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace smart_home_avr
{

static const char AVRREADPIN[] = "smart_home_avr/AvrReadPin";

  class AvrReadPinRequest : public ros::Msg
  {
    public:
      bool input;

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        bool real;
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
        bool real;
        uint8_t base;
      } u_input;
      u_input.base = 0;
      u_input.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->input = u_input.real;
      offset += sizeof(this->input);
     return offset;
    }

    const char * getType(){ return AVRREADPIN; };
    const char * getMD5(){ return "2b64ae4a7ed5de74b5f183194512b62f"; };

  };

  class AvrReadPinResponse : public ros::Msg
  {
    public:
      bool output;

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        bool real;
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
        bool real;
        uint8_t base;
      } u_output;
      u_output.base = 0;
      u_output.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->output = u_output.real;
      offset += sizeof(this->output);
     return offset;
    }

    const char * getType(){ return AVRREADPIN; };
    const char * getMD5(){ return "d5fa62db5c86ed745052c3b25d12f430"; };

  };

  class AvrReadPin {
    public:
    typedef AvrReadPinRequest Request;
    typedef AvrReadPinResponse Response;
  };

}
#endif
