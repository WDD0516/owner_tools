import sys

sys.path.append('D:\\Project\\Py\\owner_tools')

import json
import logging
import win32con
from threading import activeCount, enumerate
from easyTranslate.translate import get_trans
from listening_hotkey import Hotkey


def main():
    f = open('conf/conf.json', encoding='utf-8')
    conf = json.load(f)
    ak = conf['AccessKey ID']
    sk = conf['AccessKey Secret']
    logging.basicConfig(filename='log/tools.log', filemode='w', level=logging.DEBUG,
                        format='%(levelname)s:%(asctime)s %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
    hotkey = Hotkey()
    # hotkey.reg(key=(win32con.MOD_CONTROL, 189), func=copy_checked)  # test
    hotkey.reg(key=(win32con.MOD_CONTROL, 189), func=get_trans, args=(ak, sk, 'c2e'))  # ctrl - 中译英
    hotkey.reg(key=(win32con.MOD_CONTROL, 187), func=get_trans, args=(ak, sk, 'e2c'))  # ctrl = 英译中
    # hotkey.reg(key=(win32con.MOD_ALT, win32con.VK_F9), func=lambda: print('激活热键'), args=None)

    hotkey.start()  # 启动热键主线程
    logging.debug('-----begin')
    logging.info(f'当前线程列表:{activeCount()}' + str(enumerate()))


if __name__ == '__main__':
    main()
