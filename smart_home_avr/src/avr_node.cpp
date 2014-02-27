#include "ros.h"
#include "smart_home_sensors/ReadSensorBit.h"
#include "smart_home_sensors/WriteSensorBit.h"
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

using smart_home_sensors::ReadSensorBit;
using smart_home_sensors::WriteSensorBit;

ros::NodeHandle nh;

static void setPin(const WriteSensorBit::Request &req, WriteSensorBit::Response &res)
{
    res.success = false;
    if(req.value)
        setpinport |= _BV(setpin);
    else
        setpinport &= ~_BV(setpin);
    res.success = true;
}

static void readPin(const ReadSensorBit::Request &req, ReadSensorBit::Response &res)
{
    res.value = false;    
    if(bit_is_set(readpinport, readpin))
        res.value = true;
    else
        res.value = false;
}

ros::ServiceServer<WriteSensorBit::Request, WriteSensorBit::Response> servSetPin("avr_setpin", &setPin);
ros::ServiceServer<ReadSensorBit::Request, ReadSensorBit::Response> servReadPin("avr_readpin", &readPin);
std_msgs::UInt8 hum;
ros::Publisher humPub("avr_humidity", &hum);
std_msgs::Float32 temp;
ros::Publisher tempPub("avr_temperature", &temp);

int main()
{
    //setpin as input
    setpinddr |= _BV(setpin);
    //readpin as output
    readpinddr &= ~_BV(readpin);

    uint32_t lasttime = 0UL;
    // Initialize ROS
    nh.initNode();
    
    nh.advertiseService(servSetPin);
    //nh.spinOnce();
    nh.advertiseService(servReadPin);

    nh.advertise(humPub);
    nh.advertise(tempPub);
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
