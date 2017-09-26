#include <wiringPi.h>

//Physical pin 11, BCM pin 17, GPIO17 = wiringPi pin 0
#define LedPin 0

int main(void)
{
	if (wiringPiSetup() == -1) {
		printf("wiringPiSetup error!\n");
		return -1;
	}
	
	pinMode(LedPin,OUTPUT);
	
	//run forever... ok, until Ctrl+C
	while (1) {
		digitalwrite(LedPin, HIGH);
		printf("led on\n");
		delay(1000); //1 second
		digitalwrite(LedPin, LOW);
		printf("led off\n");
		delay(1000); //1 second
	}
	
	return 0;
}