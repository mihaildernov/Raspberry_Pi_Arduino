import serial
import time


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
    ser.flush()

while True:
    ser.write(b"test\n")
    line = ser.readline().decode('utf-8').rstrip()
    print(line)
    time.sleep(1)
