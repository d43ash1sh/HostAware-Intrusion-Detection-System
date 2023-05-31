# HostAware: Intrusion-Detection-System

The HostAware: Host Based Intrusion-Detection-System is a Python Flask application that provides a dashboard console for monitoring and analyzing attacks on the sytems. The system includes an Intrusion Detection System (IDS) that detects potential attacks in real-time and provides alerts.

## Features

- Real-time monitoring of SSH brute force attacks
- Dashboard console for visualizing attack data
- Detection of open ports, source IP addresses, source ports, and alert ports
- Real-time alerts for potential brute force attacks
- Customizable configuration for IP address, port, and authentication details

## Prerequisites

- Python 3.x
- pip package manager

## Installation

1. Clone the repository:

```shell
git clone https://github.com/your-username/ssh-brute-force-detection.git
```

## Usage

1. Configure the application settings by editing the config.py file. Specify the necessary parameters such as the IP address, port, and authentication details.

2. Start the Flask application:

```shell
python app.py
```

3. Access the application by opening your web browser and navigating to http://<server-ip>:<port>, where <server-ip> is the IP address of the server and <port> is the dedicated port specified in the configuration.

4. Log in to the dashboard using the provided username and password.

5. Monitor the detected attacks on the dashboard. The system will display information about open ports, source IP addresses, source ports, and alert ports. Alerts for potential brute force attacks will be shown in real-time.
