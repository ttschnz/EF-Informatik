from tornado.httputil import HTTPServerRequest, HTTPConnection

def serve(request: HTTPServerRequest):
    print(request, dir(request))
    print("request.uri:", request.uri, dir(request.uri))
    if isinstance(request.connection, HTTPConnection):
        request.connection.write(b"hello world\n")
        request.connection.close()
