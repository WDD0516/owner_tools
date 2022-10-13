import threading


#
# try:
#     from toast import ToastNotifier
# except ModuleNotFoundError:
#     import sys
#
#     sys.exit("Use the command \"pip install win10toast\" in Command Prompt/Powershell to use notify.py")
#
#
# def pop_up(source_text, target_text):
#     """Generates Pop-up notification when state changes"""
#     notification = ToastNotifier()
#     notification.show_toast(source_text, target_text, icon_path='image/Bugs Bunny.ico', duration=5)

# 以上调用操作系统通知栏如下问题，暂未有解决方案，更换调用plyer以及其他通知包,仍然会出现这个问题
# pywintypes.error: (-2147467259, 'Shell_NotifyIcon', '未指定的错误')
def pop_up(source_text, target_text):
    from plyer import notification
    notification.notify(title=source_text,
                        message=target_text,
                        app_icon='image\\Bugs Bunny.ico',
                        timeout=5
                        )


if __name__ == '__main__':
    t1 = threading.Thread(target=pop_up, args=('123', '456'))
    t1.start()
