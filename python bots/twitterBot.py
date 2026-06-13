import csv, random, tweepy


client = tweepy.Client(
    consumer_key="",
    consumer_secret="",
    access_token="",
    access_token_secret=""
)

random_tweet = ""
with open("twitterBot/quotes.csv", newline='') as file:
    reader = csv.reader(file, delimiter=",", quotechar="\"")
    random_choice = random.choice(list(reader))
    random_tweet = "\""+random_choice[1]+"\" - "+random_choice[0]

client.create_tweet(text=random_tweet)
