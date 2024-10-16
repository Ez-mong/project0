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
    """ nidaqmx 함수에 필요한 공통적인 변수를 정의를 내림.
        이것으로 함수를 사용을 할 때 반복성을 없애고,
        추후 유지보수를 편하게할 목적이다.
        
        return:
        common variable
    """
    buffer_size = 10000
    return buffer_size

class DAQTasks(nidaqmx.Task):
    """ 신호의 입출력을 컨트롤 하고 추후에 있을 
        다른 모듈에 사용이 될 기본이 될 함수를 정의를 내린다.    
    """
    def __init__(self):
        # 상속받은 부모클래스인 Task를 초기화하는 단계
        nidaqmx.Task.__init__(self)
        return
    
    # 아날로그 시그널을 생성을 한다
    # 계단파와 삼가파를 이용해서 전기 신호를 만든다
    def generatea_scan_signal(self):
        #추후에 변수를 집어 넣줘야 한다
        self.x_signals= GenerateSignalData.generate_triangle
        self.y_signals = GenerateSignalData.generate_step
        
        self.task = nidaqmx.Task()
        self.task.ao_channels.add_ao_voltage_chan("Dev1/ao0",min_val=-1.0,max_val=+1.0)
        self.task.ao_channels.add_ao_voltage_chan("Dev1/ao1",min_val=-1.0,max_val=+1.0)
        self.task.timing.cfg_samp_clk_timing(rate=)
        
        data = np.vstack((self.x_signals, self.y_signals))
        self.task.write(data, auto_start=True)
    
    def generate_posi_signal(self):
        self.x_signals = GenerateSignalData.generate_constant()
        self.y_signals = GenerateSignalData.generate_constant()
        
        self.task = nidaqmx.Task()
        self.task.ao_channels.add_ao_voltage_chan("Dev1/ao0",min_val=-1.0,max_val=+1.0)
        self.task.ao_channels.add_ao_voltage_chan("Dev1/ao1",min_val=-1.0,max_val=+1.0)
        self.task.timing.cfg_samp_clk_timing()
        
        data = np.vstack((self.x_signals, self.y_signals))
        self.task.write(data, auto_start=True)
    
    
    # data 수집을 위한 함수를 작성을 하자