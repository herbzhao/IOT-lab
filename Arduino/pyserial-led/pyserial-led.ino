
const int ledPin = 13; // the pin that the LED is attached to
//int Byte;      // a variable to read incoming serial data into

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
   int Byte = Serial.read();
   Serial.print(Byte);
//    Serial.print(Serial.read());
    // if it's a capital H (ASCII 72), turn on the LED:
    if (Byte == 'H') {
      digitalWrite(ledPin, HIGH);
    } 
    // if it's an L (ASCII 76) turn off the LED:
    if (Byte == 'L') {
      digitalWrite(ledPin, LOW);
    } 
  }
}
