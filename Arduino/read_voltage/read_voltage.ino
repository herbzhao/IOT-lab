//Prep for potentiometer
#include <SPI.h>
#include <mcp4xxx.h>
using namespace icecave::arduino;
MCP4XXX* pot;
float set_voltage;



// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
//  Serial.flush();
  Serial.begin(9600);
  Serial.end();
  Serial.begin(9600);
  //this speed up the String input = Serial.readString();
  Serial.setTimeout(100);
}


// the loop routine runs over and over again forever:
void loop() {
  voltage_read();
  serial_command();
  delay(10);
}

void voltage_read(){

  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float voltage = sensorValue * (5.0 / 1023.0);
  // print out the value you read:

  //print voltage line by line
  Serial.println(voltage);
}


//set pot to any number
void SetPot(){
  pot->set(set_voltage);
}


//Receive command from serial
void serial_command(){
  //read command from web interface
  String input = Serial.readString();
  //Control potentiometer
  //take out command's first 2 as 

  String pot_command_pre=input.substring(0,3); // first 3 letter
  String pot_command = input.substring(3); //after 3 letters
  //Control potentiometer: type set+value
  
  if (pot_command_pre == "pot") {
    set_voltage = 256-pot_command.toFloat()*256/5;
    SetPot();
  }
  if (pot_command_pre == "pin") {
    int pin_number = input.substring(3,5).toInt();
    String pin_switch = input.substring(5,8);
    
    if (pin_switch == "on") {
      pinMode(pin_number, OUTPUT);
      digitalWrite(pin_number, HIGH);
    }  
    if (pin_switch == "off") {
      pinMode(pin_number, OUTPUT);
      digitalWrite(pin_number, LOW);
    }
  }
}  
