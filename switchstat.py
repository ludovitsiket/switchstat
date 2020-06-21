import telnetlib
import csv
from socket import gaierror


def read_file(addr):
    x = []
    with open(addr) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            x.append(row)
    return x


def cred(data):
    ip, name, pwd = [], [], []
    x = 0
    while x < len(data):
        ip.append(data[x]['address'])
        name.append(data[x]['name'])
        pwd.append(data[x]['password'])
        x += 1
    return (ip, name, pwd)


def connection(ip, name, pwd, x):
    try:
        print(ip[x], name[x], pwd[x])
        tn = telnetlib.Telnet(ip[x])
        print('Connection to ' + ip[x] + ' OK.')
        tn.close()
        print('Connection to ' + ip[x] + ' close.')
    except gaierror as e:
        print(ip[x], e)


def telnet_conn(data):
    try:
        ip, name, pwd = cred(data)
        x = 0
        while x < len(data):
            connection(ip, name, pwd, x)
            x += 1
    except (KeyboardInterrupt, FileNotFoundError) as e:
        print(e)


def main():
    addr = 'addr.csv'
    data = read_file(addr)
    telnet_conn(data)


main()
