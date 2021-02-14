# tabiblia
Simple Bible quoting bot for Reddit

Comment on Reddit with a Bible reference between brackets, and you'll get a comment reply with the requested passage in ESV. E.g. `[Matthew 28:16-20]` or `[John 1:1]`

For single-chapter books, just refer to chapter 1. E.g., `[Jude 1:24-25]`

>τὰ βιβλία *"the books"*

# Setup
1. Install Python 3 `sudo apt install python3.9`
1. Install PIP `sudo apt install python3-pip`
1. Install PRAW `pip3 install praw`
1. Clone this repo somewhere, e.g. `/opt/`
1. `sudo touch /opt/tabiblia/shh.json`
1. Add your secrets to `shh.json`
```
{
    "app":"tabiblia v0",
    "redditid":"{your reddit app id}",
    "redditsecret":"{your reddit app's secret}",
    "username":"{your reddit bot's username}",
    "password":"{your reddit bot's password}",
    "esvkey":"{your ESV API key}"
}
```
7. Run `core.py`, recommend doing so in a way that can manage it as a system process.
