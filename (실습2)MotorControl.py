from RobokitRS import *
rs = RobokitRS.RobokitRS()
rs.port_open("com3")

# 앞으로 가기
rs.motor_write(0, 1, 15) # (포트번호(m1 = 0, m2 =1), 회전방향(시계방향 = 1, 반시계방향 = 2), 모터 속도(0 ~ 15))
rs.motor_write(1, 0, 15)
rs.motor_write(2, 1, 15)
rs.motor_write(3, 0, 15)
rs.delay(2)
rs.motor_stop(0)
rs.motor_stop(1)
rs.motor_stop(2)
rs.motor_stop(3)

rs.set_mecanumwheels_drive_front(15, 1)
rs.delay(2)
rs.set_mecanumwheels_drive_right(15, 1)
rs.delay(2)
rs.set_mecanumwheels_drive_back(15, 1)
rs.delay(2)
rs.set_mecanumwheels_drive_left(15, 1)
rs.delay(2)
rs.set_mecanumwheels_drive_stop(15, 1)