import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import telegram
import base64

api_id = '1569056'
api_hash = 'c3defffabfb1cd518070ba9d16bc46f7'
token = '1342187492:AAE0AhND59AsKuS7RQqTT3vJ0wyrNOkmGrA'

chatId = -494212497

bot = telegram.Bot(token)

# bot.deleteWebhook()

def image_to_data_url(filename):
    ext = filename.split('.')[-1]
    prefix = f'data:image/{ext};base64,'
    with open(filename, 'rb') as f:
        img = f.read()
    return prefix + base64.b64encode(img).decode('utf-8')

if bot.get_updates():
    if bot.get_updates()[-1].message.chat_id:
        chatId = bot.get_updates()[-1].message.chat_id

class Watcher:
    DIRECTORY_TO_WATCH = "../"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            try:
                time.sleep(1)
                bot.send_photo(chat_id=chatId, photo=open(event.src_path, 'rb'))
                print("sended")
            except:
                print("failed")



if __name__ == '__main__':
    w = Watcher()
    w.run()
