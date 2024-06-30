# TimeSchedule Bot for Discord
各曜日における学校の科目を出力するDiscordBot.
対応するJsonファイルを作ることで、好きなように学校の予定を出力することができる。

## Using
その日の06:00に今日の日課、22:00に明日の日課を通知する。
![ex_timebot](https://github.com/kk1341/TimeSchedule/assets/63755367/a4ddd6c8-0787-499a-8323-75483d0286d3)

以下のコマンドで、指定した曜日の日課を出力する。
```
$day_of_week
```

例.
```
$Monday
```

### Json File
このbotで使用できるJsonファイルの形式は以下の通りになる。
```json
{
    "TimeSchedule": {
        "Monday": [

        ],

        "Tuesday": [

        ],

        "Wednesday": [

        ],

        "Thursday": [

        ],

        "Friday": [

        ],

        "Saturday": [

        ],

        "Sunday": [
            
        ]
    }
}
```
