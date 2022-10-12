try:
    from toast import ToastNotifier
except ModuleNotFoundError:
    import sys

    sys.exit("Use the command \"pip install win10toast\" in Command Prompt/Powershell to use notify.py")


def pop_up(source_text, target_text):
    """Generates Pop-up notification when state changes"""
    notification = ToastNotifier()
    notification.show_toast(source_text, target_text, icon_path=None, duration=5)

