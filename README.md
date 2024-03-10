![Screenshot 2024-03-10 112500](https://github.com/selvasachein/simplewebserver/assets/149148235/070e006f-269b-491e-9440-df3a1a049b6f)# EX01 Developing a Simple Webserver
## Date: 212223040083

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
<HTML>
    <head>
        
    </head>
    <body
        bgcolor="pink">
        <font color="black"  size="75" >
        <center><h1>HOMIES OF SEC</h1></center>
        <table bgcolor="red"
        border="20" 
        align="center">
            <tr
            bgcolor="white"
            cellspace="10">
                <th>NAME</th>
                <TH>DEPT</TH>
                <TH>AGE</TH>
            </tr>
            <TR  bgcolor="white"
            cellspace="10">
                <TD> KAMALESH</TD>
                <TD> CSE</TD>
                <TD>17 </TD>
            </TR>
            <TR bgcolor="white"
            cellspace="10">
                <TD> KIRAN</TD>
                <TD> CSE</TD>
                <TD>18</TD>
            </TR>
            <TR bgcolor="white"
            cellspace="10">
                <TD> ROHIT</TD>
                <TD> CSE</TD>
                <TD>19</TD>
            </TR>
            <TR bgcolor="white"
            cellspace="10">
                <TD> PRADEEP</TD>
                <TD> IT</TD>
                <TD>18</TD>
            </TR>
            <TR bgcolor="white"
            cellspace="10">
                <TD>SUBBIAH</TD>
                <TD> IT</TD>
                <TD>17</TD>
            </TR>
            <TR bgcolor="WHITE"
            cellspace="10" >
                <TD> JABEZ</TD>
                <TD> CSE</TD>
                <TD>18</TD>
            </TR>
            <TR bgcolor="white"
            cellspace="10">
                <TD>DEVA SANJAY</TD>
                <TD> CSE</TD>
                <TD>17</TD>
            </TR>
            <TR bgcolor="white"
            cellspace="10">
                <TD> KAVIYA</TD>
                <TD> CSE</TD>
                <TD>18</TD>
            </TR>
            <TR bgcolor="white"
            cellspace="10">
                <TD> RAKSHITHA</TD>
                <TD> IT</TD>
                <TD>18</TD>
            </TR>
            <TR bgcolor="white"
             cellspace="10">
                <TD> DAISY</TD>
                <TD> IT</TD>
                <TD>18 </TD>
            </TR>
        </table>
    </body>
</HTML>
"""

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode())
print("This is my webserver")
server_address =('',80)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()


## OUTPUT:

![Screenshot 2024-03-10 112437](https://github.com/selvasachein/simplewebserver/assets/149148235/70666ad0-c0e3-4a90-90aa-c48669962c34)

![Screenshot 2024-03-10 112500](https://github.com/selvasachein/simplewebserver/assets/149148235/d6aaa16c-82d6-44ef-b856-6cace95aee50)


## RESULT:
The program for implementing simple webserver is executed successfully.
