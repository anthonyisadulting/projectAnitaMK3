import RPi.GPIO as GPIO
import time
import serial
import board




#output_pin1 = 40
fullStop1 = 64
fullStop2 = 192

# +/- 12
forwardSmall1 = 70 # 64 and up 
backwardSmall1 = 60 #64 and below

forwardSmall2 = 196
backwardSmall2 = 188

def movement(opCode):

    print("running testdrive")

    serial_port = serial.Serial(port = "/dev/ttyTHS1"
                                , baudrate = 19200
                                ,bytesize = serial.EIGHTBITS
                                ,parity = serial.PARITY_NONE
                                ,stopbits = serial.STOPBITS_ONE)

    #time.sleep(2)

    try:
        print("entering driving")

        #stop opCode
        if opCode == 0:
            #stop motor movement
            serial_port.write(fullStop1.to_bytes(1, 'big'))
            print("Stopping M1: " , fullStop1.to_bytes(1, 'big'))
            serial_port.write(fullStop2.to_bytes(1, 'big'))
            print("Stopping M2: " , fullStop2.to_bytes(1, 'big'))
        
        #forward opCode
        elif opCode == 1:
            #forward motor movement
            serial_port.write(forwardSmall1.to_bytes(1, 'big'))
            print("Forward M1: " , forwardSmall1.to_bytes(1, 'big'))
            serial_port.write(forwardSmall2.to_bytes(1, 'big'))
            print("Forward M2: " , forwardSmall2.to_bytes(1, 'big'))
        
        #backward opCode
        elif opCode == 2:
            #backward motor movement
            serial_port.write(backwardSmall1.to_bytes(1, 'big'))
            print("Backward M1: " , backwardSmall1.to_bytes(1, 'big'))
            serial_port.write(backwardSmall2.to_bytes(1, 'big'))
            print("Backward M2: " , backwardSmall2.to_bytes(1, 'big'))
        
        #left opCode
        elif opCode == 3:
            #turn left motor movement
            serial_port.write(forwardSmall1.to_bytes(1, 'big'))
            print("Forward M1: " , forwardSmall1.to_bytes(1, 'big'))
            serial_port.write(backwardSmall2.to_bytes(1, 'big'))
            print("Backward M2: " , forwardSmall2.to_bytes(1, 'big'))

        elif opCode == 4:
            #turn right motor movement
            serial_port.write(backwardSmall1.to_bytes(1, 'big'))
            print("Backward M1: " , forwardSmall1.to_bytes(1, 'big'))
            serial_port.write(forwardSmall2.to_bytes(1, 'big'))
            print("Forward M2: " , forwardSmall2.to_bytes(1, 'big'))

        elif opCode == 5:
            #change lights
            print("Light Mode in Dev")


    except(KeyboardInterrupt):
        print("Exit Program")

    finally:
        serial_port.close()
        pass
