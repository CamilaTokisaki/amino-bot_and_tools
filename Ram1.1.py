import threading
import random
import aminofix
import time

from threading import Thread
from gtts import gTTS


if __name__ == "__main__":




    translator = "ru" # ru - Русская Ram
                      # en - English Ram



    chat_information = {}
    client = aminofix.Client(); methods = []
    client.login(email="here's your login", password="Here's your password")
    sub_client = aminofix.SubClient(comId="and here's your amino ID", profile=client.profile)
    reloadTime = time.time() + 170
    if translator == "ru":
        print(f"Я стартовала на аккаунте: {sub_client.profile.nickname}")
    elif translator == "en":
        print(f"I started on the account: {sub_client.profile.nickname}")
    ban = 0
    tim = 1
    hm = [0]
    av = []
    nom = 0

def on_message(data: aminofix.objects.Event):
    global ban
    global tim
    global nom
       
    chatId = data.message.chatId
    nickname = data.message.author.nickname
    content = data.message.content
    id = data.message.messageId
    title: str = client.get_community_info(data.comId).name
    userId: str = data.message.author.userId
      
    if not content: content = "None"
    
    lis = ['Думаю, что да', 'Думаю, что нет', 'Наверное', 'Уверена на все 100%', 'Точно нет', 'Да, почему бы и нет?', 'Скорее всего да, а хотя, может и нет...', 
    'Я не знаю ответа на этот вопрос, я глупая', 'Почему ты так думаешь?', 'Я не уверена что тебе стоит знать ответ на твой вопрос','Нет','Да']

    lis2 = ['*обняла в ответ* мне приятно что ты заботишься о мне~', 'Ня~ Как приятно~', '*обняла в ответ* Не отпускай меня...',
    '*обняла в ответ* Можно нам так стоять вместе вечно?..', '*обняла в ответ* Я люблю тебя..', '*обняла в ответ* :3', '*обняла в ответ* я счастлива~']

    lis3 = ['Привет', "Здравствуй", "hola mi amigo", "Привет, зая", "Мур-Мур~", "Да-да, это я"]

    lisen = ['I think so, yes.', "I don't think so", 'Probably', "I'm 100% sure of it", 'Absolutely not.', 'Yeah, why not?', 'Most likely yes, but maybe not...', 
    "I don't know the answer to that question, I'm stupid", 'What makes you think that?', "I'm not sure you should know the answer to your question", 'No', 'Yes']

    lis2en = ["*hugged me back* I'm glad you care about me~", 'Nyah~ How nice~', "*Hugged me back* Don't let me go...",
    '*Hugged back* Can we stand like this together forever?', '*hugged back* I love you...', '*hugged back* :3', "*hugged back* I'm happy~"]

    lis3en = ['Hi', 'Hello', 'hola mi amigo', 'Hi, poochie', 'Mur-Mur~', "Yes, yes, it's me"]

    print(nickname, content, title)

    if content.lower().startswith("команды") or content.lower().startswith("помощь") or content.lower().startswith("help"):
        if translator == "ru":
            sub_client.send_message(message="""
[B]Команды:

Люблю - Покажите Рам свою любовь!
Рам - Поздоровайтесь с Рам!
Действия - Взаимодействия с участниками
*обнял* или *обняла* - обнять Рам!
Вопрос, - спроси у Рам что- либо!
Гс - Попроси Рам записать голсовое сообщение!
Любовь - узнай вероятность любви между людьми
АдПанель - админская панель
Инфо - информация профиля
Создательница - О создателе Рам
Информация - список обновления Рам!
""",chatId=chatId)
        elif translator == "en":
            sub_client.send_message(message="""
[B]Commands:

Love - Show Ram your love!
Ram - Say hello to Ram!
Actions - Interactions with participants
*hugged* - hug Ram!
Question - Ask Ram anything!
Gs - Ask Ram to write down a voice message!
Lovers - Find out the possibility of love between people.
AdPanel - admin panel.
Info - Profile Info.
Creator - About Ram's Creator!
Information - Ram's update list!
""",chatId=chatId)


    if content.lower().startswith("рам") or content.lower().startswith("ram"):
        if translator == "ru":
            sub_client.send_message(message=str(random.choice(lis3)), chatId=chatId, replyTo=id)
        elif translator == "en":
            sub_client.send_message(message=str(random.choice(lis3en)), chatId=chatId, replyTo=id)

    if content.lower().startswith("онлайн") or content.lower().startswith("online"):
        if data.message.author.role != 0:
            if translator == "ru":
                sub_client.activity_status('online')
                sub_client.send_message(message="Я в сети!", chatId=chatId)
            elif translator == "en":
                sub_client.activity_status('online')
                sub_client.send_message(message="I'm online", chatId=chatId)
        elif not data.message.author.role != 0:
            if translator == "ru":
                sub_client.send_message(message="Прости, но у меня или у тебя нет прав на выполнения этой команды", chatId=chatId)
            elif translator == "en":
                sub_client.send_message(message="I'm sorry, but I or you do not have the authority to execute this command", chatId=chatId)

    if content.lower().startswith("оффлайн") or content.lower().startswith("offline"):
        if data.message.author.role != 0:
            if translator == "ru":   
                sub_client.activity_status('offline')
                sub_client.send_message(message="Я вне сети!", chatId=chatId)
            elif translator == "en":
                sub_client.activity_status('offline')
                sub_client.send_message(message="I'm offline!", chatId=chatId)
        elif not data.message.author.role != 0:
            if translator == "ru":
                sub_client.send_message(message="Прости, но у меня или у тебя нет прав на выполнения этой команды", chatId=chatId)
            elif translator == "en":
                sub_client.send_message(message="I'm sorry, but I or you do not have the authority to execute this command", chatId=chatId)

    if content.lower().startswith("вопрос,") or content.lower().startswith("question,"):
        if translator == "ru":
            sub_client.send_message(message=str(random.choice(lis)), chatId=chatId, replyTo=id)
        elif translator == "en":
            sub_client.send_message(message=str(random.choice(lisen)), chatId=chatId, replyTo=id)

    if content.lower().startswith("люблю") or content.lower().startswith("love"):
        if translator == "ru":
            sub_client.send_message(message="Я тоже тебя люблю", chatId=chatId, replyTo=id)
        elif translator == "en":
            sub_client.send_message(message="I love you too", chatId=chatId, replyTo=id)

    if content.lower().startswith("lovers") or content.lower().startswith("любовь"):
        mentions = data.message.extensions.get('mentionedArray')
        if mentions != None and len(mentions) == 2:
            pidorasi = [sub_client.get_user_info(x['uid']).nickname for x in mentions]
            if translator == "ru":
                sub_client.send_message(
                    message=f"Вероятность того, что {pidorasi[0]} и {pidorasi[1]} любят друг друга равно {random.randint(0, 100)}%",
                    chatId=chatId)
            elif translator == "en":
                sub_client.send_message(
                    message=f"The probability that  {pidorasi[0]} and {pidorasi[1]} love each other: {random.randint(0, 100)}%",
                    chatId=chatId)

    if content.lower().startswith("*обнял*") or content.lower().startswith("*обняла*") or content.lower().startswith("*hugged*"):
        if translator == "ru":
            sub_client.send_message(message=str(random.choice(lis2)), chatId=chatId, replyTo=id)
        elif translator == "en":
            sub_client.send_message(message=str(random.choice(lis2en)), chatId=chatId, replyTo=id)

    if content.lower().startswith("информация") or content.lower().startswith("information"):
        if translator == "ru":
            sub_client.send_message(message='''
[B]Обновления: 1.1.1

==Изменения:==
-Полный перенос Рам на условно новую библиотеку, дважды))
-Сделаны мини исправления

==Удалено:==
-Старая бибилиотека бота, тоже дважды)
''', chatId=chatId)
        elif translator == "en":
            sub_client.send_message(message='''
[B]Update: 1.1.1

This is the biggest update since the creation of Ram!

==Changes:==
-Full transfer of Ram to a conditional new library, twice))


==Removed:==
-Old bot bibliography, also twice)
-Minimum corrections have been made
''', chatId=chatId)

    if content.lower().startswith("создательница") or content.lower().startswith("creator"):
        if translator == "ru":
            sub_client.send_message(message='''
Версия бота 1.1.1

==Создательница:==
Дискорд - CamilaTokisaki#5351
Телеграмм - @CamilaTokisaki
github - https://github.com/CamilaTokisaki
Почта - camilatokisakideveloper@gmail.com

==Особая благодарность:==
WildNightFox - За помощь с переносом библиотеки и доп командой
Его дискорд: WildNightFox#9154

И всё, больше я никому не благодарна :3
''', chatId=chatId)
        elif translator == "en":
            sub_client.send_message(message='''
Bot version 1.1.1

==Creator:==
Discord - CamilaTokisaki#5351
Telegram - @CamilaTokisaki
github - https://github.com/CamilaTokisaki
E-mail - camilatokisakideveloper@gmail.com

==Special thanks:==
WildNightFox - For help with migrating the library and adding commands
His discord: WildNightFox#9154

And that's it, I'm not grateful to anyone else :3
''', chatId=chatId)

    if content.lower().startswith("действия") or content.lower().startswith("actions"):
        if translator == "ru":
            sub_client.send_message(message='''
[B]Действия:

щекочет - Прижаться
кормит - Покормить
обнимает - Обнять
целует - Поцеловать
гладит - Погладить
тыкает - Тыкнуть
бьёт - ударить
щекочет - Пощекотать
кусает - делать кусь
''', chatId=chatId)

        elif translator == "en":
            sub_client.send_message(message='''
[B]Actions:

cuddle - Cuddle up
feed - feed
hug - Hug
kiss - Kiss
pat - Stroke
poke - Poke
slap - slap
tickle - Tickle
kus - give a bite
''', chatId=chatId)

    if content.lower().startswith("tickle") or content.lower().startswith("щекочет"):
        author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
        if translator == "ru":
            sub_client.send_message(message=f'{data.message.author.nickname} щекочет {author2}', chatId=chatId)
        elif translator == "en":
            sub_client.send_message(message=f'{data.message.author.nickname} tickles {author2}', chatId=chatId)

    if content.lower().startswith("slap") or content.lower().startswith("бьёт"):
        author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
        if translator == "ru":
            sub_client.send_message(message=f'{data.message.author.nickname} бьёт {author2}', chatId=chatId)
        elif translator == "en":
            sub_client.send_message(message=f'{data.message.author.nickname} beats {author2}', chatId=chatId)

    if content.lower().startswith("poke") or content.lower().startswith("тыкает"):    
        author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
        if translator == "ru":
            sub_client.send_message(message=f'{data.message.author.nickname} тыкает в {author2}', chatId=chatId)
        elif translator == "en":
            sub_client.send_message(message=f'{data.message.author.nickname} pokes at {author2}', chatId=chatId)

    if content.lower().startswith("pat") or content.lower().startswith("гладит"):
        author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
        if translator == "ru":
            sub_client.send_message(message=f'{data.message.author.nickname} гладит {author2}', chatId=chatId)
        elif translator == "en":
            sub_client.send_message(message=f'{data.message.author.nickname} gently strokes {author2}', chatId=chatId)

    if content.lower().startswith("hug") or content.lower().startswith("обнимает"):
        author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
        if translator == "ru":
            sub_client.send_message(message=f'{data.message.author.nickname} обнимает {author2}', chatId=chatId)
        elif translator == "en":
            sub_client.send_message(message=f'{data.message.author.nickname} hugs {author2}', chatId=chatId)

    if content.lower().startswith("feed") or content.lower().startswith("кормит"):
        author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
        if translator == "ru":
            sub_client.send_message(message=f'{data.message.author.nickname} кормит {author2}', chatId=chatId)
        elif translator == "en":
            sub_client.send_message(message=f'{data.message.author.nickname} feeds {author2}', chatId=chatId)

    if content.lower().startswith("cuddle") or content.lower().startswith("прижимается"):
        author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
        if translator == "ru":
            sub_client.send_message(message=f'{data.message.author.nickname} прижимается к {author2}', chatId=chatId)
        elif translator == "en":
            sub_client.send_message(message=f'{data.message.author.nickname} snuggles up to {author2}', chatId=chatId)

    if content.lower().startswith("kiss") or content.lower().startswith("целует"):
        author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
        if translator == "ru":
            sub_client.send_message(message=f'{data.message.author.nickname} целует {author2}', chatId=chatId)
        elif translator == "en":
            sub_client.send_message(message=f'{data.message.author.nickname} kisses {author2}', chatId=chatId)

    if content.lower().startswith("kus") or content.lower().startswith("кусает"):
        author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
        if translator == "ru":
            sub_client.send_message(message=f'{data.message.author.nickname} делает кусь {author2}', chatId=chatId)
        elif translator == "en":
            sub_client.send_message(message=f'{data.message.author.nickname} makes a kus {author2}', chatId=chatId)

    if content.lower().startswith("инфо") or content.lower().startswith("info"):
        repa=sub_client.get_user_info(userId=userId).reputation
        lvl = sub_client.get_user_info(userId=userId).level
        crttime = sub_client.get_user_info(userId=userId).createdTime[0:10]
        followers = sub_client.get_user_achievements(userId=userId).numberOfFollowersCount
        profilchange = sub_client.get_user_info(userId=userId).modifiedTime[0:10]
        commentz = sub_client.get_user_info(userId=userId).commentsCount
        posts = sub_client.get_user_achievements(userId=userId).numberOfPostsCreated
        followed = sub_client.get_user_info(userId=userId).followingCount
        if translator == "ru":
            sub_client.send_message(chatId=data.message.chatId, message=f"""
Никнейм: {nickname}
Дата Создания Аккаунта: {crttime}
Последний раз профиль изменялся: {profilchange}
Количество Репутации: {repa}
Уровень Аккаунта: {lvl}
Количество постов созданных в профиле: {posts}
Количество комментариев на стене профиля: {commentz}
Количество людей на которых вы подписаны: {followed}
Подписчики аккаунта: {followers}
	""")
        elif translator == "en":
            sub_client.send_message(chatId=data.message.chatId, message=f"""
Nickname: {nickname}
Account Creation Date: {crttime}
The last time the profile was changed: {profilchange}
Number of Reputation: {repa}
Account Level: {lvl}
Number of posts created in the profile: {posts}
Number of comments on the profile wall: {comments}
The number of people you are subscribed to: {followed}
Account subscribers: {followers}
	""")            

    if content.lower().startswith("гс") or content.lower().startswith("gs"):
        if translator == "ru":
            myobj = gTTS(text=data.message.content[4:], lang='ru', slow=False)
            myobj.save("gs.mp3")
            with open("gs.mp3", "rb") as file:
                sub_client.send_message(chatId=chatId, file=file, fileType="audio")
        elif translator == "en":
            myobj = gTTS(text=data.message.content[4:], lang='en', slow=False)
            myobj.save("gs.mp3")
            with open("gs.mp3", "rb") as file:
                sub_client.send_message(chatId=chatId, file=file, fileType="audio")

    if content.lower().startswith("адпанель") or content.lower().startswith("adpanel"):
        if data.message.author.role != 0:
            if translator == "ru":
                sub_client.send_message(message="""
[B]Админ Панель
Онлайн - Рам появлится в списке "В сети"
Оффлайн - Рам перестанет высввечтиваться
Зачистка - Чистит 10 сообщений (с учётом этого)
СуперЧистка - Чистит 100 сообщений
""", chatId=chatId, replyTo=id)
            elif translator == "en":
                sub_client.send_message(message="""
[B]Admin Panel.
Online - Ram will appear in the "Online" list
Offline - Ram will no longer appear
Cleanup - Cleans up 10 posts (includes this one)
SuperClean - Cleans 100 messages
""", chatId=chatId, replyTo=id)
        elif not data.message.author.role != 0:
            if translator == "ru":
                sub_client.send_message(message="Прости, но у меня или у тебя нет прав на выполнения этой команды", chatId=chatId)
            elif translator == "en":
                sub_client.send_message(message="I'm sorry, but I or you do not have the authority to execute this command", chatId=chatId)

    if content.lower().startswith("!ночь") or content.lower().startswith("!night"):
        if data.message.author.role != 0:
            if translator == "ru":
                sub_client.send_message(message="*зевая* Спокойной ночи сладкие мои~", chatId=chatId)
            elif translator == "en":
                sub_client.send_message(message="*singing* Good night my sweethearts~", chatId=chatId)
        elif not data.message.author.role != 0:
            if translator == "ru":
                sub_client.send_message(message="Прости, но у меня или у тебя нет прав на выполнения этой команды", chatId=chatId)
            elif translator == "en":
                sub_client.send_message(message="I'm sorry, but I or you do not have the authority to execute this command", chatId=chatId)

    if content.lower().startswith("!утро") or content.lower().startswith("!morn"):
        if data.message.author.role != 0:
            if translator == "ru":
                sub_client.send_message(message="*потирая сонные глазки улыбаясь* Доброе утро лапочки~", chatId=cahtId)
            elif translator == "en":
                sub_client.send_message(message="*rubbing sleepy eyes and smiling* Good morning, darlings~", chatId=cahtId)
        elif not data.message.author.role != 0:
            if translator == "ru":
                sub_client.send_message(message="Прости, но у меня или у тебя нет прав на выполнения этой команды", chatId=chatId)
            elif translator == "en":
                sub_client.send_message(message="I'm sorry, but I or you do not have the authority to execute this command", chatId=chatId)

    if content.lower().startswith("зачистка") or content.lower().startswith("сleanup"):
        if data.message.author.role != 0:
            for msgId in sub_client.get_chat_messages(chatId=data.message.chatId, size=10).messageId:
                sub_client.delete_message(reason="зачистка", chatId=data.message.chatId, messageId=msgId, asStaff=True)
        elif not data.message.author.role != 0:
            if translator == "ru":
                sub_client.send_message(message="Прости, но у меня или у тебя нет прав на выполнения этой команды", chatId=chatId)
            elif translator == "en":
                sub_client.send_message(message="I'm sorry, but I or you do not have the authority to execute this command", chatId=chatId)

    if content.lower().startswith("суперчистка") or content.lower().startswith("superclean"):
        if data.message.author.role != 0:
            for msgId in sub_client.get_chat_messages(chatId=data.message.chatId, size=100).messageId:
                sub_client.delete_message(reason="суперчистка", chatId=data.message.chatId, messageId=msgId, asStaff=True)
        elif not data.message.author.role != 0:
            if translator == "ru":
                sub_client.send_message(message="Прости, но у меня или у тебя нет прав на выполнения этой команды", chatId=chatId)
            elif translator == "en":
                sub_client.send_message(message="I'm sorry, but I or you do not have the authority to execute this command", chatId=chatId)

    if [x for x in ['.tickle', '.kus', '.slap', '.poke', '.hug', '.cuddle', '.feed', '.kiss', '.pat', '!утро', '!ночь', 'гс', '!morn', '!night', 'gs' ] if (x in content)]:
        sub_client.delete_message(reason="зачистка чата", chatId=data.message.chatId, messageId=data.message.messageId, asStaff=True)



for x in client.chat_methods:
    methods.append(client.event(client.chat_methods[x].__name__)(on_message))

while True:
    if time.time() >= reloadTime:
        if translator == "ru":
            print("Обновление Сокета...")
        elif translator == "en":
            print("Updating Socket...")
        try:
            client.close()
            client.start()
        except:pass
        if translator == "ru":
            print("Обновлено!")
        elif translator == "en":
            print("Updated!")
        reloadTime += 170
