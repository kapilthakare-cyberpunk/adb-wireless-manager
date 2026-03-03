#!/bin/bash
# Initial Setup Script for ADB Wireless
# Enables wireless ADB and configures connection

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
CONFIG_FILE="$PROJECT_DIR/config.ini"

echo "📱 ADB Wireless Initial Setup"
echo "=============================="
echo ""

# Check if device is connected via USB
echo "Checking for USB-connected devices..."
DEVICES=$(adb devices | grep -v "List" | grep "device$" | grep -v "^[0-9.]*:")

if [ -z "$DEVICES" ]; then
    echo "❌ No USB device found!"
    echo "   Please connect your phone via USB and enable USB debugging."
    exit 1
fi

DEVICE_ID=$(echo "$DEVICES" | head -1 | awk '{print $1}')
echo "✅ Found device: $DEVICE_ID"

# Enable TCP/IP mode
echo ""
echo "Enabling ADB over WiFi (port 5555)..."
adb -s "$DEVICE_ID" tcpip 5555
sleep 2

# Get device IP address
echo ""
echo "Detecting device WiFi IP address..."
DEVICE_IP=$(adb -s "$DEVICE_ID" shell ip -f inet addr show wlan0 2>/dev/null | grep "inet " | awk '{print $2}' | cut -d/ -f1)

if [ -z "$DEVICE_IP" ]; then
    echo "⚠️  Could not auto-detect IP. Using default."
    DEVICE_IP="192.168.1.47"
fi

echo "✅ Device IP: $DEVICE_IP"

# Update configuration
echo ""
echo "Updating configuration..."
cat > "$CONFIG_FILE" << EOF
[device]
name = Galaxy S23 Ultra
ip = $DEVICE_IP
port = 5555

[settings]
auto_reconnect = false
timeout = 10
EOF

echo "✅ Configuration saved to $CONFIG_FILE"

# Test wireless connection
echo ""
echo "Testing wireless connection..."
adb connect "$DEVICE_IP:5555"
sleep 2

if adb devices | grep -q "$DEVICE_IP:5555"; then
    echo ""
    echo "🎉 Setup complete!"
    echo ""
    echo "You can now disconnect USB and use wireless ADB."
    echo "Run './scripts/connect.sh' to reconnect anytime."
    echo ""
    adb devices | grep "$DEVICE_IP:5555"
else
    echo ""
    echo "⚠️  Wireless connection test failed."
    echo "   Keep USB connected and try again."
fi
