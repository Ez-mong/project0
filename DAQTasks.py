# NI DAQ USB-6212 BNC를 사용한다
# DAQ 보드를 사용하면서 필요한 메소드를 작성해 만들었다
# DAQ 보드로 scanning system에 필요한 메소드
# DAQ 보드로 data 수집에 필요한 메소드
# 기본적인 메소드를 작성을 한다.

from typing import Tuple
import numpy as np
import numpy.typing
import nidaqmx
from nidaqmx.constants import AcquisitionType, RegenerationMode
import time
from GenerateSignalData import GenerateSignalData



def main_variable():
    """ nidaqmx 함수에 필요한 공통 변수를 정의."""
    buffer_size = 10000
    return buffer_size

class DAQTasks(nidaqmx.Task):
    """신호의 입출력을 컨트롤하고, 다른 모듈에 사용될 기본 함수 정의."""
    
    def __init__(self):
        # 상속받은 부모 클래스인 Task를 초기화
        nidaqmx.Task.__init__(self)
    
    def generate_scan_signal(self):
        """스캔 신호 생성: 삼각파 및 계단파."""
        self.x_signals = GenerateSignalData.generate_triangle()
        self.y_signals = GenerateSignalData.generate_step()

        self.task = nidaqmx.Task()
        self.task.ao_channels.add_ao_voltage_chan("Dev1/ao0", min_val=-1.0, max_val=+1.0)
        self.task.ao_channels.add_ao_voltage_chan("Dev1/ao1", min_val=-1.0, max_val=+1.0)
        self.task.timing.cfg_samp_clk_timing(rate=1000, sample_mode=AcquisitionType.CONTINUOUS)
        
        data = np.vstack((self.x_signals, self.y_signals))
        self.task.write(data, auto_start=False)
        self.task.start()
        time.sleep(1)
        self.task.stop()
        self.task.close()
    
    def generate_posi_signal(self):
        """고정 신호 생성."""
        self.x_signals = GenerateSignalData.generate_constant()
        self.y_signals = GenerateSignalData.generate_constant()

        self.task = nidaqmx.Task()
        self.task.ao_channels.add_ao_voltage_chan("Dev1/ao0", min_val=-1.0, max_val=+1.0)
        self.task.ao_channels.add_ao_voltage_chan("Dev1/ao1", min_val=-1.0, max_val=+1.0)
        self.task.timing.cfg_samp_clk_timing(rate=1000, sample_mode=AcquisitionType.CONTINUOUS)

        data = np.vstack((self.x_signals, self.y_signals))
        self.task.write(data, auto_start=False)
        self.task.start()
        time.sleep(1)
        self.task.stop()
        self.task.close()