import network
import time
import socket


def web_page():
  html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
            <body><h1>Hello World</h1></body></html>
         """
  return html

"""from network import WLAN
wlan = WLAN(mode=WLAN.STA)
wlan.connect(ssid='mywifi', auth=(WLAN.WPA2_ENT, 'username', 'password'), [identity='myidentity', ca_certs='/flash/cert/ca.pem'])"""
def connect_eduroam():
    station = network.WLAN(network.STA_IF)
    if not station.isconnected():
        print('connecting to network...')
        station.active(True)
        station.connect(
            ssid='eduroam',
            key='Namaganda.7',

            #security=network.WLAN.WPA2
            #'shawal.mbalire@students.mak.ac.ug','Namaganda.7',
            )
        while not station.isconnected():
            pass
    print('network config:', station .ifconfig())

def ap_mode(ssid, password):
    ap = network.WLAN(network.AP_IF)
    ap.config(essid=ssid, password=password)
    ap.active(True)

    while ap.active() == False:
        pass
    print('AP Mode Is Active, You can Now Connect')
    print('IP Address To Connect to:: ' + ap.ifconfig()[0])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)

    while True:
      conn, addr = s.accept()
      print('Got a connection from %s' % str(addr))
      request = conn.recv(1024)
      print('Content = %s' % str(request))
      response = web_page()
      conn.send(response)
      conn.close()
def main():
    connect_eduroam()
    ap_mode('Shawal RP Pico W','12121212')

if __name__ == '__main__':
    main()
