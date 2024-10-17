""" Detector를 이용해서 수집한 정보(data)를 받아서 가공하는 메소드를
    만들어 놓았다 그래프 plot, save, edit을 할 수 있게 만들 예정이다
"""

import matplotlib.pyplot as plt
import numpy as np

class DataProcessor:
    def __init__(self):
        # 추후 코드 작성
        pass
    
    def data_plot(self, data: np.ndarray):
        """DAQ로 받은 data를 plot"""
        plt.figure()
        plt.plot(data)
        plt.title("DAQ Data Plot")
        plt.xlabel("sample")
        plt.ylabel("signal")
        plt.grid(True)
        plt.show()
        
    def data_process1(self, data: np.ndarray):
        """데이터 처리할 수 있는 함수만들기, 꼭 하나일 필요는 없다. 데이터 노이즈 제거
            필터링, 스무딩, fft(fast fourier transform 등)을 작성해서 추후에
            프로그램으로 정보를 어느 정도 가공을 해서 저장을 할 수 있게 만들자
        """
        return data    