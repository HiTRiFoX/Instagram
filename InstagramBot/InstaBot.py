import sys

sys.path.append("C:/Users/reuve/PycharmProjects/venv/Lib/site-packages")

from instabot import Bot
import os
import shutil
import time as t
import smtplib as smtp
import random

file_path = "C:/Users/reuve/PycharmProjects/InstagramBot/config"
if os.path.exists(file_path):
    shutil.rmtree(file_path)

bot = Bot(
    min_likes_to_like=0,
    max_likes_to_like=10000,
    max_followers_to_follow=10000,
    unfollow_delay=0.5,
    follow_delay=1,
    max_follows_per_day=10000,
    max_unfollows_per_day=10000,
    max_following_to_follow=10000,
    filter_users=False,
    filter_business_accounts=False,
    filter_verified_accounts=False,
    base_path="C:/Users/reuve/PycharmProjects/InstagramBot/config",
    blocked_actions_sleep_delay=5
)

bot.login(username="nisui_hevrati", password="@Re322855909")

following = len(bot.get_user_following("nisui_hevrati"))


def send_msg(subject, description=""):
    email = "botting.instagram@yandex.ru"
    server = smtp.SMTP("smtp.yandex.ru", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("botting.instagram@yandex.ru", "ghdgiprbqqoasjai")
    server.sendmail(email, email, f"Subject: {subject}\n\n{description}")


def program(follower=""):
    if follower == "":
        while True:
            users = get_last_following()
            for user in users:
                if not already_followed(user):
                    if check_ratio(user):
                        bot.follow(user)
                        t.sleep(random.randint(60, 90))
    else:
        while True:
            users = specific_user(follower)
            for user in users:
                if not already_followed(user):
                    if check_ratio(user):
                        print("blocked_actions: ", bot.blocked_actions)
                        print("sleeping_actions: ", bot.sleeping_actions)
                        print("blocked_actions_protection: ", bot.blocked_actions_protection)
                        print("blocked_actions_sleep: ", bot.blocked_actions_sleep)
                        print("blocked_actions_sleep_delay: ", bot.blocked_actions_sleep_delay)
                        bot.follow(user)
                        t.sleep(random.randint(60, 90))




def get_last_following():
    global following
    while True:
        if following == 0:
            following = len(bot.get_user_following("nisui_hevrati"))
        if not bot.get_user_medias(bot.get_user_following("nisui_hevrati")[following - 1]):
            following -= 1
        elif not bot.get_media_likers(bot.get_user_medias(bot.get_user_following("nisui_hevrati")[following - 1])[0]):
            following -= 1
        else:
            return bot.get_media_likers(bot.get_user_medias(bot.get_user_following("nisui_hevrati")[following - 1])[0])


def check_ratio(user):
    if bot.get_user_info(user)['following_count'] > bot.get_user_info(user)['follower_count']:
        return True
    else:
        return False


def specific_user(user):
    return bot.get_media_likers(bot.get_user_medias(user)[0])


def add_followed():
    users = bot.get_user_following("nisui_hevrati")
    followed = open("C:/Users/reuve/PycharmProjects/InstagramBot/config/followed.txt", "w")
    for user in users:
        followed.write("%s" % user)
        followed.write("\n")


def already_followed(user):
    followed = open("C:/Users/reuve/PycharmProjects/InstagramBot/config/followed.txt", "r")
    if user in followed.read():
        return True
    else:
        return False

print("blocked_actions: ", bot.blocked_actions)
print("sleeping_actions: ", bot.sleeping_actions)
print("blocked_actions_protection: ", bot.blocked_actions_protection)
print("blocked_actions_sleep: ", bot.blocked_actions_sleep)
print("blocked_actions_sleep_delay: ", bot.blocked_actions_sleep_delay)
#send_msg("Program Started")
#add_followed()
try:
    program("daniel_macholsky")
except:
    send_msg("Program Stopped", sys.exc_info())

