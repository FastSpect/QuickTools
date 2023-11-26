from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def start_ftp_server():
    # Create an authorizer
    authorizer = DummyAuthorizer()

    # Add a new user with a username and password
    authorizer.add_user("username", "password",
                        "/path/to/ftp/folder", perm="elradfmw")

    # Create an FTP handler and associate the authorizer
    handler = FTPHandler
    handler.authorizer = authorizer

    # Create an FTP server with the handler
    server = FTPServer(("0.0.0.0", 21), handler)

    print("FTP server started on 0.0.0.0:21...")

    # Start the FTP server
    server.serve_forever()


if __name__ == "__main__":
    start_ftp_server()
