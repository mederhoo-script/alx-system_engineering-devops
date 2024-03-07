#!/usr/bin/python3
"""a function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers)
for a given subreddit.
If an invalid subreddit is given,
the function should return 0."""
import requests


def number_of_subscribers(subreddit):
    """get number of subscibers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url)
    if response.status_code == 404:
        return 0
    if response.status_code == 200:
        data = response.json()
        return data.get("data").get("subscribers")
    else:
        return 0
