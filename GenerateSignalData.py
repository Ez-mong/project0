from typing import Tuple
import numpy as np
import numpy.typing



class GenerateSignalData:
    """ 스캐닝 및 영점조절을 위한 전기 신호를 만들기 위한
        신호를 구성하는 data를 만들어 내는 class입니다
        이 함수를 가지고 DAQTask에서 출력을 하게 해준다  
    """
    def __init__(self):
        self.frequency: float = 1,
        self.amplitude: float = 1,
        self.sampling_rate: float = 10000,
        self.number_of_samples: int = 10000
              
    def generate_sine_wave(
        self,
        frequency: float,
        amplitude: float,
        sampling_rate: float,
        number_of_samples: int,
        phase_in: float = 0.0,
    ) -> Tuple[numpy.typing.NDArray[numpy.double], float]:
        # '--> , :'은type hint(있어도 그만 없어도 그만, 대신 가독성이 높어짐,정적 분석 도구 지원, 코드 유지 보수 유리)
        # 봔환값으로 함수의 return값이 어떤식으로 나오는 지 명시
        # []는 tuple형태로 자료가 return이 된다, 1번 째 값은 Numpy배열의 값, 2번 째 float값으로 반환이 되는 뜻 
        # 이는 필수가 아님 개발자에게 도움을 주기 위한 가이드일 뿐이다
        """Generates a sine wave with a specified phase.

        Args:
            frequency: Specifies the frequency of the sine wave.
            amplitude: Specifies the amplitude of the sine wave.
            sampling_rate: Specifies the sampling rate of the sine wave.
            number_of_samples: Specifies the number of samples to generate.
            phase_in: Specifies the phase of the sine wave in radians.

        Returns:
            Indicates a tuple containing the generated data and the phase
            of the sine wave after generation.
        """
        duration_time = number_of_samples / sampling_rate
        duration_radians = duration_time * 2 * np.pi
        phase_out = (phase_in + duration_radians) % (2 * np.pi)
        t = np.linspace(phase_in, phase_in + duration_radians, number_of_samples, endpoint=False)

        return (amplitude * np.sin(frequency * t), phase_out)
    
    def generate_triangle(
        self,
        frequency,
        voltage,
        sampling_rate: int, 
        duration = 1.0):
        t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
        signal = (2 * voltage * np.abs(np.mod(t * frequency, 1.0)-0.5) - 0.5*voltage)*2
        return signal
    
    def generate_step(
        self,
        steps,
        voltage,
        sampling_rate: int,
        duration = 1.0,
    ):
        step_size = duration / steps
        signal = np.repeat(np.linspace(-voltage, voltage,steps), int(step_size * sampling_rate))
        return signal
    
    def generate_zero(
        self,
        sampling_rate
    ):
        np.zeros(int(sampling_rate))
        return np.zeros(int(sampling_rate))
    
    def generate_constant(
        self,
        sampling_rate,
        volatage
    ):
        np.ones(int(sampling_rate)) * volatage
        return np.ones(int(sampling_rate)) * volatage