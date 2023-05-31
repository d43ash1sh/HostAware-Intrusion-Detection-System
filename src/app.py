#This is the main file for Hostaware IDS 
from flask import Flask, render_template, redirect, url_for, request
import eventlet
from flask_socketio import SocketIO
from colorama import Fore, Back, Style
import werkzeug
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep
from flask import Flask
from scapy.all import *
from colorama import Fore, Back, Style
import logging
import socket

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)
print(Fore.RED + """
 ██░ ██  ▒█████    ██████ ▄▄▄█████▓    ▄▄▄       █     █░ ▄▄▄       ██▀███  ▓█████
▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒   ▒████▄    ▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒▓█   ▀
▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░   ▒██  ▀█▄  ▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒▒███
░▓█ ░██ ▒██   ██░  ▒   ██▒░ ▓██▓ ░    ░██▄▄▄▄██ ░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄
░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░     ▓█   ▓██▒░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒░▒████▒
 ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░       ▒▒   ▓▒█░░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░
                                                                                    """)

class Loader:
    def __init__(self, desc="Loading...", end="Done!", timeout=0.1):
        """
        A loader-like context manager

        Args:
            desc (str, optional): The loader's description. Defaults to "Loading...".
            end (str, optional): Final print. Defaults to "Done!".
            timeout (float, optional): Sleep time between prints. Defaults to 0.1.
        """
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()


if __name__ == "__main__":
    with Loader("Starting Host Aware IDS..."):
        for i in range(10):
            sleep(0.25)


    loader = Loader("Initializing Network monitoring [+]", "Done!", 0.05).start()
    for i in range(10):
        sleep(0.25)
    loader.stop()
print("Please visit this link or copy paste the url for Dashboard view")
print(Fore.BLUE + "URL - http://127.0.0.1:8181/")



app = Flask(__name__,template_folder='templates')

@app.route('/', methods=['GET', 'POST'])    
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect('dashboard')
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    open_ports = []
    target_ip = '127.0.0.1'  # Replace with your local machine's IP address

    # Define the range of ports you want to scan
    start_port = 1
    end_port = 25

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
        

    return render_template('dashboard.html',  open_ports=open_ports)

@app.route('/settings')
def settings():
    return render_template('settings.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181, debug=True)
    socketio.run(app)