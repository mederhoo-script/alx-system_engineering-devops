#!/usr/bin/python3

"""a function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers)
for a given subreddit.
If an invalid subreddit is given,
the function should return 0."""

import requests


def number_of_subscribers(subreddit):
    """get number of subscibers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'linux:Ubuntu 20.04 (by u/Turbulent-Arm-26330'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    if response.status_code == 200:
        data = response.json()
        return data.get("data").get("subscribers")
    else:
        return 0
