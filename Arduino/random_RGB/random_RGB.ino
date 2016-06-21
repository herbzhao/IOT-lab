void setup() {
  // put your setup code here, to run once:
  //initilise serial input
  pinMode(05, OUTPUT); //red
  pinMode(06, OUTPUT); //green
  pinMode(07, OUTPUT); //blue
   //jump between each change

    //initilise serial input
  Serial.begin(9600);
  Serial.end();
  Serial.begin(9600);
  //this speed up the String input = Serial.readString();
  Serial.setTimeout(150);
}

// the loop routine runs over and over again forever:
void loop() {
  //initialise value
  int r_value_ori = random(255);
  int g_value_ori = random(255);
  int b_value_ori = random(255);
  
  while (true) { 
    //settings for fading
    int gap = 10;
    int timer = 500;
    
    randomSeed(analogRead(5));
    
    //generate new value
    int r_value = random(255);
    int g_value = random(255);
    int b_value = random(255);

    int r_increment = ( r_value  - r_value_ori -  (r_value - r_value_ori) % gap ) / gap;
    int g_increment = ( g_value  - g_value_ori -  (g_value - g_value_ori) % gap ) / gap;
    int b_increment = ( b_value  - b_value_ori -  (b_value - b_value_ori) % gap ) / gap;

    //gradual change
    int i = 0;
    while (i< gap)
    {
      set_RGB(r_value_ori, g_value_ori, b_value_ori);
      Serial.println("r:");
      Serial.println(r_value_ori);
      Serial.println(g_value_ori);
      Serial.println(b_value_ori);
      r_value_ori= r_value_ori + r_increment;
      i = i+1;
      delay(timer);
    }
     i = 0;
        while (i< gap)
    {
      set_RGB(r_value_ori, g_value_ori, b_value_ori);
      Serial.println("g:");
      Serial.println(r_value_ori);
      Serial.println(g_value_ori);
      Serial.println(b_value_ori);
      g_value_ori= g_value_ori + g_increment;
      i = i+1;
      delay(timer);
    }
    
     i = 0;
        while (i< gap)
    {
      set_RGB(r_value_ori, g_value_ori, b_value_ori);
      Serial.println("b:");
      Serial.println(r_value_ori);
      Serial.println(g_value_ori);
      Serial.println(b_value_ori);
      b_value_ori= b_value_ori + b_increment;
      i = i+1;
      delay(timer);
    }
  }
}



void set_RGB(int r_value, int g_value, int b_value){
  analogWrite(05, r_value);
  analogWrite(06, g_value);
  analogWrite(07, b_value);
}






