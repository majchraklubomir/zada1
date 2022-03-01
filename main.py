import socket
import socketserver
import sipfullproxy

if __name__ == '__main__':
    localhost = "0.0.0.0"
    port = 5060
    ipaddr = socket.gethostbyname_ex(socket.gethostname())[2][4]
    print("Proxy address:", ipaddr)
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddr, port)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddr, port)
    server = socketserver.UDPServer((localhost, port), sipfullproxy.UDPHandler)
    server.serve_forever()
