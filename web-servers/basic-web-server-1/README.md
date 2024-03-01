Using `http.server` module
===


 ## Running a demo server 

 1. Open up a terminal.
 
 2. `cd` into a directory that has some files in it (maybe a directory containing some text files, HTML files, or images ).
 
 3. Run `python -m http.server 8000` in your terminal.


## Description

The demo server is actually a web server. If you have another computer on the same local network, you could use it to access files served up by this server.

When you put  `localhost:8000`  in your browser, your browser sends an HTTP request to the Python program `(here representing the web-browser)` you're running. That program responds with a piece of data, which your browser presents to you. If you place a index.html file in the same directory it can be viewed using a client app like a web-browser.

## What's a server anyway?

A server is just a program that accepts connections from other programs on the network.

When you start a server program, it waits for clients to connect to it — like the demo server waiting for your web browser to ask it for a page. Then when a connection comes in, the server runs a piece of code — like calling a function — to handle each incoming connection. A  _connection_ in this sense is like a phone call: it's a channel through which the client and server can talk to each other. Web clients send requests over these connections, and servers send responses back.

Take a look in the terminal where you ran the demo server. You'll see a  _server log_  with an entry for each request your browser sent:

```
Serving HTTP on 0.0.0.0 port 8000 ...
127.0.0.1 - - [03/Oct/2016 13:47:35] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [03/Oct/2016 13:47:36] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [03/Oct/2016 13:48:06] "GET /falafelosofhy.png HTTP/1.1" 200 -
127.0.0.1 - - [03/Oct/2016 13:49:23] code 404, message File not found
127.0.0.1 - - [03/Oct/2016 13:49:23] "GET /NotExistyFile HTTP/1.1" 404 -
```

RFC 9110
HTTP Semantics
https://www.rfc-editor.org/rfc/rfc9110.html


URI Schemes abd Anatomy by Wiki
https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#Generic_syntax


URI Schemes by IANA
https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml
