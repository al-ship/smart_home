#ifndef _ROS_smart_home_core_Notification_h
#define _ROS_smart_home_core_Notification_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace smart_home_core
{

  class Notification : public ros::Msg
  {
    public:
      char * id;
      char * text;
      uint8_t level;
      char * destination;
      char * recipient;
      uint8_t data_length;
      uint8_t st_data;
      uint8_t * data;

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      uint32_t * length_id = (uint32_t *)(outbuffer + offset);
      *length_id = strlen( (const char*) this->id);
      offset += 4;
      memcpy(outbuffer + offset, this->id, *length_id);
      offset += *length_id;
      uint32_t * length_text = (uint32_t *)(outbuffer + offset);
      *length_text = strlen( (const char*) this->text);
      offset += 4;
      memcpy(outbuffer + offset, this->text, *length_text);
      offset += *length_text;
      *(outbuffer + offset + 0) = (this->level >> (8 * 0)) & 0xFF;
      offset += sizeof(this->level);
      uint32_t * length_destination = (uint32_t *)(outbuffer + offset);
      *length_destination = strlen( (const char*) this->destination);
      offset += 4;
      memcpy(outbuffer + offset, this->destination, *length_destination);
      offset += *length_destination;
      uint32_t * length_recipient = (uint32_t *)(outbuffer + offset);
      *length_recipient = strlen( (const char*) this->recipient);
      offset += 4;
      memcpy(outbuffer + offset, this->recipient, *length_recipient);
      offset += *length_recipient;
      *(outbuffer + offset++) = data_length;
      *(outbuffer + offset++) = 0;
      *(outbuffer + offset++) = 0;
      *(outbuffer + offset++) = 0;
      for( uint8_t i = 0; i < data_length; i++){
      *(outbuffer + offset + 0) = (this->data[i] >> (8 * 0)) & 0xFF;
      offset += sizeof(this->data[i]);
      }
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      uint32_t length_id = *(uint32_t *)(inbuffer + offset);
      offset += 4;
      for(unsigned int k= offset; k< offset+length_id; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_id-1]=0;
      this->id = (char *)(inbuffer + offset-1);
      offset += length_id;
      uint32_t length_text = *(uint32_t *)(inbuffer + offset);
      offset += 4;
      for(unsigned int k= offset; k< offset+length_text; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_text-1]=0;
      this->text = (char *)(inbuffer + offset-1);
      offset += length_text;
      this->level =  ((uint8_t) (*(inbuffer + offset)));
      offset += sizeof(this->level);
      uint32_t length_destination = *(uint32_t *)(inbuffer + offset);
      offset += 4;
      for(unsigned int k= offset; k< offset+length_destination; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_destination-1]=0;
      this->destination = (char *)(inbuffer + offset-1);
      offset += length_destination;
      uint32_t length_recipient = *(uint32_t *)(inbuffer + offset);
      offset += 4;
      for(unsigned int k= offset; k< offset+length_recipient; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_recipient-1]=0;
      this->recipient = (char *)(inbuffer + offset-1);
      offset += length_recipient;
      uint8_t data_lengthT = *(inbuffer + offset++);
      if(data_lengthT > data_length)
        this->data = (uint8_t*)realloc(this->data, data_lengthT * sizeof(uint8_t));
      offset += 3;
      data_length = data_lengthT;
      for( uint8_t i = 0; i < data_length; i++){
      this->st_data =  ((uint8_t) (*(inbuffer + offset)));
      offset += sizeof(this->st_data);
        memcpy( &(this->data[i]), &(this->st_data), sizeof(uint8_t));
      }
     return offset;
    }

    const char * getType(){ return "smart_home_core/Notification"; };
    const char * getMD5(){ return "e04c81259b029d9a296d083566105023"; };

  };

}
#endif