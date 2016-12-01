import BaseHTTPServer
from w1thermsensor import W1ThermSensor

HOST_NAME = ''
PORT_NUMBER = 8000

sensor = W1ThermSensor()

class WebTemp(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(s):
        #temp_c = sensor.get_temperature() #Celsius, full precision
        #temp_f = sensor.get_temperature(W1ThermSensor.DEGREES_F) #Fahrenheit, full precision
        temp_f = str(round(sensor.get_temperature(W1ThermSensor.DEGREES_F),1)) #Fahrenheit, round to one decimal place
        s.send_response(200)
        s.send_header("Content-Type", "text/plain")
        s.end_headers()
        s.wfile.write("Probe 1|"+temp_f)

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), WebTemp)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
