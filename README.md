# EX01 Developing a Simple Webserver
## Date:

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
### Index
~~~
<!DOCTYPE html>
<html>
  <head>
    <title>System Configuration</title>
  </head>
  <body>
    <h1>Laptop Configuration Details</h1>
    <ul>
      <li>System: {{ system_info.system }}</li>
      <li>Node: {{ system_info.node }}</li>
      <li>Release: {{ system_info.release }}</li>
      <li>Version: {{ system_info.version }}</li>
      <li>Machine: {{ system_info.machine }}</li>
      <li>Processor: {{ system_info.processor }}</li>
    </ul>
  </body>
</html>
~~~
### app.py
~~~
from flask import Flask, render_template
import platform

app = Flask(__name__)

@app.route('/')
def home():
    # Get system details
    system_info = {
        'system': platform.system(),
        'node': platform.node(),
        'release': platform.release(),
        'version': platform.version(),
        'machine': platform.machine(),
        'processor': platform.processor()
    }
    # Render HTML with system details
    return render_template('index.html', system_info=system_info)

if __name__ == '__main__':
    app.run(debug=True)

~~~

## OUTPUT:
### Web 
![image](https://github.com/user-attachments/assets/94ca0d25-7030-4b21-80b4-a85e72e5289c)


### Server
![image](https://github.com/user-attachments/assets/b3c8d9d2-5c37-4da5-b004-1b387188ba8f)


## RESULT:
The program for implementing simple webserver is executed successfully.
