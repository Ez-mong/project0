# NI DAQ USB-6212 BNC를 사용한다
# DAQ 보드를 사용하면서 필요한 메소드를 작성해 만들었다
# DAQ 보드로 scanning system에 필요한 메소드
# DAQ 보드로 data 수집에 필요한 메소드
# 기본적인 메소드를 작성을 한다.

from typing import Tuple
import nidaqmx.errors
import numpy as np
import numpy.typing
import nidaqmx
from nidaqmx.constants import AcquisitionType, RegenerationMode
import time
from GenerateSignalData import GenerateSignalData


# main_variable이 필요할까...?
def main_variable():
    """ nidaqmx 함수에 필요한 공통 변수를 정의."""
    buffer_size = 10000
    return buffer_size


# DAQ로 할 작업을 작성 신호 생성, data 정보 얻기
class DAQTasks(nidaqmx.Task):
    # DAQTasks class가 nidaqmx.Task를 상속받고 있으며,
    # self는 자동으로 nidaqmx.Task의 인스턴스가 된다
    # self.task = nidaqmx.Task() 구문 할 필요 없다
    # 바로 self.로 메서드 사용하면 됨
    """신호의 입출력을 컨트롤하고, 다른 모듈에 사용될 기본 함수 정의."""
    
    def __init__(self):
        # 상속받은 부모 클래스인 Task를 초기화
        nidaqmx.Task.__init__(self)
        self.generate = GenerateSignalData()
    
    def generate_scan_signal(self):
        """스캔 신호 생성: 삼각파 및 계단파."""
        self.x_signals = self.generate.generate_triangle() # 변수 조건 기입
        self.y_signals = self.generate.generate_step()     # 변수 조건 기입

        self.ao_channels.add_ao_voltage_chan("Dev1/ao0", min_val=-1.0, max_val=+1.0)
        self.ao_channels.add_ao_voltage_chan("Dev1/ao1", min_val=-1.0, max_val=+1.0)
        self.timing.cfg_samp_clk_timing(rate=1000, sample_mode=AcquisitionType.CONTINUOUS)
        
        data = np.vstack((self.x_signals, self.y_signals))
        self.write(data, auto_start=False)
        self.start()
        time.sleep(1)
        self.stop()
        self.close()
    
    def generate_posi_signal(self):
        """고정 신호 생성."""
        self.x_signals = self.generate.generate_constant() # 변수 조건 기입
        self.y_signals = self.generate.generate_constant() # 변수 조건 기입

        self.ao_channels.add_ao_voltage_chan("Dev1/ao0", min_val=-1.0, max_val=+1.0)
        self.ao_channels.add_ao_voltage_chan("Dev1/ao1", min_val=-1.0, max_val=+1.0)
        self.timing.cfg_samp_clk_timing(rate=1000, sample_mode=AcquisitionType.CONTINUOUS)

        data = np.vstack((self.x_signals, self.y_signals))
        self.write(data, auto_start=False)
        self.start()
    
    # scan stop
    def stop_signal(self):
        self.stop()
        self.close()
        
    # Data 수집
    def data_collection(self, num_samples = 1000):
        """Data 수집을 위한 작업"""
        try:
            self.ai_channels.add_ai_voltage_chan("Dev1/ai0")
            self.timing.cfg_samp_clk_timing(rate=1000, sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=num_samples)
            self.start()
            
            data = self.read(number_of_samples_per_channel=num_samples)
            return np.array(data)
        except nidaqmx.errors.DaqError as e:
            print(f"DAQ Error: {e}")
            return np.array([])
        
