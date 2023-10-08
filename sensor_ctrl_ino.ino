#define Rpin A0
#define Lpin A1
#define Upin A2
#define Dpin A3
int LValue = 0;
int RValue = 0;
int UValue = 0;
int DValue = 0;
int ct = 0;

int thershold = 800;

void setup()
{
 Serial.begin(9600);
}

void loop()
{
 LValue = analogRead(Lpin);
 RValue = analogRead(Rpin);
 UValue = analogRead(Upin);
 DValue = analogRead(Dpin);
 

 if (LValue>thershold) {
 if (ct < 1){
 Serial.println("L");
 ct++;}
 
}
 else if (RValue>thershold) {
 if (ct < 1){
 Serial.println("R");
 ct++;}
}
 else if (UValue>thershold) {
 if (ct < 1){
 Serial.println("U");
 ct++;}
}
 else if (DValue>thershold) {
 if (ct < 1){
 Serial.println("D");
 ct++;}}
 
 else if (RValue>thershold && LValue>thershold) {
 if (ct < 1){
 Serial.println("ST");
 ct++;}
}
else {
 ct=0;
}
 
 delay(1);
}
