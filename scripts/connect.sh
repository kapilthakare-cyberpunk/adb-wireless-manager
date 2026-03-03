#!/bin/bash
# ADB Wireless Connect Script
# Quick reconnection for wireless ADB

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
CONFIG_FILE="$PROJECT_DIR/config.ini"

# Read configuration
DEVICE_IP=$(grep "^ip" "$CONFIG_FILE" | cut -d'=' -f2 | tr -d ' ')
DEVICE_PORT=$(grep "^port" "$CONFIG_FILE" | cut -d'=' -f2 | tr -d ' ')
DEVICE_NAME=$(grep "^name" "$CONFIG_FILE" | cut -d'=' -f2 | tr -d ' ')

echo "🔌 Connecting to $DEVICE_NAME via ADB Wireless..."
echo "   IP: $DEVICE_IP:$DEVICE_PORT"
echo ""

# Disconnect any existing connection
adb disconnect "$DEVICE_IP:$DEVICE_PORT" 2>/dev/null
sleep 1

# Connect to device
adb connect "$DEVICE_IP:$DEVICE_PORT"

if adb devices | grep -q "$DEVICE_IP:$DEVICE_PORT"; then
    echo ""
    echo "✅ Connected successfully!"
    echo ""
    adb devices | grep "$DEVICE_IP:$DEVICE_PORT"
else
    echo ""
    echo "❌ Connection failed. Make sure:"
    echo "   1. Phone is on the same WiFi network"
    echo "   2. Wireless debugging is enabled on phone"
    echo "   3. IP address is correct (run ./scripts/initial-setup.sh to update)"
    exit 1
fi
