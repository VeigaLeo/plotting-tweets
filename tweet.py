
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

tweets = pd.read_csv("tweets-data/tweets.csv")

tweets.head()


def get_candidates(row):
    candidates = []
    text = row['text'].lower()
    if "clinton" in text or "hillary" in text:
        candidates.append("clinton")
    if "trump" in text or "donald" in text:
        candidates.append("trump")
    if "sanders" in text or "bernie" in text:
        candidates.append("sanders")
    return ",".join(candidates)


# counts = tweets['candidate'].value_counts()
# plt.plot(range(len(counts)), counts)
# ------------------------------------------------ #
tweets["candidate"] = tweets.apply(get_candidates, axis=1)
tweets["created"] = pd.to_datetime(tweets["created"])
tweets['user_created'] = pd.to_datetime(tweets['user_created'])
tweets["user_age"] = tweets['user_created'].apply(
    lambda x: (datetime.now() - x).total_seconds() / 3600 / 24 / 365)
# plt.hist(tweets["user_age"])
# plt.title("Tweets mentioning candidates")
# plt.xlabel("Twitter account age in years")
# plt.ylabel("# of tweets")
# plt.show()


# ------------------------------------------------ #

cl_tweets = tweets["user_age"][tweets["candidate"] == "clinton"]
sa_tweets = tweets["user_age"][tweets["candidate"] == "sanders"]
tr_tweets = tweets["user_age"][tweets["candidate"] == "trump"]
plt.hist([
         cl_tweets,
         sa_tweets,
         tr_tweets
         ],
         stacked=True,
         label=["clinton", "sanders", "trump"])
plt.legend()
plt.title("Tweets mentioning each candidate")
plt.xlabel("Twitter account age in years")
plt.ylabel("# of tweets")
plt.show()
