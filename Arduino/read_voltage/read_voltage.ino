/*
  ReadAnalogVoltage
  Reads an analog input on pin 0, converts it to voltage, and prints the result to the serial monitor.
  Graphical representation is available using serial plotter (Tools > Serial Plotter menu)
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.
*/

const int ledPin = 13; // the pin that the LED is attached to

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
//  Serial.flush();
  Serial.begin(9600);
  Serial.end();
  Serial.begin(9600);
  //this speed up the String input = Serial.readString();
  Serial.setTimeout(100);
  pinMode(ledPin, OUTPUT);
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


void serial_command(){
  //read command from web interface
  String input = Serial.readString();
  //input high , turn on LED
    if (input == "high") {
      digitalWrite(ledPin, HIGH);
    } 
            // if it's a high (ASCII 76) turn off the LED:
    if (input == "low") {
      digitalWrite(ledPin, LOW);
    }  
}
