import time


def swipe_page(driver,direction,number,during=0):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    for i in range(number):
        if direction == 'up':
            driver.swipe(x * 0.5, y * 0.8, x * 0.5, y * 0.2, during)
        elif direction == 'down':
            driver.swipe(x * 0.5, y * 0.2, x * 0.5, y * 0.8, during)
        elif direction == 'left':
            driver.swipe(x * 0.8, y * 0.5, x * 0.2, y * 0.5, during)
        elif direction == 'down':
            driver.swipe(x * 0.2, y * 0.5, x * 0.8, y * 0.5, during)
        time.sleep(1)

