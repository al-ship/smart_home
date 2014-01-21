#include "ros.h"
#include "smart_home_avr/AvrHumidity.h"
#include "smart_home_avr/AvrTemperature.h"
// Include C headers (ie, non C++ headers) in this block
extern "C"
{
    #include <util/delay.h>
    #include "DHT22.h"
}

// Needed for AVR to use virtual function
extern "C" void __cxa_pure_virtual(void);
void __cxa_pure_virtual(void) {}

ros::NodeHandle nh;
using smart_home_avr::AvrHumidity;
using smart_home_avr::AvrTemperature;
//std_msgs::String str_msg;
//ros::Publisher chatter("chatter", &str_msg);

void getHumidity(const AvrHumidity::Request &req, AvrHumidity::Response &res)
{
    float dht_temp = 1;
    uint8_t hum = 1;
    readDHT22(&hum, &dht_temp);
    res.output = hum;    
//        DHT_ERROR_NONE
}

void getTemperature(const AvrTemperature::Request &req, AvrTemperature::Response &res)
{
    float dht_temp = 1;
    uint8_t hum = 1;
    readDHT22(&hum, &dht_temp);
    res.output = dht_temp;    
//        DHT_ERROR_NONE
}

ros::ServiceServer<AvrHumidity::Request, AvrHumidity::Response> servHum("avr_humidity", &getHumidity);
ros::ServiceServer<AvrTemperature::Request, AvrTemperature::Response> servTemp("avr_temperature", &getTemperature);

int main()
{
//    uint32_t lasttime = 0UL;
   
    // Initialize ROS
    nh.initNode();
    //nh.advertise(chatter);
    nh.advertiseService(servHum);
    nh.advertiseService(servTemp);
    while(1)
    {
        /*
        /// Send the message every second
        if(avr_time_now() - lasttime > 1000)
        {
            str_msg.data = hello;
            chatter.publish(&str_msg);
            lasttime = avr_time_now();
        }
        */
        nh.spinOnce();
    }
    return 0;
}
