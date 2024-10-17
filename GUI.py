import tkinter as tk
from DAQTasks import DAQTasks
from Data import DataProcessor

class ScanningWindow:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1820x980')
        self.root.title("ScanningWindow")
        
        self.DAQ = DAQTasks()
        
        self.xscan_voltage_lb = tk.Label(root, text = "X[V]")
        self.xscan_voltage_lb.pack(side="left", anchor="ne", padx = 10, pady = 10)
          
        self.xscan_vlotage_ent = tk.Entry(root,)         
                
        self.yscan_voltage_lb = tk.Label(root, text = "Y[V]")
        self.yscan_voltage_lb.pack(side="left", anchor="e",padx = 10, pady = 10)
        
        self.scan_start_bt = tk.Button(root, text = "SCAN", command= self.start_scan)
        self.scan_start_bt.pack(side = "left",padx = 10, pady = 10)
        
        self.scan_stop_bt = tk.Button(root, text = "STOP", command = self.stop_scan)
        self.scan_stop_bt.pack(side = "left",padx=10,pady=10)
        
        
        self.label = tk.Label(root, text="Status: Idle")
        self.label.pack(pady=10)
        
        self.daq_task = DAQTasks()
        self.data_processor = DataProcessor()
        
    # Start Scanning
    def start_scan(self):
        self.DAQ.generate_scan_signal()
        self.scan_start_bt.config(text = "scanning in progress...")
    
    # stop scan
    def stop_scan(self):
        self.DAQ.stop_signal()
        self.scan_stop_bt.config(text = "scanning stop")
    
    # Locate Position
        
    # Data plot
    def show_data(self):
        self.label.config(text = "Status: collecting Data...")
        data = self.daq_task.data_collection()
        self.data_processor.data_plot(data)
        self.label.config(text="Status: Data Collection Completed")
    
    #