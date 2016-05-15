//Prep for potentiometer
#include <SPI.h>
#include <mcp4xxx.h>
using namespace icecave::arduino;
MCP4XXX* pot;
float set_voltage;


//set name for GPIO pins
const int ledPin = 13; // the pin that the LED is attached to

void setup()
{
    //connect chip select (SS) pin at 10
    pot = new MCP4XXX(10);
    //set to 0V at P0A
    pot->set(pot->max_value());

    //prep serial
//    Serial.flush();
    Serial.begin(9600);
    Serial.end();
    Serial.begin(9600);
    Serial.setTimeout(100);

    //set GPIO pins
    pinMode(ledPin, OUTPUT); // the pin connect to on-board LED
    digitalWrite(ledPin, HIGH);
}

void loop()
{
    //print voltage
    //read command from web interface
    potentiometer_control();
    delay(50);
    voltage_read();
    digitalWrite(ledPin, HIGH);
    
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
//  Serial.print('*');
  Serial.println(voltage);
//  Serial.println("");
}


//Receive command from serial
void potentiometer_control(){
  
  //read command from web interface
  String input = Serial.readString();
  //Control potentiometer
  String pot_command = input;
  //take out command's first 2 as 
  String pot_command_pre = pot_command;
  pot_command_pre.remove(2); // only have first 2 
  pot_command.remove(0,2);  //have characters after pre

  //Control potentiometer: type set+value
  if (pot_command_pre == "go") {
    set_voltage = 256-pot_command.toFloat()*256/5;
    SetPot();
  }
}  


/*
//Receive command from serial
void GPIO_control(){
  String input = Serial.readString();
  String pin_command = Serial.readString();
  //read command from web interface
  // control any GPIO pins
      if (pin_command == "high") {
      digitalWrite(ledPin, HIGH);
    } 
            // if it's a high (ASCII 76) turn off the LED:
    if (pin_command == "low") {
      digitalWrite(ledPin, LOW);
    }  
}
*/



