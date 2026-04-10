# adb-wireless-manager

## Overview
Python-based GUI and script suite for managing Android Debug Bridge (ADB) wireless connections. It simplifies the process of connecting to Android devices over a network for remote debugging and file management.

## Project Purpose
Provide a user-friendly interface for ADB wireless operations, reducing the reliance on repetitive command-line inputs. It automates device discovery, pairing, and connection management.

## Key Features
- Graphical Interface: Built with Python for cross-platform device management.
- Wireless Connection Support: Simplifies ADB over TCP/IP connections.
- Automated Discovery: Identifies available devices on the local network.
- Configurable Settings: Persistent storage for device IPs and connection ports via config.ini.

## Prerequisites
- Python (v3.8 or higher).
- Android SDK Platform-Tools (ADB) installed and in System PATH.
- Android device with Wireless Debugging enabled.

## Installation
```bash
git clone https://github.com/kapilthakare-cyberpunk/adb-wireless-manager
cd adb-wireless-manager
pip install -r requirements.txt
```

## Configuration
- Update config.ini with preferred default settings.
- Ensure the Android device is on the same network as the host machine.

## Usage
### Running the GUI
```bash
python gui/main.py
```
### Running scripts directly
```bash
python scripts/connect_wireless.py --ip <device-ip> --port <port>
```

## Development
- Add new features to the gui/ or scripts/ directories.
- Test connection stability across different network conditions.

## License
Refer to the LICENSE file for details.
