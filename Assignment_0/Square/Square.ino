
#include <Romi32U4.h>

Romi32U4Motors motors;
Romi32U4ButtonA buttonA;

void setup()
{
  // Wait for the user to press button A.
  buttonA.waitForButton();

  // Delay so that the robot does not move away while the user is
  // still touching it.
  delay(1000);
}

void loop()
{
  // Run left motor forward.
  ledYellow(1);
  for (int speed = 0; speed <= 100; speed++)
  {
    motors.setLeftSpeed(speed);
  }

  // Run right motor forward.
  ledRed(1);
  for (int speed = 0; speed <= 100; speed++)
  {
    motors.setRightSpeed(speed);
  }
  delay(1000);
   for (int speed = 100; speed >= 0; speed--)
  {
    motors.setRightSpeed(speed);
    motors.setLeftSpeed(speed);
    
  }
  delay(1000);

  ledRed(1);
  for (int speed = 0; speed <= 100; speed++)
  {
    motors.setRightSpeed(speed);
  }
  delay(1000);
}
