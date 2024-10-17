""" 양자나노광학 실험실의 처 DIY 실험장비, GalvoScanningSystem
    다른 모듈을 import해서 최종적으로 GUI(tkinter)를 이용해서
    실험장비의 comtrol 및 data 측정을 할 수 있게 만들었다
"""

# 오픈소스로 배포하는 패키지 파잃 import
# Python과 함께 설치된 패키지(표준 라이브러리)는 pip(외부 패키지 관리 도구) 명령어 안 됨
import sys                          # 파이썬 인터프리터와 관련된 시스템 관련 기능을 제공, 인터프리터 제어, 시스템환경과 관련된 정보 확인 
import os                           # Operating System, 운영체제 제공하는 기능(파일 복사, 붙여넣기, 디렉토리 등) 파이썬으로 할 수 있게
import nidaqmx                      # NI DAQ USB-6212 BNC컨트롤 기능 제공
import numpy                        # 데이터의 다차원 배열, 텐서(?), 데이터 분석
import matplotlib.pyplot as plt     # 그래프/data처리
import time                         # 시간을 다루는...시간과 관련된 기능을 제공
import cv2                          # 파이썬으로 영상을 처리하기 위해
import pyuff                        # UFF 파일 형식을 관리하기 위해
import logging                      # 소프트웨어 실행시 이벤트(Debug, Error, Info, Warning, Critical) 정보를 출력
import tkinter as tk                # python으로 GUI만들기

# 이 시스템에서 사용을 위해 만든 패키지 import
import DAQTasks
import GUI
import GenerateSignalData
import Data



#logging.basicConfig(level=logging.INFO) # 기본 로깅 설정, 로그 메시지의 출력 형식
#logger = logging.getLogger(__name__)
def galvo():
    root = tk.Tk()
    app = GUI.ScanningWindow(root)
    root.mainloop()
     
if __name__ == "__main__":
    galvo()