from instabot import Bot
import os
import shutil

counter = 1


def convertToURL():
    global counter
    for user in open("instagram users.txt", "r").readlines():  # Get user from the file.
        open("instagram URLs.txt", "a").write(f"{counter}. instagram.com/{user}")  # Write the user to new file and add the URL format.
        counter += 1


def getUsers(post):
    global counter  # Just a counter for the print to see how much users I've got.
    for id in bot.get_media_likers(post):  # Get user from likes users.
        if f"{bot.get_username_from_user_id(id)}\n" not in open("already followed.txt", "r").readlines():  # Check if that user is already in the file.
            if f"{bot.get_username_from_user_id(id)}\n" not in open("instagram users.txt", "r").readlines():  # Check if that user is already in the file.
                if bot.get_user_info(id)['following_count'] > bot.get_user_info(id)['follower_count']:  # Check if the following/follower ratio is good.
                    print(f"{counter}. {bot.get_username_from_user_id(id)}")  # Print the user name.
                    counter += 1  # counter + 1
                    open("instagram users.txt", "a").write(bot.get_username_from_user_id(id) + "\n")  # Add the user to the file.
                    open("already followed.txt", "a").write(bot.get_username_from_user_id(id) + "\n")  # Add the user to the file.


if os.path.exists("config"):  # delete the config file so the program can run.
    try:
        shutil.rmtree("config")
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))

convertToURL()  # If you want to convert to URL.

bot = Bot(filter_users=False,
          filter_business_accounts=False,
          min_likes_to_like=0,
          max_likes_to_like=10000,
          min_media_count_to_follow=0)
bot.login(username="nisui_hevrati", password="@Re3228559092")

post = bot.get_media_id_from_link("https://www.instagram.com/p/CipMypvIm5B/")  # TODO: DON'T FORGET TO PUT THE POST.


while len(open("instagram users.txt", "r").readlines()) < 100:
    if os.stat("instagram users.txt").st_size > 0:  # Check if there is users in the file.
        for user in open("instagram users.txt", "r"):  # Get every user from file.
            repuser = user.replace("\n", "")  # Delete the "/n" from the the string.
            print("Entered to user: ", repuser)  # Print the entered user.
            if not bot.get_user_info(bot.get_user_id_from_username(repuser))['is_private']:  # Check if the user is no private.
                if bot.get_user_info(bot.get_user_id_from_username(repuser))['media_count'] != 0:  # Check if there is a media in the user.
                    getUsers(bot.get_user_medias(bot.get_user_id_from_username(repuser))[0])  # Get the like users from the media.
                else:
                    print("No Media.")  # Print "No Media." if there is no media.
            else:
                print("Private Account.")  # Print "Private Account." if the user is private.
    else:  # If there is no users - Take media from input.
        getUsers(post)  # Get likes users from media.
