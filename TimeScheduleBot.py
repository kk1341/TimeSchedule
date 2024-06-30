import discord
import json
import datetime
import calendar
from discord.ext import tasks

# 適宜TOKENとCHANNEL_IDを入れて動かす
TOKEN = None
CHANNEL_ID = None
client = discord.Client()

#$曜日(例:$Monday)と打たれた時にその曜日の時間割を出力
@client.event
async def on_message(message):
  if message.author.bot:
    return
  if message.content[:1] == '$':
    SendMessage = get_Schedule(message.content[1:])
    await message.channel.send(SendMessage)

#一分間ごとに現在の時間を取得し午前六時と午後の10時に時間割を出力
@tasks.loop(seconds = 60)
async def loop():
  now = datetime.datetime.now().strftime('%H:%M')
  if now == '06:00':
    weekDay = get_weekDay(0)
    sendTimeSchedule = get_Schedule(weekDay)
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('今日の日課はこれだよ！！' + '\n' + sendTimeSchedule)
  elif now == '22:00':
    weekDay = get_weekDay(1)
    sendTimeSchedule = get_Schedule(weekDay)
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('明日の日課はこれだよ！！' + '\n' + sendTimeSchedule)

# 入力された曜日の授業科目を出力
def get_Schedule(weekDay):
    data = load_JsonData()
    try:
      timeSchedule = data['TimeSchedule'][weekDay]
      sendTimeShedule = '\n'.join(timeSchedule)
    except KeyError:
      sendTimeShedule = 'コマンドが違うよ！！'
    return sendTimeShedule

# その日の曜日を返す
def get_weekDay(next_day):
  weekday = datetime.date.today().weekday() + next_day
  if weekday == 7:
    weekday = 0
  weekday_name = calendar.day_name[weekday]
  return weekday_name

# 授業科目が書いているJsonファイルを読み込む
def load_JsonData():
  timeschedule_file = open("TimeSchedule.json", "r", encoding="utf-8")
  timeschedule_data = json.load(timeschedule_file)
  return timeschedule_data


loop.start()
client.run(TOKEN)