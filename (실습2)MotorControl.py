from RobokitRS import *
rs = RobokitRS.RobokitRS()
rs.port_open("/dev/tty.usbserial-0001")

rs.motor.write(0, 1, 15)
# 1. 모터 드라이브 보드에 연결된 포트 번호 (M1 = 0, M2 = 1, M3 = 2, M4 = 3)
# 2. 디렉션 값 (시계방향 = 1, 반시계방향 = 2)
# 3. 모터 속도 (0 ~ 15)
rs.delay(2)
rs.motor_stop(0)

rs.set_mecanumwheels_drive_front(15, 1) # 속도, 모터타입
rs.set_mecanumwheels_drive_left(15, 1)  # 왼쪽으로 이동
rs.set_mecanumwheels_rotate_left(15, 1) # 좌회전

rs.set_mecanumwheels_drive_frontleft(15, 1) # 왼쪽 대각선 이동
rs.set_mecanumwheels_drive_backright(15, 1)