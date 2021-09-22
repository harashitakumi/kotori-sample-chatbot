#jsonファイル  情報読み込み
import json
file = open("info.json", "r")
info = json.load(file)

#ボット作成
from linebot import LineBotApi
from linebot.models import TextSendMessage

#指定したチャンネルを今から使いますという宣言
CHANNEL_ACCESS_TOKEN = info["CHANNEL_ACCESS_TOKEN"]
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    #どのユーザーに送るのか
    USER_ID = info["USER_ID"]
    #どのメッセージを
    messages = TextSendMessage(text = "おはようちゅん！！\n 今日も１日頑張るちゅん！！")
    #メッセージをユーザーに送る
    line_bot_api.push_message(USER_ID, messages = messages)

if __name__ == "__main__":
    main()
