Using `http.server` module
===

 ## Running a demo server 

 1. Open up a terminal.
 
 2. `cd` into a directory that has some files in it (maybe a directory containing some text files, HTML files, or images ).
 
 3. Run `python3 -m http.server 8000` in your terminal.


## Description

The demo server is actually a web server. If you have another computer on the same local network, you could use it to access files served up by this server.

When you put  `localhost:8000`  in your browser, your browser sends an HTTP request to the Python program `(here representing the web-browser)` you're running. That program responds with a piece of data, which your browser presents to you. If you place a index.html file in the same directory it can be viewed using a client app like a web-browser.