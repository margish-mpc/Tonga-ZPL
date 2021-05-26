import sys
import mpc_zebra

def main():
    print('Zebra Printer IP Addr for 1"x1": %s' % (sys.argv[1]))
    print('Model No: %s' % (sys.argv[2]))
    print('S/N : %s' % (sys.argv[3]))
    print('FCC ID : %s' % (sys.argv[4]))
    ip_1x1 = sys.argv[1]
    model = sys.argv[2]
    serial_no = sys.argv[3]
    fcc_id = sys.argv[4]
    mpc_zebra.print_label_prod_1x1(ip_1x1, model,serial_no, fcc_id)

if __name__ == '__main__':
    main()