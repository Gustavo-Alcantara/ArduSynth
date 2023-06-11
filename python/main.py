import serial

with serial.Serial("COM3") as ser:
    while True:
        notes = ser.readline()
        print(notes)