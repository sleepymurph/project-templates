#!/usr/bin/env/python3

# Basic Python HTTP server with threading and shutdown.

import argparse
import http.server
import logging
import re
import signal
import socket
import socketserver
import sys
import threading

#=================================================================
# Command-Line Argument Parsing
#

def parse_args():
    PORT_DEFAULT = None
    DIE_AFTER_SECONDS_DEFAULT = 20 * 60
    SHUTDOWN_GRACE_PERIOD_DEFAULT = 2
    LOG_LEVEL_DEFAULT = "INFO"

    parser = argparse.ArgumentParser(prog=__file__)

    porthelp = "Port number to listen on."
    if PORT_DEFAULT:
        portkwargs = { "default": PORT_DEFAULT,
                "help": porthelp + " Default: {}".format(PORT_DEFAULT) }
    else:
        portkwargs = { "required": True,
                "help": porthelp + " Required." }
    parser.add_argument("-p", "--port", type=int, **portkwargs)

    parser.add_argument("--die-after-seconds", type=float,
            default=DIE_AFTER_SECONDS_DEFAULT,
            help="kill server after so many seconds have elapsed, " +
                "in case we forget or fail to kill it, " +
                "default %d (%d minutes)" % (DIE_AFTER_SECONDS_DEFAULT, DIE_AFTER_SECONDS_DEFAULT/60))

    parser.add_argument("--shutdown-grace-period", type=float,
            default=SHUTDOWN_GRACE_PERIOD_DEFAULT,
            help="When server is asked to shutdown, give it this many seconds to shutdown cleanly. Default: {}".format(SHUTDOWN_GRACE_PERIOD_DEFAULT))

    parser.add_argument("--loglevel", default=LOG_LEVEL_DEFAULT,
            help="Logging level. ERROR, WARN, INFO, DEBUG. Default: {}".format(LOG_LEVEL_DEFAULT))

    return parser.parse_args()


#=================================================================
# HTTP Request Handler
#

class HttpRequestHandler(http.server.BaseHTTPRequestHandler):

    def send_whole_response(self, code, content, content_type=None):

        if isinstance(content, str):
            content = content.encode("utf-8")
            if not content_type:
                content_type = "text/plain"
            if content_type.startswith("text/"):
                content_type += "; charset=utf-8"

        self.send_response(code)
        self.send_header('Content-type', content_type)
        self.send_header('Content-length',len(content))
        self.end_headers()
        self.wfile.write(content)

    def do_GET(self):
        if self.path == "/":
            self.send_whole_response(200, "Hello, world!")
            return

        self.send_whole_response(404, "Unknown path: " + self.path)



#=================================================================
# HTTP Server
#

class ThreadingHttpServer(http.server.HTTPServer, socketserver.ThreadingMixIn):
    pass


def run_http_server(args):
    server = ThreadingHttpServer( ('', args.port), HttpRequestHandler)

    logging.basicConfig(level=args.loglevel)

    def run_server():
        logging.info("Starting server on port %d." , args.port)
        server.serve_forever()
        logging.info("Server has shut down cleanly.")

    # Start HTTP server in a separate thread for proper shutdown
    #
    # serve_forever() and shutdown() must be called from separate threads
    # for the shutdown to work properly.
    # shutdown() is called by signal handlers and by the timeout,
    # which both execute on the main thread.
    # So the server must be running on a separate thread.
    thread = threading.Thread(target=run_server)
    # Setting thread as daemon will allow the program to exit even if the server gets hung up.
    thread.daemon = True
    thread.start()

    def shutdown_server_with_grace_period():
        logging.info("Asking server to shut down.")
        server.shutdown()
        thread.join(args.shutdown_grace_period)
        if thread.isAlive():
            logging.error("Server thread is still alive after %.3f-second grace period. Trying to exit anyway.", args.shutdown_grace_period)
            sys.exit(1)

    def shutdown_server_on_signal(signum, frame):
        if hasattr(signal, "Signals"):
            signame = signal.Signals(signum).name
            sigdesc = "{}, {}".format(signum, signame)
        else:
            sigdesc = str(signum)
        logging.info("Got system signal %s.", sigdesc)
        shutdown_server_with_grace_period()

    # Install signal handlers
    signal.signal(signal.SIGTERM, shutdown_server_on_signal)
    signal.signal(signal.SIGINT, shutdown_server_on_signal)

    # Run until given timeout
    thread.join(args.die_after_seconds)

    # Check if server timed out instead of exiting
    if thread.isAlive():
        logging.warn("Reached %.3f second timeout.", args.die_after_seconds)
        shutdown_server_with_grace_period()


#=================================================================
# Main
#

if __name__ == "__main__":
    args = parse_args()
    run_http_server(args)
