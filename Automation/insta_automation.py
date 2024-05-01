from instabot import Bot
bot= Bot()
bot.login(username='', password='')
bot.follow('userid')
bot.upload_photo('path of file')
bot.send_message('here the message',['userid','usersid2'])

following = bot.get_user_following("user_id")
for folowng in following:
    print(bot.get_user_info(following))