import json
import csv
import pandas as pd
import random
from linebot import LineBotApi
from linebot.models import TextSendMessage

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

file1 = open('info.json','r')
info = json.load(file1)
file2 = pd.read_csv(filepath_or_buffer="sample_data.csv", encoding="ms932", sep=",")

send_text = file2.values[random.randint(0, len(file2)-1),random.randint(1,len(file2.columns)-1)]

def main():
    USER_ID = info['USER_ID']
    messages = TextSendMessage(text = send_text)
    line_bot_api.push_message(USER_ID,messages)

if __name__ == "__main__":
    main()