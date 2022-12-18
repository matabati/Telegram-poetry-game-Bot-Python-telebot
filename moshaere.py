import telebot
import time
import sys
from telebot import types
import random


gameflag = 0
memberflag = 0
members = []
wait = 1
num = 0
n = "\n".encode("utf")
score = []
turn = 120
alphabets = ['ا','ب','پ','ت','ث','ج','چ','ح','خ','د','ذ','ر','ژ','ز','س','ش','ص','ض','ط','ظ','ع','غ','ف','ق','ک','گ','ل','م','ن','و','ه','ی']
alphabet = ""
end = 0
want_ans = 0
menu = ['Start a new game','Force start','Join game','Force stop','Rules','Members']

bot_token = "///"

bot = telebot.TeleBot(bot_token)

def find_at(msg):
    for text in msg:
        if 'a' in text:
            return text

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    global n

    text = " سلام و صد سلام به گلای تو خونه، جیگرطلاهای نمونه! 😍"
    text0 =  " همون طوری که در جریانید همه چیز از اونجایی شروع شد که من به اشتباه با ملیکا دوست شدم و در جواب اینکه دلش یه ربات مشاعره میخواند که اگه گفت ت بده و تو نوشتی:"
    text1 =   " ترثبخصاثبخصابخصثابمثابصثابمصا حافظا!"
    text2 = " نگه آفرین کلک 😜 حالا وقتشه من با الف بگم! 😜"
    text3 = " - توهین نباشه به دوستان عزیز ربات ساز البته! من برای این ربات سرورم نمیخرم حتی 😂 هیچ ادعایی ندارم 😂 -"
    text4 = " من در جواب ملیکا اظهار کردم کار راحتیه و گفتم:"

    bot.reply_to(message,text.encode("utf-8"))
    time.sleep(2)
    bot.send_message(chat_id=message.chat.id,text=text0.encode("utf-8")+n+text1.encode("utf-8")+n+text2.encode("utf-8")+n+text3.encode("utf-8")+n+text4.encode("utf-8"))
    time.sleep(16)

    bot.send_animation(chat_id=message.chat.id, animation='https://external-preview.redd.it/TiRpif4KkJ8MBbrvxfN480u2g0oaTIoZ2ItyjCiL5Zo.gif?format=mp4&s=9c710637bcffbbdf9c41b8f186fc157bd8b81edf')
    text5 = "که به گور خودم خندیدم :|"
    text6 = " القصه برای بازی کردن با رباتم به من تک بزنید اگه آنلاین نیستم تا رانش کنم و شانس بیارید خواب نباشم 😌 مگرنه رباتتون میکنم :| حالام برید :| چخه :| بای :|"
    time.sleep(2)
    bot.send_message(chat_id=message.chat.id,text=text5.encode("utf-8"))
    time.sleep(2)
    bot.send_message(chat_id=message.chat.id,text=text6.encode("utf-8"))


@bot.message_handler(commands = ['moshaere'])
def send_game(message):
    text = "لتس پلی عه گیم 😈 شما تا الی ماشالله وقت دارید عضو شید 😈 اگه خواستید بازی رو شروع کنید فورس استارت رو بزنید و قطعا باید دوتا باشید حداقل 😐 چون من معطل شماها نبودم عمرمو بذارم پای این دلقک که بخواید با خودتون مشاعره کنید 😐"
    markup = types.ReplyKeyboardMarkup()
    start = types.KeyboardButton('Start a new game')
    fStart = types.KeyboardButton('Force start')
    join = types.KeyboardButton('Join game')
    fStop = types.KeyboardButton('Force stop')
    rules = types.KeyboardButton('Rules')
    members = types.KeyboardButton('Members')
    markup.add(start, join)
    markup.add(fStop,fStart)
    markup.add(rules, members)
    if gameflag==0:
        bot.send_message(chat_id=message.chat.id,text=text.encode("utf-8"),reply_markup=markup,parse_mode='markdown')

@bot.message_handler(commands = ['force_stop'])
def stop1(message):
    global wait
    global end
    global gameflag
    global members
    global score
    if gameflag==1:
        end = 1
        wait = 0
        gameflag = 0
        members.clear()
        score.clear()
        bot.send_message(chat_id=message.chat.id, text="اوکی بای :|".encode("utf-8"))
    else:
        bot.send_message(chat_id=message.chat.id, text="بازی ای در جریان نیست.".encode("utf-8"))

@bot.message_handler(func=lambda message: message.text == 'Force stop' and message.content_type == 'text')
def stop(message):
    global wait
    global end
    global gameflag
    global members
    global score
    if gameflag == 1:
        end = 1
        wait = 0
        gameflag = 0
        members.clear()
        score.clear()
        bot.send_message(chat_id=message.chat.id, text="اوکی بای :|".encode("utf-8"))
    else:
        bot.send_message(chat_id=message.chat.id, text="بازی ای در جریان نیست.".encode("utf-8"))


@bot.message_handler(func=lambda message: message.text not in menu, content_types=['text'])
def answer(message):
    global members
    global num
    global alphabet
    global score
    global want_ans

    if want_ans == 1:

        if message.from_user.username==members[num]:
            if message.text[0]==alphabet:
                bot.send_message(chat_id=message.chat.id, text =str(members[num]).encode("utf")+" بابا دمت گرم! ما به شما یک امتیاز میدهیم! 😎".encode("utf-8"))
                score[num] = score[num] + 1
                alphabet = message.text[-1]

            else:
               bot.send_message(chat_id=message.chat.id, text=str(members[num]).encode("utf")+" این چی بود؟! ما از شما یک امتیاز کم میکنیم تا درست شی! 😐 ".encode("utf-8"))
               score[num] = score[num] - 1

        want_ans = 0

@bot.message_handler(func=lambda message: message.text == 'Force start' and message.content_type == 'text')
def force_start(message):
    global wait
    wait = 0

@bot.message_handler(func=lambda message: message.text == 'Start a new game' and message.content_type == 'text')
def start(message):
    global gameflag
    global members
    global wait
    global end
    global alphabets
    global alphabet
    global num
    global want_ans

    temp = 0

    if gameflag == 1 :
        bot.send_message(chat_id=message.chat.id , text = "نمیتونین باز یه بازی جدید شروع کنید!".encode("utf-8"))
    else:
        gameflag = 1
        bot.send_message(chat_id=message.chat.id, text = "بازی جدید شروع شدش جیگرطلاها!".encode("utf-8"))
        while wait == 1:
             time.sleep(1)

        wait = 1

        if end == 1:
            end = 0

        elif end == 0 and gameflag == 1:
            if len(members)<2:
                bot.send_message(chat_id = message.chat.id , text = "تعدادتون کافی نیست نفله ها :|".encode("utf-8"))
                gameflag = 0
                members.clear()
                score.clear()

            else:
                cycle = 8
                if len(members)>5:
                    cycle = 10
                while end == 0 and wait == 1 and cycle>0:

                    num = random.randint(0,len(members)-1)
                    if alphabet=="":
                        alphabet = alphabets[random.randint(0,len(alphabets)-1)]
                    markup = types.ForceReply(selective=True)
                    bot.send_message(chat_id=message.chat.id,
                                     text=str("@" + str(members[num])).encode("utf") + " نوبت توعه تا ".encode(
                                         "utf-8") + str("(" + alphabet + ")").encode("utf-8") + " بیای!😌".encode(
                                         "utf-8") + "\n".encode(
                                         "utf"), reply_markup=markup)

                    want_ans = 1

                    while end == 0 and temp<24 and want_ans==1:
                        time.sleep(5)
                        temp = temp + 1
                    temp = 0

                    if want_ans == 1 and end!=1:
                        bot.send_message(chat_id=message.chat.id, text="خب هیچ جوابی به من ندادین! =((( ".encode("utf-8"))
                        score[num] = score[num] - 1

                    cycle = cycle - 1

                if end!= 1 :
                    text0 = ""
                    for i in range(len(members)):
                          text0 = text0 + "\n" + str(members[i])+ " -> " + str(score[i])

                    bot.send_message(chat_id=message.chat.id, text="آل رایت آل رایت آل رایت! 😎".encode("utf-8")+"\n".encode("utf")+"وقت اعلام نتایجه!💃🏻💃🏻💃🏻".encode("utf-8")+text0.encode("utf"))
                
                    text0 = ""

                    print(max(score))

                    max0 = max(score)
                    max1 = max0
                    while max0 == max1:
                        for s in score:
                            print(s)
                        for m in members:
                            print(m)
                        text0 = text0 +"\n 🥇"+ str(members[score.index(max1)])
                        del members[score.index(max0)]
                        del score[score.index(max0)]
                        if len(score)!=0:
                            max1 = max(score)
                        else:
                            break;

                    bot.send_message(chat_id = message.chat.id , text = "و برنده بین شما نوب سگا کسی نیست جززززز 🥁🥁🥁🥁🥁 ".encode("utf-8")+text0.encode("utf"))
                    bot.send_animation(chat_id=message.chat.id,animation='https://media2.giphy.com/media/8m4R4pvViWtRzbloJ1/giphy.gif?cid=ecf05e47dd3db963f020c9077262b8a4eaeae7b5d69ef46b&rid=giphy.gif')
                    gameflag = 0
                    end = 0
                    wait = 1
                    score.clear()
                    members.clear()
                elif end == 1:
                    want_ans = 0

@bot.message_handler(func=lambda message: message.text == 'Members' and message.content_type == 'text')
def members_names(message):
    global gameflag
    global members

    text0 = ""
    if gameflag == 1:
        for m in members:
            text0 = text0 + "\n" + m

        bot.send_message(chat_id = message.chat.id , text = "اشخاصی که تا به این لحظه جوین شدند:".encode("utf-8")+text0.encode("utf"))


@bot.message_handler(func=lambda message: message.text == 'Rules' and message.content_type == 'text')
def rules(message):
    bot.send_message(chat_id = message.chat.id , text = "قوانین ساده اند:".encode("utf-8")+"\n".encode("utf")+"۱- شما دو دقیقه وقت دارید که جواب خودتونو ارسال کنید!".encode("utf-8")+"\n".encode("utf")+"۲- بهتره اولین پاسخی که بعد از پیام ربات میدید جوابتون به سوال باشه!".encode("utf-8")+"\n".encode("utf")+"۳- و شاید من نفهمم که دارید تقلب میکنید اما خدا میفهمه -____- با وجدان بازی کنید!".encode("utf-8"))
    bot.send_animation(chat_id=message.chat.id,animation='https://media.giphy.com/media/Yl8pfUmelpZMA/giphy.gif')



@bot.message_handler(func=lambda message: message.text == 'Join game' and message.content_type == 'text')
def join(message):
    global gameflag
    global members
    global score
    if gameflag == 1 :
        username = message.from_user.username
        if username not in members:
            bot.send_message(chat_id=message.chat.id, text = str("@"+str(username)).encode("utf") + " عضو شد".encode("utf-8") )
            members.append(username)
            score.append(0)

    else:
        bot.send_message(chat_id = message.chat.id , text = "بازی ای برای عضو شدن در جریان نیست.".encode("utf-8"))



@bot.message_handler(commands= ['barney'])
def send_barney(message):
    bot.send_animation(chat_id=message.chat.id,animation='https://i.imgur.com/H48hPCk.gif')

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
