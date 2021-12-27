import os
from log import log, warn, err
log("compiling typescript...")
os.system("tsc")
log("done!")

log("configuring server...")
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application, StaticFileHandler
PORT = 8081
app = Application([
        (r"/(.*)", StaticFileHandler, {"path": "./public_html", "default_filename":"index.html"}),
    ],[
        (r"/(.*)"), warn, {}
    ])

server = HTTPServer(app)
server.listen(PORT)
log(f"done! server running on port {PORT}")
try:
    IOLoop.current().start()
except:
    err(f"server stopped, cleaning up...")
    os.system("rm -rf ./public_html/script")
    log("done!")