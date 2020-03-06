from pathlib import Path
import os

class UBotRunner:

    @staticmethod
    def run(account, test):
        # UBot spyder initialization
        print("Running ubot spyder...")
        home_path = str(Path.home())
        ubot_spyder_path = '/InstaPy/ubot-spyder/ubot/ubot_spyder.py'
        ubot_spyder_command = "python3 " + home_path + ubot_spyder_path + " " + account + " " + str(test)
        print(ubot_spyder_command)
            
        os.system(ubot_spyder_command)