//Prep for potentiometer
#include <SPI.h>
#include <mcp4xxx.h>
using namespace icecave::arduino;
MCP4XXX* pot;
float set_voltage;



// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:

  //connect Potentiometer at chip select (SS) pin at 10
  pot = new MCP4XXX(10);
  //set to 0V at P0A
  pot->set(pot->max_value());

  //initilise serial input
  Serial.begin(9600);
  Serial.end();
  Serial.begin(9600);
  //this speed up the String input = Serial.readString();
  Serial.setTimeout(150);
}


// the loop routine runs over and over again forever:
void loop() {
  voltage_read(1);
  voltage_read(0);
  serial_command();
  delay(100);
}

void voltage_read(int pin){

  // read the input on analog pin 0:
  int sensorValue = analogRead(pin);
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float voltage = sensorValue * (5.0 / 1023.0);
  // print out the value you read:
  //print voltage line by line
  
  Serial.print("pin");
  Serial.print("A");
  Serial.print(pin);
  Serial.print(":  ");
  Serial.print(voltage);
  Serial.print("V \n \r");
}



//set pot to any number
void SetPot(){
  pot->set(set_voltage);
}

//Receive command from serial
void serial_command(){
  //read command from web interface
  String input = Serial.readString();
  String pre_command=input.substring(0,3); // first 3 letter
  
  //Control potentiometer: type pot+value (voltage)
  if (pre_command == "pot") {
    String pot_command = input.substring(3); //after 3 letters
    float set_voltage = 256-pot_command.toFloat()*256/5;
    SetPot();
  }
  
  //control any pins with "pin03on or pin03off"
  if (pre_command == "pin") {
    int pin_number = input.substring(3,5).toInt();
    String pin_switch = input.substring(5);
    
    if (pin_switch == "on") {
      pinMode(pin_number, OUTPUT);
      digitalWrite(pin_number, HIGH);
    }  
    if (pin_switch == "off") {
      pinMode(pin_number, OUTPUT);
      digitalWrite(pin_number, LOW);
    }
  }

  //analog pin control "ana07255"
  if (pre_command == "ana") {
    int pin_number = input.substring(3,5).toInt();
    int analog_value = input.substring(5).toInt();
      pinMode(pin_number, OUTPUT);
      analogWrite(pin_number,analog_value);
  }

    //analog pin control "RGB255255255"
  if (pre_command == "RGB") {
    int r_value = input.substring(3,6).toInt();
    int g_value = input.substring(6,9).toInt();
    int b_value = input.substring(9,12).toInt();
      pinMode(05, OUTPUT); //red
      analogWrite(05,r_value);
      pinMode(06, OUTPUT); //red
      analogWrite(06,g_value);
      pinMode(07, OUTPUT); //red
      analogWrite(07,b_value);
  }
}  


