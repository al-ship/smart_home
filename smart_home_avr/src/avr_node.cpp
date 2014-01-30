#include "ros.h"
#include "smart_home_avr/AvrSetPin.h"
#include "smart_home_avr/AvrReadPin.h"
#include "std_msgs/UInt8.h"
#include "std_msgs/Float32.h"
#include "std_msgs/Bool.h"
// Include C headers (ie, non C++ headers) in this block
extern "C"
{
    #include <util/delay.h>
    #include "DHT22.h"
    #include <avr/io.h>
}
#define setpinport PORTB
#define setpinddr  DDRB
#define setpin     PB5
#define readpinport PORTD
#define readpinddr  DDRD
#define readpin     PD3
// Needed for AVR to use virtual function
extern "C" void __cxa_pure_virtual(void);
void __cxa_pure_virtual(void) {}

using smart_home_avr::AvrSetPin;
using smart_home_avr::AvrReadPin;

ros::NodeHandle nh;

std_msgs::UInt8 hum;
ros::Publisher humPub("avr_humidity", &hum);
std_msgs::Float32 temp;
ros::Publisher tempPub("avr_temperature", &temp);

void setPin(const AvrSetPin::Request &req, AvrSetPin::Response &res)
{
    res.output = false;
    if(req.input)
        setpinport |= _BV(setpin);
    else
        setpinport &= ~_BV(setpin);
    res.output = true;
}

void readPin(const AvrReadPin::Request &req, AvrReadPin::Response &res)
{
    res.output = false;    
    if(bit_is_set(readpinport, readpin))
        res.output = true;
    else
        res.output = false;
}

ros::ServiceServer<AvrSetPin::Request, AvrSetPin::Response> servSetPin("avr_setpin", &setPin);
ros::ServiceServer<AvrReadPin::Request, AvrReadPin::Response> servReadPin("avr_readpin", &readPin);

int main()
{
    //setpin as input
    setpinddr |= _BV(setpin);
    //readpin as output
    readpinddr &= ~_BV(readpin);

    uint32_t lasttime = 0UL;
    // Initialize ROS
    nh.initNode();
    nh.advertise(humPub);
    nh.advertise(tempPub);
    nh.advertiseService(servSetPin);
    nh.advertiseService(servReadPin);
    while(1)
    {
        /// Send the message every 3 seconds
        if(avr_time_now() - lasttime > 3000)
        {
            readDHT22(&hum.data, &temp.data);
            
            humPub.publish(&hum);
            tempPub.publish(&temp);
            lasttime = avr_time_now();
        }
        nh.spinOnce();
    }
    return 0;
}
