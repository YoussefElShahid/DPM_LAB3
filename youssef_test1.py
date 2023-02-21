from utils import sound
from utils.brick import TouchSensor, EV3UltrasonicSensor, wait_ready_sensors, reset_brick,Motor
from time import sleep

DELAY_SEC = 0.3  # seconds of delay between measurements
pitch_list =["G1","A4","G8","D5",'C7']
print("Program start.\nWaiting for sensors to turn on...")
TOUCH_SENSOR_FLUTE = TouchSensor(1)
TOUCH_SENSOR_DRUM = TouchSensor(4)
US_SENSOR = EV3UltrasonicSensor(2)
Motor = Motor("A")
wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.
print("Done waiting.")



try:
    while True:
        if TOUCH_SENSOR_DRUM.is_pressed():
            Motor.set_power(60)
            print ("Drum Touch Sensor pressed")
        #while not TOUCH_SENSOR_FLUTE.is_pressed():
            #pass
        value = US_SENSOR.get_value()
        if value >=255:
            raise BaseException
        if TOUCH_SENSOR_FLUTE.is_pressed():
            print ("FLute Touch Sensor pressed")
            while value is None:
                US_SENSOR.get_value()
            if (value < 255):
                print(value)
                sound.Sound(pitch=pitch_list[int(value//5)],duration=0.5,volume=100).play()
        sleep (DELAY_SEC)


except BaseException:
    print ("Done with the program")
    Motor.set_power(0)
    reset_brick()
    exit()
    
                
            
            
