import logging

import pyperclip
from pynput import keyboard
import time
import re
from notify_trans import pop_up
from threading import activeCount, enumerate
from ali_trans import TransApi


def copy_checked():  # 复制选中的文本
    control = keyboard.Controller()  # 定义键盘控制的类
    time.sleep(0.1)
    with control.pressed(keyboard.Key.ctrl):  # 发送组合键
        control.press('c')
        control.release('c')
    time.sleep(0.1)


def get_clipboard():
    return pyperclip.paste()  # 获取剪切板


class Translate:
    clipboard_text = ''
    AccessKeyID = ''
    AccessKeySecret = ''

    def __init__(self, ak, sk):
        copy_checked()
        self.clipboard_text = get_clipboard()
        self.AccessKeyID = ak
        self.AccessKeySecret = sk

    def is_en(self):
        my_re = re.compile(r'[A-Za-z]', re.S)
        res = re.findall(my_re, self.clipboard_text)
        return bool(len(res))

    def is_cn(self):
        for _char in self.clipboard_text:
            if '\u4e00' <= _char <= '\u9fa5':
                return True
        return False

    def trans(self, mode):
        if (mode == 'c2e' and not self.is_cn) or (mode == 'e2c' and not self.is_en):
            warning = '该文本不包含中文' if mode == 'c2e' else '该文本不包含英文'
            logging.warning(self.clipboard_text + warning)
            pop_up(self.clipboard_text, warning)
        elif mode == 'c2e' or mode == 'e2c':
            target_text = TransApi.get_result(self.AccessKeyID, self.AccessKeySecret, mode, self.clipboard_text)

            logging.debug(f'{self.clipboard_text} -> {target_text}')
            pop_up(self.clipboard_text, target_text)
        else:
            logging.warning('mode有误')


def get_trans(ak, sk, mode):
    t = Translate(ak, sk)
    t.trans(mode)
    time.sleep(1)
    logging.info(f'当前线程列表:{activeCount()}'+str(enumerate()))
