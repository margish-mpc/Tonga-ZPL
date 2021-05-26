import socket

PRINTER_PORT = 9100

MODEL = "QS-CO-001"
SERIAL_NO = "MMYY-abc123"
FCC_ID = "123456789"

def print_label_prod_1x1(ip, model, serial_no, fcc_id):
    label_file = open("prod_label_1x1.zpl")
    zpl_print_str = label_file.read()
    label_file.close()

    zpl_print_str = zpl_print_str.replace(MODEL, model)
    zpl_print_str = zpl_print_str.replace(SERIAL_NO, serial_no])
    zpl_print_str = zpl_print_str.replace(FCC_ID, fcc_id)
    print(zpl_print_str)
    return
    new_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    new_socket.connect((ip, PRINTER_PORT))
    new_socket.send(zpl_print_str.encode())
    new_socket.close()