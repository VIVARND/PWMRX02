mport RPi.GPIO as GPIO
import time

# BCM 핀 번호를 사용
GPIO.setmode(GPIO.BCM)

# PWM 핀 선언
BCM12_PWM0 = 12
BCM18_PWM0 = 13
BCM13_PWM1 = 18

# GPIO 핀 설정
GPIO.setup(BCM12_PWM0, GPIO.OUT)
GPIO.setup(BCM18_PWM0, GPIO.OUT)
GPIO.setup(BCM13_PWM1, GPIO.OUT)

# PWM 주파수 설정 (50Hz)
pwm0 = GPIO.PWM(BCM12_PWM0, 50)
pwm1 = GPIO.PWM(BCM18_PWM0, 50)
pwm2 = GPIO.PWM(BCM13_PWM1, 50)

# PWM 시작
pwm0.start(0)
pwm1.start(0)
pwm2.start(0)

try:
    while True:
        # 듀티 사이클 변경으로 PWM 신호 조절
        for duty_cycle in range(0, 101, 5):
            pwm0.ChangeDutyCycle(duty_cycle)
            pwm1.ChangeDutyCycle(100 - duty_cycle)
            pwm2.ChangeDutyCycle(duty_cycle)
            time.sleep(0.1)
except KeyboardInterrupt:
    # PWM 정지
    pwm0.stop()
    pwm1.stop()
    pwm2.stop()

    # GPIO 설정 초기화
    GPIO.cleanup()