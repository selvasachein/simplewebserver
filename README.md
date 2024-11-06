# EX01 Developing a Simple Webserver
## Date:05.11.2024

## AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
'''
from http.server import HTTPServer,BaseHTTPRequestHandler

content='''

<html>
    <head>
        <center>
        <tittle>
           <b>LAPTOP CONFIGURATION</b>
            </tittle>
        </head>
        <boby>
            <table border="2" cellpadding="10">
            <tr> 
                <td>Brand</td>       
                <td>Lenovo</td>
                </tr>
                <tr>
                <td>Series</td>
                <td>ThinkPad E16 Gen1</td>
                </tr>
                <tr>
                    <td>Processor Brand</td>
                    <td>INTEL</td>
                    </tr>
                    <tr>
                        <td>Processor Type</td>
                        <td>Core 15</td>
                        </tr> 
                        <tr>
                            <td>Graphics Card Interface</td>
                            <td>Integrated</td>
                            </tr>
                            <tr>
                                <td>Operating System</td>
                                <td>Windows 11 Home</td>
                                </tr> 
        </table>
   

</html>


'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
'''

## OUTPUT:
![alt text](<Screenshot 2024-11-06 190005.png>)

![alt text](<Screenshot 2024-11-06 190023.png>)


## RESULT:
The program for implementing simple webserver is executed successfully.
