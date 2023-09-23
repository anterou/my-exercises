import time,webbrowser
def validator(func):
    def wrapper(url):
        if "." in url:
            time.sleep(2)
            func(url)
        else:
            print("Иди в очко")
    return wrapper
@validator
def open_url(url):
    webbrowser.open(url)
open_url("https://vk.com")