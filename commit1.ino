#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN         9           
#define SS_PIN          10          
MFRC522 mfrc522(SS_PIN, RST_PIN);   

void setup() {
  Serial.begin(9600);        
  SPI.begin();               
  mfrc522.PCD_Init();        
  Serial.println(F("TO WRITE DATA SCAN THE NFC TAG"));
}

void loop() {

  MFRC522::MIFARE_Key key;
  for (byte i = 0; i < 6; i++) key.keyByte[i] = 0xFF;

  byte buffer[34];
  byte block;
  MFRC522::StatusCode status;
  byte len;

  Serial.setTimeout(20000L) ;    
  // Ask personal data: SRN
  Serial.println(F("Enter the student SRN and end it with #"));
  len = Serial.readBytesUntil('#', (char *) buffer, 30) ; // read SRN from serial
  for (byte i = len; i < 30; i++) buffer[i] = ' ';     // pad with spaces


  status = mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, block, &key, &(mfrc522.uid));

  // Write block
  status = mfrc522.MIFARE_Write(block, buffer, 16);

  block = 2;
  status = mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, block, &key, &(mfrc522.uid));


  // Write block
  status = mfrc522.MIFARE_Write(block, &buffer[16], 16);


  Serial.println(" ");
  mfrc522.PICC_HaltA(); 
  mfrc522.PCD_StopCrypto1(); 
}
