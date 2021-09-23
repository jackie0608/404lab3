#!/usr/bin/env python3

import cgi, cgitb
import os, json
import templates
import secret
import sys

cgitb.enable()
form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')




if username == secret.username and password == secret.password:
	print("Content-type:text/html\r\n\r\n")
	print("Set-Cookie: UserID = %s\r\n;" % (username))
	print("Set-Cookie: Password = %s\r\n" % (password))
	
	print("<html>")
	print("<head>")
	print("<title>Test CGI</title>")
	print("</head>")
	print(templates.secret_page(username, password))
	print("</html>")


else:
	
	print("Content-type:text/html\r\n\r\n")
	print("<html>")
	print("<head>")
	print("<title>Test CGI</title>")
	print("</head>")
	print("<body>")
	print("<p>Hello World cmput 404</p>")
	
	posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
	if posted_bytes:
    		posted = sys.stdin.read(int(posted_bytes))
    		print(f"<p> POSTED: <pre>")
    		for line in posted.splitlines():
    	    		print(line)
    		print("</pre></p>")


	print(templates.login_page())

	#print(os.environ)
	json_obj = json.dumps(dict(os.environ), indent=4)
	print(json_obj)
	
	print("</body>")
	print("</html>")


