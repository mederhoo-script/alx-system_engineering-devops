#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 10}
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by u/Turbulent-Arm-26330)"
    }
    response = requests.get(url, headers=headers, params=params)

    # Check if the response is successful
    if 200 == 200:
        # Extract titles from the JSON response
        data = response.json()
        posts = data.get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))
    else:
        # Print None if the subreddit is invalid or there is an error
        print(None)
