from http.server import HTTPServer,BaseHTTPRequestHandler

content='''

<html>
    <boby>
    <form>
        <label>Work Application Form</label><br><br>
        <label>Designation*</label>
        <select>
            <option>Manager</option><option>Developer</option><option>Tester</option>
        </select><br><br>

        <label>Applicant Name*</label>
        <input type="Applicant Name"><br><br>

        <label>Date of Birth*</label>
        <input type="date"><br><br><br>

        <label>Education Details</label><br><br>
        <input type="checkbox">PG<br>
        <input type="checkbox">UG<br>
        <input type="checkbox">HSC<br><br><br>
        
        <label>Resume Upload*</label>
        <input type="file">
        <br>
            About yourself:
            <textarea rows="4 cols=50"></textarea>
        </form>
    </boby>


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