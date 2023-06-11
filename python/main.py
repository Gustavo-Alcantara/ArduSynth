import serial

with serial.Serial("COM3",bytesize=7) as ser:
    while True:
        notes = ser.readline()
        print(notes)