def connect(host,port=3306,protocol="tcp"):
    print("host",host)
    print("port",port)
    print("protocol",protocol)
    print()
connect("localhost",port=3342)
connect("localhost",80,protocol="gcl")
connect("localhost",protocol="9999")