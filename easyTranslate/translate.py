import logging

import pyperclip
import win32api
import win32con
from pynput import keyboard
import time
import re
from notify_trans import pop_up
from threading import activeCount, enumerate
from ali_trans import TransApi


def copy_checked():  # 复制选中的文本
    win32api.keybd_event(17, 0, 0, 0)
    win32api.keybd_event(67, 0, 0, 0)
    win32api.keybd_event(67, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.05)

    # control = keyboard.Controller()  # 定义键盘控制的类
    # time.sleep(0.1)
    # with control.pressed(keyboard.Key.ctrl_r):  # 发送组合键
    #     control.press('c')
    #     control.release('c')
    # with control.pressed(keyboard.Key.ctrl, 'c'): logging.debug('触发ctrl+c')


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
            pop_up('warn', warning)
        elif mode == 'c2e' or mode == 'e2c':
            target_text = TransApi.get_result(self.AccessKeyID, self.AccessKeySecret, mode, self.clipboard_text)
            pyperclip.copy(target_text)
            logging.debug(f'{self.clipboard_text} -> {target_text}')
            try:
                pop_up(mode+'翻译结果', target_text)
            except Exception as e:
                # 如有需要，请打印 error
                logging.error(e)
        else:
            logging.warning('mode有误')


def get_trans(ak, sk, mode):
    t = Translate(ak, sk)
    t.trans(mode)
