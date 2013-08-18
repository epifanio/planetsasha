#!/usr/bin/env python
import socket
from lxml import etree
	

def parsesignalLookAt(data):
    try :
    	xmldoc = etree.fromstring(data)
	lookat_lat = xmldoc.xpath("//LookAt/latitude/text()")
	lookat_lon = xmldoc.xpath("//LookAt/longitude/text()")
	lookat_alt = xmldoc.xpath("//LookAt/altitude/text()")
	lookat_range = xmldoc.xpath("//LookAt/range/text()")
	lookat_heading = xmldoc.xpath("//LookAt/heading/text()")
	lookat_altmode = xmldoc.xpath("//LookAt/altitudeMode/text()")
	nav = {}
	nav['lookat_lon'] , nav['lookat_lat'] = float(lookat_lon[0]) , float(lookat_lat[0])
	nav['lookat_alt'] , nav['lookat_range'] , nav['lookat_heading'] , nav['lookat_altmode'] = float(lookat_alt[0]), float(lookat_range[0]), float(lookat_heading[0]), str(lookat_altmode[0])
	print nav
	return nav
    except :
    	print 'xml parsing problems in parsesignalLookAt'



def navlogger(host,port):
    HOST = host
    PORT = port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print 'Connected by', addr
    data = conn.recv(1024)
    try :
    	parsed = parseSignal(data)
    	print parsed
    	if not data:
            conn.close()
    except :
    	print 'parse error'
    conn.close()




#addzoom('/data/florida/Brevard.tif',-81.0009,29.0009,15000,'localhost',8000,7000)
#removefile('/data/florida/Brevard.tif','localhost',8000)
