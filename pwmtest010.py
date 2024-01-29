from ast import While
import time
import RPi.GPIO as GPIO

# GPIO 핀번호 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.in) # PWM 신호를 읽기 위한 핀 설정
GPIO.setup(12. GPIO.out) # PWM 신호를 출력하기 위한 핀 설정

pwm_out = GPIO.PWM(12, 100) # 12번 핀에 100Hz의 PWM 신호를 출력
pwm_out.start(0) # 초기 듀티비 설정

try:
    While True:
    pwm_value = GPIO.input(18) # 18번 핀의 PWM 신호를 읽음
    print("PWM Value: ", pwm_value)
    pwm_out.ChangeDutyCycle(pwm_value) # 읽은 PWM 값을 12번 핀으로 출력
    time.sleep(0,1) #0.1초 동안 대기
except KeyboardInterrupt:
    pwm_out.stop()
    GPIO.cleanup()    
      