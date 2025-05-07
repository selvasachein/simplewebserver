from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>TCP/IP PROTOCOLS</title>
    <style>
        .head-box{
            border:2px black solid;
            border-radius: 20px;
            text-align: center;
            font-family: 'Times New Roman', Times, serif;
            font-size: medium;
            width: 50%;
            margin: 20px auto;
            background: linear-gradient(to bottom, #ffffff, #9ee4fe) ;
            color: black solid;
        }
        .info-box{
            margin: 20px auto;
            width: 60%;
            border-radius: 20px;
            overflow: hidden;
            border: 2px solid black;
        }
        .info-box table{
            width: 100%;
            border-collapse: collapse;
            font-family: 'Times New Roman', Times, serif;
            background-color: #9ee4fe;
        }
        
        
        .info-box th, .info-box td{
            font-size: larger;
            padding: 20px;
            text-align: left;    
            border: 1px solid black;
            
        }
        
    </style>
</head>
<body>
    <div class="container">
        <div class="head-box">
            <h1 id="111">TCP/IP</h1>
        </div>

        <div class="info-box" >
        <table>
           <tr><th><b>TCP/IP LAYER</b></th><th><b>PROTOCOL</b></th></tr>
           <tr><td>Application Layer</td><td>HTTP, FTP, SMTP, DNS, DHCF</td></tr>
           <tr><td>Transport Layer</td><td>TCP, UDP</td></tr>
              <tr><td>Internet Layer</td><td>IP(IPv4, IPv6), ICMP, ARP, IGMP</td></tr>
              <tr><td>Network Access Layer</td><td>Ethernet, WI-FI, PPP, Slip</td></tr>
             
        </table>
        </div>
    </div>
</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()