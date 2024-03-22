import serial.tools.list_ports


try:
    ser = serial.Serial("COM3", 9600, timeout=2)

    leitura_serial = ser.read(8)
    print("leitura serial", leitura_serial)
    if leitura_serial:
        peso_inicial = leitura_serial.decode().strip()
        print("peso_inicial_code", peso_inicial)

        ser.close()

    else:
        print("Nenhum dado recebido. Fechando a porta serial.")
        ser.close()

except serial.SerialException as e:
    print(f'A porta não foi encontrada!\n\n- {e}')
