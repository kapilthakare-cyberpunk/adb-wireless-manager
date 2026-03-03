#!/bin/bash
# Install Desktop Shortcut

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo "Installing desktop shortcuts..."

# Create desktop entry
cat > "$PROJECT_DIR/ADB Wireless Connect.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=ADB Wireless Connect
Comment=Quick connect to Android device via ADB over WiFi
Exec=$PROJECT_DIR/scripts/connect.sh
Icon=system-run
Terminal=true
Categories=Utility;Development;
StartupNotify=false
EOF

# Copy to desktop and applications menu
mkdir -p ~/.local/share/applications
cp "$PROJECT_DIR/ADB Wireless Connect.desktop" ~/.local/share/applications/

if [ -d ~/Desktop ]; then
    cp "$PROJECT_DIR/ADB Wireless Connect.desktop" ~/Desktop/
    chmod +x ~/Desktop/ADB\ Wireless\ Connect.desktop
    echo "✅ Desktop shortcut created: ~/Desktop/ADB Wireless Connect.desktop"
fi

chmod +x "$PROJECT_DIR/ADB Wireless Connect.desktop"
echo "✅ App menu entry installed: ~/.local/share/applications/"

echo ""
echo "Desktop shortcut installation complete!"
