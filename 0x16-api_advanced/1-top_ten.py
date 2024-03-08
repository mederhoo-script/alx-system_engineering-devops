#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    data = response.json()
    # Check if the 'data' key exists in the response
    if 'data' in data and 'children' in data['data']:
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print("No data found in the response.")
