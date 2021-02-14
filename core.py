import praw
import json
import re
import esv

file = open('shh.json')
variables = json.loads(file.read())

reddit = praw.Reddit(
    client_id=variables["redditid"],
    client_secret=variables["redditsecret"],
    password=variables["password"],
    user_agent=variables["app"],
    username=variables["username"]
    )

subreddit = reddit.subreddit('DrKC9N')

try:
    with open("last_comment_success.txt","r") as sourcefile:
        last_bot_comment = sourcefile.read()
except:
    print("Couldn't read from last_comment_success.txt")

for comment in subreddit.stream.comments():
    text = comment.body
    match = re.search(r"\[.{2,25}:.{1,12}\]",text)
    if match and (comment.created_utc > float(last_bot_comment)):
        print("Found a comment newer than our last bot response.")
        try:
            apiquery = re.sub(r"[^0-9a-zA-Z :-]","",match.group(0))
            print("Sending `" + apiquery + "` to the appropriate Bible API.")
            response = esv.get_esv_text(apiquery)
            comment_successful = comment.reply(response)
            if comment_successful:
                print(comment_successful.created_utc)
                last_bot_comment = str(comment_successful.created_utc)
                with open("last_comment_success.txt","w") as bump:
                    print("file opened successfully")
                    bump.write(last_bot_comment)
        except:
            print("whoops")
