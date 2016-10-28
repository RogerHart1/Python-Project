void setup()
{
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{
  if(Serial.available() > 0) {
   String value = Serial.readString();
    Serial.print(value);
    if(value == "ON") {
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if(value == "OFF") {
      digitalWrite(LED_BUILTIN, LOW);
    }
    //Serial.print(value);
    //Serial.print("\n");
    
    //digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  //delay(1000);                       // wait for a second
  //digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
 //delay(1000);
   
  
  }
  
    
  }

