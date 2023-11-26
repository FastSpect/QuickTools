import os

from twisted.cred.checkers import AllowAnonymousAccess, FilePasswordDB
from twisted.cred.portal import Portal
from twisted.internet import reactor
from twisted.protocols.ftp import FTPFactory, FTPRealm


def start_ftp_server():
    host = "127.0.0.1"
    port = 21

    print(f"Starting FTP server on {host}:{port}...")

    portal = Portal(
        FTPRealm(os.path.dirname(os.path.realpath(__file__))),
        [
            AllowAnonymousAccess(),
        ],
    )
    factory = FTPFactory(portal)
    factory.passivePortRange = range(30000, 31000)
    reactor.listenTCP(port, factory, interface=host)

    try:
        reactor.run()
    except KeyboardInterrupt:
        raise


if __name__ == "__main__":
    start_ftp_server()
