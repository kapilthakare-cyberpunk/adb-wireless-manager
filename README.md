# ADB Wireless Manager

## About
**ADB Wireless Manager** is a Python-based GUI and script suite designed to simplify the management of Android Debug Bridge (ADB) wireless connections. It eliminates the need for repetitive command-line inputs by providing a user-friendly interface for device discovery, pairing, and connection management over a network.

## Features
- **Graphical User Interface:** Easy-to-use Python-based GUI for managing connections.
- **Wireless Connection Support:** Streamlined workflow for ADB over TCP/IP.
- **Automated Discovery:** Quickly identify and connect to available devices on the local network.
- **Persistent Configuration:** Save device IPs and connection ports in `config.ini` for quick access.
- **Direct Scripting:** Standalone scripts for power users who prefer the command line.

## Tech Stack
- **Language:** Python 3.8+
- **Frameworks:** Tkinter/CustomTkinter (GUI)
- **Tools:** Android SDK Platform-Tools (ADB)

## Usage

### Installation
1. Ensure Python 3.8+ is installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure `adb` is in your system PATH.

### Running the Application
To start the GUI:
```bash
python gui/main.py
```

### Command Line Usage
To connect to a device directly using scripts:
```bash
python scripts/connect_wireless.py --ip <device-ip> --port <port>
```

---
*Maintained by Kapil T.*
