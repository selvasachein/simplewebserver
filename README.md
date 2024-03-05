# EX01 Developing a Simple Webserver
## Date:

## AIM:
To develop a simple webserver to serve html pages.

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
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
       <title>Software Company </title>
       <body>
               <table border="2" cellspacing="10" cellpadding="6">
                       <caption> Top five highest revenue generating software companies </caption>
                       <tr> 
                              <th> Serial number </th>
                              <th> Companies </th>
                              <th> Revenue Generated </th>
                       </tr>
                       <tr>
                              <th> 1, </th>
                              <td> Oracle </td>
                              <td> $203.08 billion </td>
                       </tr>
                       <tr> 
                              <th> 2, </th>
                              <td> Microsoft </td>
                              <td> $46.07 billion </td>
                       </tr>
                       <tr>
                              <th> 3, </th>
                              <td> SAP </td>
                              <td> $32.97 billion </td>
                       </tr>
                       <tr>
                              <th> 4, </th>
                              <td> Salesforce </td>
                              <td> $30.29 billion </td>
                       </tr>
                       <tr>
                              <th> 5, </th>
                              <td> Adobe </td>
                              <td> $17.61 billion </td>
                       </tr>

                       </table>
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

## OUTPUT:
![SS-1](https://github.com/selvasachein/simplewebserver/assets/151864235/a3f975f6-298e-49de-87d7-c5ef4fb99281)


## RESULT:
The program for implementing simple webserver is executed successfully.
