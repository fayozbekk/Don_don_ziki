import random

maftuna = input("Tosh, qaychi va qog'ozdan birini tanlang:")
tqq = ["tosh", "qaychi", "qog'oz"]
bot = random.choice(tqq)
print("Botning tanlovi:", bot)
if bot == maftuna:
    print("Durrang🤫")
elif (bot == "tosh" and maftuna=="qaychi"
      or bot == "qaychi" and maftuna=="qog'oz"
      or bot == "qog'oz" and maftuna=="tosh"):
    print("Siz yutqizdingiz🤣")

elif (maftuna == "tosh" and bot=="qaychi"
      or maftuna == "qaychi" and bot=="qog'oz"
      or maftuna == "qog'oz" and bot=="tosh"):
    print("Siz yutdizgiz😒")
else:
    print("Bunday ishora yo'q")
