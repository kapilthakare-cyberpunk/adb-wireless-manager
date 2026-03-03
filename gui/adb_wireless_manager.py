#!/usr/bin/env python3
"""
ADB Wireless Manager
GUI application for easy wireless ADB connection management
"""

import subprocess
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import configparser
import os

class ADBWirelessManager:
    def __init__(self, root):
        self.root = root
        self.root.title("ADB Wireless Manager")
        self.root.geometry("450x400")
        self.root.resizable(False, False)
        
        # Load configuration
        self.config = self.load_config()
        
        # Style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(
            main_frame, 
            text=f"📱 {self.config['device']['name']}",
            font=('Helvetica', 16, 'bold')
        )
        title_label.pack(pady=(0, 5))
        
        self.status_label = ttk.Label(
            main_frame,
            text="Status: Checking...",
            font=('Helvetica', 10)
        )
        self.status_label.pack(pady=(0, 20))
        
        # Connection info
        info_frame = ttk.LabelFrame(main_frame, text="Connection Info", padding="10")
        info_frame.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(info_frame, text=f"IP Address: {self.config['device']['ip']}").pack(anchor=tk.W)
        ttk.Label(info_frame, text=f"Port: {self.config['device']['port']}").pack(anchor=tk.W)
        ttk.Label(info_frame, text=f"Full: {self.config['device']['ip']}:{self.config['device']['port']}").pack(anchor=tk.W)
        
        # Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=10)
        
        self.connect_btn = ttk.Button(
            btn_frame, 
            text="🔌 Connect",
            command=self.connect,
            width=15
        )
        self.connect_btn.pack(pady=5)
        
        self.disconnect_btn = ttk.Button(
            btn_frame,
            text="🔌 Disconnect",
            command=self.disconnect,
            width=15
        )
        self.disconnect_btn.pack(pady=5)
        
        self.refresh_btn = ttk.Button(
            btn_frame,
            text="🔄 Refresh Status",
            command=self.check_status,
            width=15
        )
        self.refresh_btn.pack(pady=5)
        
        self.config_btn = ttk.Button(
            btn_frame,
            text="⚙️ Update IP / Config",
            command=self.update_config,
            width=15
        )
        self.config_btn.pack(pady=5)
        
        # Auto-reconnect checkbox
        self.auto_reconnect_var = tk.BooleanVar(value=False)
        auto_check = ttk.Checkbutton(
            main_frame,
            text="Auto-reconnect on disconnect",
            variable=self.auto_reconnect_var
        )
        auto_check.pack(pady=(15, 0))
        
        # Log area
        log_frame = ttk.LabelFrame(main_frame, text="Log", padding="5")
        log_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        self.log_text = tk.Text(log_frame, height=4, width=40, font=('Courier', 8))
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
        # Initial status check
        self.check_status()
    
    def load_config(self):
        config = configparser.ConfigParser()
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.dirname(script_dir)
        config_file = os.path.join(project_dir, 'config.ini')
        
        if os.path.exists(config_file):
            config.read(config_file)
        else:
            config['device'] = {'name': 'Android Device', 'ip': '192.168.1.47', 'port': '5555'}
            config['settings'] = {'auto_reconnect': 'false', 'timeout': '10'}
        
        return config
    
    def log(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
    
    def run_command(self, cmd):
        try:
            result = subprocess.run(
                cmd, 
                shell=True, 
                capture_output=True, 
                text=True,
                timeout=10
            )
            return result.stdout + result.stderr
        except Exception as e:
            return str(e)
    
    def check_status(self):
        def check():
            self.connect_btn.config(state='disabled')
            output = self.run_command("adb devices")
            
            ip = self.config['device']['ip']
            port = self.config['device']['port']
            
            if f"{ip}:{port}" in output and "device" in output:
                self.status_label.config(text="Status: ✅ Connected", foreground='green')
                self.log(f"✓ Device connected at {ip}:{port}")
            else:
                self.status_label.config(text="Status: ❌ Disconnected", foreground='red')
                self.log("✗ Device not connected")
            
            self.connect_btn.config(state='normal')
        
        threading.Thread(target=check, daemon=True).start()
    
    def connect(self):
        def do_connect():
            self.connect_btn.config(state='disabled')
            ip = self.config['device']['ip']
            port = self.config['device']['port']
            
            self.log(f"Connecting to {ip}:{port}...")
            
            # Disconnect first
            self.run_command(f"adb disconnect {ip}:{port}")
            
            # Connect
            output = self.run_command(f"adb connect {ip}:{port}")
            self.log(output.strip())
            
            # Verify
            devices = self.run_command("adb devices")
            if f"{ip}:{port}" in devices and "device" in devices:
                self.status_label.config(text="Status: ✅ Connected", foreground='green')
                self.log("✓ Connection successful!")
                messagebox.showinfo("Success", f"Connected to {self.config['device']['name']}!")
            else:
                self.status_label.config(text="Status: ❌ Failed", foreground='red')
                self.log("✗ Connection failed")
                messagebox.showerror("Failed", "Could not connect. Check:\n1. Same WiFi network\n2. Wireless debugging enabled\n3. Correct IP address")
            
            self.connect_btn.config(state='normal')
        
        threading.Thread(target=do_connect, daemon=True).start()
    
    def disconnect(self):
        def do_disconnect():
            ip = self.config['device']['ip']
            port = self.config['device']['port']
            
            self.log(f"Disconnecting from {ip}:{port}...")
            output = self.run_command(f"adb disconnect {ip}:{port}")
            self.log(output.strip())
            self.status_label.config(text="Status: ❌ Disconnected", foreground='red')
            self.log("✓ Disconnected")
        
        threading.Thread(target=do_disconnect, daemon=True).start()
    
    def update_config(self):
        dialog = ConfigDialog(self.root, self.config)
        if dialog.result:
            self.config = dialog.result
            self.log("✓ Configuration updated")
            self.check_status()

class ConfigDialog:
    def __init__(self, parent, config):
        self.result = None
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Update Configuration")
        self.dialog.geometry("350x200")
        self.dialog.resizable(False, False)
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        frame = ttk.Frame(self.dialog, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="Device Name:").pack(anchor=tk.W)
        self.name_entry = ttk.Entry(frame, width=40)
        self.name_entry.insert(0, config['device']['name'])
        self.name_entry.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(frame, text="IP Address:").pack(anchor=tk.W)
        self.ip_entry = ttk.Entry(frame, width=40)
        self.ip_entry.insert(0, config['device']['ip'])
        self.ip_entry.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(frame, text="Port:").pack(anchor=tk.W)
        self.port_entry = ttk.Entry(frame, width=40)
        self.port_entry.insert(0, config['device']['port'])
        self.port_entry.pack(fill=tk.X, pady=(0, 15))
        
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill=tk.X)
        
        ttk.Button(btn_frame, text="Save", command=self.save).pack(side=tk.LEFT)
        ttk.Button(btn_frame, text="Cancel", command=self.dialog.destroy).pack(side=tk.LEFT, padx=10)
        
        self.dialog.wait_window()
    
    def save(self):
        config = configparser.ConfigParser()
        config['device'] = {
            'name': self.name_entry.get(),
            'ip': self.ip_entry.get(),
            'port': self.port_entry.get()
        }
        config['settings'] = {'auto_reconnect': 'false', 'timeout': '10'}
        
        # Save to file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.dirname(script_dir)
        config_file = os.path.join(project_dir, 'config.ini')
        
        with open(config_file, 'w') as f:
            config.write(f)
        
        self.result = config
        self.dialog.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ADBWirelessManager(root)
    root.mainloop()
