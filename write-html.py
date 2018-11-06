#!/usr/bin/python
# coding=utf-8

f = open('Hellowrold.html', 'w')
message = """ <html>
<head></head>
<body><p>Hello World!</p></body>
</html>"""
f.write(message)
f.close()
