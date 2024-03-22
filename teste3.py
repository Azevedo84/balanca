import serial
import serial.tools.list_ports
import time
import re


def ler_peso():
    try:
        while True:
            ser = serial.Serial("COM3", 9600, timeout=2)

            leitura_serial = ser.read(8)
            print(f"leitura_serial: {leitura_serial}")

            peso_decode = leitura_serial.decode().strip()

            padrao = re.compile(r'\d+\.\d+')

            peso_final = padrao.findall(str(peso_decode))
            print(float(peso_final[0]))

            print("fim")
            ser.close()

            time.sleep(2)

    except serial.SerialException as e:
        print(f'Erro na porta serial: {e}')


ler_peso()
