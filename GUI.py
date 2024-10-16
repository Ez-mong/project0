import tkinter as tk
from DAQTasks import DAQTasks

class ScanningWindow:
    def __init__(self,root):
        self.root = root
        self.root.title("ScanningWindow")
        
        self.DAQ = DAQTasks
        
        self.scan_start_button = tk.Button(root, text = "SCAN", command= self.start_scan)
        self.scan_start_button.pack(pady = 20)
        
    def start_scan(self):
        self.DAQ.generate_scan_signal()
        self.scan_start_button.config(text = "scanning in progress...")