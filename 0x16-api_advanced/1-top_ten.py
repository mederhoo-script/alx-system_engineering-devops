#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """api"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 10}
    headers = {
        "User-Agent":
        "0x16-api_advanced:project:v1.0.0 (by u/Turbulent-Arm-26330)"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        if not posts:
            print(f"No hot posts found in subreddit: {subreddit}")
            return
        for post in posts:
            print(post.get('data', {}).get('title'))
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request error occurred: {e}")


# Example usage:
top_ten("python")
