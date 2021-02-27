#include <SPI.h>
#include <MFRC522.h>
#include <Keyboard.h>

#define RST_PIN         9           
#define SS_PIN          10          

MFRC522 mfrc522(SS_PIN, RST_PIN);   

void setup() {
  Serial.begin(9600);                                           
  SPI.begin();                                                  
  mfrc522.PCD_Init();                                              
  Serial.println(F("Scan your SRN:"));    
}

void loop() {

  
  MFRC522::MIFARE_Key key;
  for (byte i = 0; i < 6; i++) key.keyByte[i] = 0xFF;
  byte block = 4;
  byte len = 18;
  byte buffer1[18];
  MFRC522::StatusCode status;

 
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
    return;
  }

  if ( ! mfrc522.PICC_ReadCardSerial()) {
    return;
  }

  Serial.println(F("**Card Detected:**"));
  //mfrc522.PICC_DumpDetailsToSerial(&(mfrc522.uid)); //dump some details about the card 
  Serial.print(F("SRN: "));


  //------------------------------------------- GET SRN
  status = mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, 4, &key, &(mfrc522.uid)); 
  status = mfrc522.MIFARE_Read(block, buffer1, &len);

  //------------------------------------------- PRINT SRN
  for (uint8_t i = 0; i < 16; i++)
  {
      Serial.write(buffer1[i]);
  }

  Serial.println(F("\n**End Reading**\n"));

  delay(1000); //change value if you want to read cards faster

  mfrc522.PICC_HaltA();
  mfrc522.PCD_StopCrypto1();
}
