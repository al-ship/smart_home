#ifndef _ROS_SERVICE_Command_h
#define _ROS_SERVICE_Command_h
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace smart_home_core
{

static const char COMMAND[] = "smart_home_core/Command";

  class CommandRequest : public ros::Msg
  {
    public:
      char * command;

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      uint32_t * length_command = (uint32_t *)(outbuffer + offset);
      *length_command = strlen( (const char*) this->command);
      offset += 4;
      memcpy(outbuffer + offset, this->command, *length_command);
      offset += *length_command;
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      uint32_t length_command = *(uint32_t *)(inbuffer + offset);
      offset += 4;
      for(unsigned int k= offset; k< offset+length_command; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_command-1]=0;
      this->command = (char *)(inbuffer + offset-1);
      offset += length_command;
     return offset;
    }

    const char * getType(){ return COMMAND; };
    const char * getMD5(){ return "cba5e21e920a3a2b7b375cb65b64cdea"; };

  };

  class CommandResponse : public ros::Msg
  {
    public:
      char * response;

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      uint32_t * length_response = (uint32_t *)(outbuffer + offset);
      *length_response = strlen( (const char*) this->response);
      offset += 4;
      memcpy(outbuffer + offset, this->response, *length_response);
      offset += *length_response;
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      uint32_t length_response = *(uint32_t *)(inbuffer + offset);
      offset += 4;
      for(unsigned int k= offset; k< offset+length_response; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_response-1]=0;
      this->response = (char *)(inbuffer + offset-1);
      offset += length_response;
     return offset;
    }

    const char * getType(){ return COMMAND; };
    const char * getMD5(){ return "6de314e2dc76fbff2b6244a6ad70b68d"; };

  };

  class Command {
    public:
    typedef CommandRequest Request;
    typedef CommandResponse Response;
  };

}
#endif
