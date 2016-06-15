void setup() {
  // put your setup code here, to run once:
  //initilise serial input
  pinMode(05, OUTPUT); //red
  pinMode(06, OUTPUT); //green
  pinMode(07, OUTPUT); //blue
}

// the loop routine runs over and over again forever:
void loop() {
  random_RGB();
  delay(500);
}

void random_RGB(){
      analogWrite(05,random(0,255));
      analogWrite(06,random(0,255));
      analogWrite(07,random(0,255));
}

