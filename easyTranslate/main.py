import logging
import win32con
from threading import activeCount, enumerate
from easyTranslate.translate import get_trans
from listening_hotkey import Hotkey


def main(ak, sk):
    logging.basicConfig(filename='log/tools.log', level=logging.DEBUG,
                        format='%(levelname)s:%(asctime)s %(message)s', datefmt='%Y/%m/%d %I:%M:%S %p')
    hotkey = Hotkey()
    hotkey.reg(key=(win32con.MOD_ALT, win32con.VK_F9), func=get_trans, args=(ak, sk, 'c2e'))  # alt f9 中译英
    hotkey.reg(key=(win32con.MOD_ALT, win32con.VK_F10), func=get_trans, args=(ak, sk, 'e2c'))  # alt f10 英译中
    # hotkey.reg(key=(win32con.MOD_ALT, win32con.VK_F9), func=lambda: print('激活热键'), args=None)
    hotkey.start()  # 启动热键主线程
    logging.info(f'当前线程列表:{activeCount()}' + str(enumerate()))


if __name__ == '__main__':
    main('ak','sk')
