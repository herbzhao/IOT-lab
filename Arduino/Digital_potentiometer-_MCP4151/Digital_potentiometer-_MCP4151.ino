#include <SPI.h>
#include <mcp4xxx.h>

using namespace icecave::arduino;

MCP4XXX* pot;

float set_voltage;

void setup()
{
    // Construct an instance of the MCP4XXX to manage the digipot.
    // The first parameter is the pin number to use for 'chip select' (CS), if you are
    // using the default SPI CS pin for your Arduino you can simply omit this parameter.
    
    //connect chip select pin at 10
    //set to 0 position
    pot = new MCP4XXX(10);
    pot->set(pot->max_value());

    //prep serial
    Serial.flush();
    Serial.begin(9600);
    Serial.setTimeout(50);
}

void loop()
{
    //print voltage
    voltage_read();
    delay(50);
    //read command from web interface
    serial_command();
}

//set pot to any number
void SetPot(){
  pot->set(set_voltage);
}


//print A1 voltage in serial monitor
void voltage_read(){

  // read the input on analog pin 0:
  int sensorValue = analogRead(A1);
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float voltage = sensorValue * (5.0 / 1023.0);
  // print out the value you read:
  //print voltage line by line
  Serial.print(voltage);
  Serial.println("V");

}


//Receive command from serial
void serial_command(){
  //read command from web interface
  String input = Serial.readString();
//  String input_value;
  input.remove(0, 3);
  set_voltage = 256-input.toFloat()*256/5;
      if (set_voltage > -1 and set_voltage < 256) {
      SetPot();
      }
}


