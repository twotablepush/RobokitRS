import keyboard
from RobokitRS import *

rs = RobokitRS.RobokitRS()
rs.port_open("com3")

def move_front():
    rs.set_mecanumwheels_drive_front(15, 1)
    print("앞으로 이동 중...")

def move_back():
    rs.set_mecanumwheels_drive_back(15, 1)
    print("뒤로 이동 중...")

def move_right():
    rs.set_mecanumwheels_drive_right(15, 1)
    print("오른쪽으로 이동 중...")

def move_left():
    rs.set_mecanumwheels_drive_left(15, 1)
    print("왼쪽으로 이동 중...")

def move_frontright():
    rs.set_mecanumwheels_drive_frontright(15, 1)
    print("오른쪽 앞으로 이동 중...")

def move_frontleft():
    rs.set_mecanumwheels_drive_frontleft(15, 1)
    print("왼쪽 앞으로 이동 중...")

def move_backright():
    rs.set_mecanumwheels_drive_backright(15, 1)
    print("오른쪽 뒤로 이동 중...")

def move_backleft():
    rs.set_mecanumwheels_drive_backleft(15, 1)
    print("왼쪽 뒤로 이동 중...")

def turn_right():
    rs.set_mecanumwheels_rotate_right(15, 1)
    print("오른쪽으로 회전 중...")

def turn_left():
    rs.set_mecanumwheels_rotate_left(15, 1)
    print("왼쪽으로 회전 중...")

def stop():
    rs.set_mecanumwheels_drive_stop(1)
    print("모터 정지.")

keyboard.add_hotkey('w', move_front)
keyboard.add_hotkey('x', move_back)
keyboard.add_hotkey('d', move_right)
keyboard.add_hotkey('a', move_left)
keyboard.add_hotkey('e', move_frontright)
keyboard.add_hotkey('q', move_frontleft)
keyboard.add_hotkey('c', move_backright)
keyboard.add_hotkey('z', move_backleft)
keyboard.add_hotkey('right', turn_right)
keyboard.add_hotkey('left', turn_left)
keyboard.add_hotkey('s', stop)

print("                                 키보드로 모터를 제어하세요.")
print("          Q : 왼쪽 대각선 앞              W : 앞              E : 오른족 대각선 앞")
print("          A : 왼쪽                        S : 정지            D : 오른쪽")
print("          Z : 왼쪽 대각선 뒤              X : 뒤              C : 왼쪽 대각선 뒤")
print("왼쪽 화살표 : 왼쪽으로 회전                       오른쪽 화살표 : 오른쪽으로 회전")