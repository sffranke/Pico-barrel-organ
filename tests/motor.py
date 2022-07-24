from machine import Pin
import utime
 
m1 = Pin(3, Pin.OUT)
m2 = Pin(2, Pin.OUT)
 
enable_m = Pin(4, Pin.OUT)
 
enable_m(1)
 
while True:
    #forward direction
    m1(1)
    m2(0)
    utime.sleep(10)
    #stop position
    m1(0)
    m2(0)
    break    
    
