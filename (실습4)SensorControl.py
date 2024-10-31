# set_pin_mode(pin:int, mode:Modes)
# 해당 pin의 사용 방식을 mode로 설정한다. 센서 및 모듈을 사용하기 전에 설정해야한다.
# pin -> min = 2, max = 13 (디지털핀 2 ~ 13, 아날로그핀 14 ~ 19)
# mode -> pin의 사용방식을 정한다
# input(입력), analog(아날로그 입력), sonar(초음파센서)

from RobokitRS import *
rs = RobokitRS.RobokitRS()
rs = port_open("com7")

# 적외선 센서
rs.set_pin_mode(12, RobokitRS.Modes.INPUT)
rs.set_pin_mode(13, RobokitRS.Modes.INPUT)
while(True):
    IR = rs.digital_read(12)
    if IR == 1:
        rs.set_rgb_led_red(2)
        rs.set_rgb_led_on(2)
    else:
        rs.set_rgb_led_off(2)

# 초음파 센서
# 초음파 센서를 가동해서 데이터를 수집하는 함수.
rs.sonar_begin(13)
while(True):
    SONAR = rs.sonar_read(13)
    print(SONAR)

# 저장된 초음파 센서 데이터 중에서 핀에 연결된 초음파 세서의 데이터를 반환하는 함수.
rs.sonar_read(13)

# 초음파 거리에 따른 RGB 색상 바꾸기
rs.sonar_begin(13)
while(True):
    SONAR = rs.sonar_read(13)
    if SONAR >= 2 and SONAR <= 5:
        rs.set_rgb_led_red(2)
        rs.set_rgb_led_on(2)
    elif SONAR >= 6 and SONAR <= 10:
        rs.set_rgb_led_orange(2)
        rs.set_rgb_led_on(2)
    elif SONAR >= 11 and SONAR <= 15:
        rs.set_rgb_led_yellow(2)
        rs.set_rgb_led_on(2)
    elif SONAR >= 16 and SONAR <= 20:
        rs.set_rgb_led_green(2)
        rs.set_rgb_led_on(2)
    else:
        rs.set_rgb_led_off(2)
