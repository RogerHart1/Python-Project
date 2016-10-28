void setup() {
  
from mosquitto import *
//from serial import *
//from random import *
//board = Serial("FULL DEVICE NAME",SPEED,timeout=2)
randomID = random()
client = Mosquitto("LightSubscriber" + str(randomID))
client.connect("10.212.61.136")

client.subscribe("/lights")

def messageReceived(broker, obj, msg):
    global client
    payload = msg.payload.decode()
    print("Message " + msg.topic + " containing: " + payload)
    
    
client.on_message = messageReceived
while.True: client.loop()

}

void loop() {
  // put your main code here, to run repeatedly:

}
