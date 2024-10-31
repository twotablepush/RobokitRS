from RobokitRS import *
rs = RobokitRS.RobokitRS()
rs.port_open("com3")

rs.set_rgb_led_color(3, 100, 100, 100) # (포트번호, R, G, B), 흰색 출력
rs.set_rgb_led_on(3)
rs.delay(2)
rs.set_rgb_led_color(3, 100, 0, 0)
rs.delay(2)
rs.set_rgb_led_color(3, 0, 100, 0)
rs.delay(2)
rs.set_rgb_led_color(3, 0, 0, 100)
rs.delay(2)
rs.set_rgb_led_white(3) # 색을 직접 선택
rs.delay(2)
rs.set_rgb_led_red(3)
rs.delay(2)
rs.set_rgb_led_green(3)
rs.delay(2)
rs.set_rgb_led_sky(3)
rs.delay(2)
rs.set_rgb_led_brightness(3, 50) # 밝기 조절
rs.delay(2)
rs.set_rgb_led_brightness(3, 25)
rs.delay(2)
rs.set_rgb_led_off(3)