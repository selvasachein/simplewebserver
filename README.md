# EX01 Developing a Simple Webserver
## Date:

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
##<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <style>
        .row1
        {
            background-color: burlywood;
            place-items: center;
            height: 60px;
            font-family: Verdana;
            display: flex;
        }
        i
        {
            color: black
        }
        a
        {
            color:black;
            text-decoration: none;
            padding: 10px;
        }
        a:hover
        {
            color:gray
        }
        i:hover
        {
            color: gray;
        }
        .search
        {
            
            height: 40px;
            width=30px;
            border-radius: 10px; 
            outline: none;
            border: none;
            
        }
    </style>
</head>
<body>
    <div class="row1">
       <div style="width: 35%;" class="i">
            <a href=""><i class="bi bi-whatsapp" style="color: black;font-size: 25px;border: 5px;"></i></a>
            <a href=""><i class="bi bi-facebook" style="color: black;font-size: 25px;border: 5px;"></i></a>
            <a href=""><i class="bi bi-instagram" style="color: black;font-size: 25px;border: 5px;"></i></a>
            <a href=""><i class="bi bi-envelope" style="color: black;font-size: 25px;border: 5px;"></i></a>
            <a href=""><i class="bi bi-twitter" style="color: black;font-size: 25px;border: 5px;"></i></a>
        </div>
        <div style="width:45%;" >
            <a href="">Alumini</a><i class="bi bi-three-dots-vertical"></i>
            <a href="">Events</a><i class="bi bi-three-dots-vertical"></i>
            <a href="">career</a><i class="bi bi-three-dots-vertical"></i>
            <a href="">Login</a><i class="bi bi-three-dots-vertical"></i>
            <a href="">SEC Portal</a>
        </div>
        <div style="width: 10%;">
            <input type="text" name="Search" placeholder="Search" class="search p-2" >
        </div>
    </div style=border>
    <div class="row p-3">
        <div class="col-4">
            <img src="c:\Users\91893\Downloads\HTML\saveetha.png"style width="100%">
        </div>
        <div class="col-8">
            <a href="">Home</a><i class="bi bi-three-dots-vertical"></i>
            <a href="">About</a><i class="bi bi-three-dots-vertical"></i>
            <a href="">Departments</a><i class="bi bi-three-dots-vertical"></i>
            <a href="">Life at SEC</a><i class="bi bi-three-dots-vertical"></i>
            <a href="">Placements</a><i class="bi bi-three-dots-vertical"></i>
            <a href="">Admissions</a>
        </div>
    <div>
        <div style="width: 100%;height=60%;">
            <div id="carouselExample" class="carousel slide">
                <div class="carousel-inner">
                  <div class="carousel-item active">
                    <img src="ex11.png" class="d-block w-100" alt="...">
                  </div>
                  <div class="carousel-item">
                    <img src="ex22.png" class="d-block w-100 h-60" alt="...">
                  </div>
                  <div class="carousel-item">
                    <img src="ex33.png" class="d-block w-100" alt="...">
                  </div>
                </div>
                <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
                  <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                  <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
                  <span class="carousel-control-next-icon" aria-hidden="true"></span>
                  <span class="visually-hidden">Next</span>
                </button>
              </div>
            </div>
    </div>
</body>
</html>##

## OUTPUT:


## RESULT:
The program for implementing simple webserver is executed successfully.
