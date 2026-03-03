# 📱 ADB Wireless Manager

Quick and persistent wireless ADB connection manager for Android devices (optimized for Samsung Galaxy S23 Ultra).

## Features

- 🔌 One-click wireless ADB connection
- 🖥️ GUI app for easy management
- 🚀 Terminal shortcut for quick access
- 📌 Desktop shortcut integration
- ⚡ Auto-reconnect capability

## Quick Start

### Prerequisites

- ADB installed (`sudo apt install adb`)
- Android device with USB debugging enabled
- Device and computer on the same WiFi network

### Initial Setup (One-time)

1. Connect your device via USB
2. Run the setup script:
   ```bash
   ./scripts/initial-setup.sh
   ```
3. The script will:
   - Enable ADB over WiFi (port 5555)
   - Detect your device's IP address
   - Configure all connection scripts

### Usage

**Option 1: Terminal (Fastest)**
```bash
./scripts/connect.sh
```

**Option 2: GUI App**
```bash
python3 gui/adb_wireless_manager.py
```

**Option 3: Desktop Shortcut**
- Double-click `ADB Wireless Connect.desktop` on your desktop

## Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd adb-wireless-manager

# Make scripts executable
chmod +x scripts/*.sh

# Optional: Install desktop shortcut
./scripts/install-desktop-shortcut.sh
```

## Configuration

Edit `config.ini` to change:
- Device IP address
- ADB port (default: 5555)
- Device name

## Files

```
adb-wireless-manager/
├── scripts/
│   ├── connect.sh          # Quick connect script
│   ├── initial-setup.sh    # One-time setup script
│   └── install-desktop-shortcut.sh
├── gui/
│   └── adb_wireless_manager.py  # GUI application
├── ADB Wireless Connect.desktop  # Desktop shortcut
├── config.ini              # Configuration file
├── README.md
└── requirements.txt
```

## Troubleshooting

**Device not connecting?**
- Ensure both devices are on the same WiFi network
- Check that Wireless Debugging is enabled on your phone
- Verify the IP address is correct (run `./scripts/initial-setup.sh` to update)

**IP address changed?**
- Run `./scripts/initial-setup.sh` again to detect new IP
- Or manually update `config.ini`

## License

MIT License

## Author

Created for Galaxy S23 Ultra wireless ADB management
