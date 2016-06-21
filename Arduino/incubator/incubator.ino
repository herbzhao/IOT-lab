//Setup onewire for temperatuer sensor
#include <OneWire.h>
#include <DallasTemperature.h>
// Data wire is plugged into pin 2 on the Arduino
#define ONE_WIRE_BUS 3

// Setup a oneWire instance to communicate with any OneWire devices 
OneWire oneWire(ONE_WIRE_BUS);
 
// Pass our oneWire reference to Dallas Temperature.
DallasTemperature sensors(&oneWire);



// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  // Start up the onewire library
  sensors.begin();

  //initilise serial input
  Serial.begin(9600);
  Serial.end();
  Serial.begin(9600);
  //this speed up the String input = Serial.readString();
  Serial.setTimeout(150);
}


// the loop routine runs over and over again forever:
void loop() {
  delay(200);
  float sensor_temp = temp_read();
  temp_control(sensor_temp, 37);
}



float temp_read(){
  // call sensors.requestTemperatures() to issue a global temperature
  // request to all devices on the bus
  sensors.requestTemperatures(); // Send the command to get temperatures
  float sensor_temp = sensors.getTempCByIndex(0);
  Serial.print("Temperature for Device 1 is: ");
  Serial.println(sensor_temp); // Why "byIndex"? 
    // You can have more than one IC on the same bus. 
    // 0 refers to the first IC on the wire
  return sensor_temp;
}

void temp_control(float sensor_temp, float set_temp){
  if (sensor_temp < set_temp) {
      pinMode(4, OUTPUT); 
      digitalWrite(4, HIGH);
      Serial.println("heating");
  }
  if (sensor_temp >= set_temp) {
      pinMode(4, OUTPUT);
      digitalWrite(4, LOW);
      Serial.println("cooling");
  }
}



