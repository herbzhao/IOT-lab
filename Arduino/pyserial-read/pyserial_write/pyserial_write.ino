void setup() {
  // initialize serial communication:
  Serial.begin(9600);
}

void loop() {

for (int i=0; i <= 500; i++){
      Serial.print(i);
      delay(1000);
   } 

   
}
