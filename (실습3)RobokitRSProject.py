from RobokitRS import *
rs = RobokitRS.RobokitRS()
rs.port_open("com7")

rs.sonar_begin(11)  # 초음파 센서
rs.set_pin_mode(12, RobokitRS.Modes.INPUT)  # 우측 적외선 센서
rs.set_pin_mode(13, RobokitRS.Modes.INPUT)  # 좌측 적외선 센서

while(True):
    SONAR = rs.sonar_read(11)
    IL_R = rs.digital_read(12)
    IL_L = rs.digital_read(13)
    
    if SONAR < 20:
        rs.set_mecanumwheels_drive_stop(15, 1)  # 초음파로 물체가 20cm 이내일 때 정지
        rs.delay(1)  # 짧은 딜레이
    elif IL_R == 1:
        rs.set_mecanumwheels_drive_left(15, 1)  # 우측에 감지되면 좌측으로 회피
        rs.delay(1)
    elif IL_L == 1:
        rs.set_mecanumwheels_drive_right(15, 1)  # 좌측에 감지되면 우측으로 회피
        rs.delay(1)
    else:
        rs.set_mecanumwheels_drive_front(15, 1)  # 물체가 없으면 전진
