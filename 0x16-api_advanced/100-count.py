#!/usr/bin/python3
"""recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive,
delimited by spaces.
Javascript should count as javascript,
but java should not)."""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """recursive functions"""
    if not hot_list:  # Initialize the hot_list only in the first call
        hot_list = []
    if after == "STOP":  # Base case for recursion
        return hot_list
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    # Check if the response is successful
    if response.status_code == 200:
        # Extract titles from the JSON response
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        after = data['data']['after']
        return recurse(subreddit, hot_list, after)
    elif response.status_code == 404:
        # If the subreddit is invalid or no results found, return None
        return None
    else:
        # If there is an error, return an empty list
        return []


# Test the function
if __name__ == '__main__':
    subreddit = input("Enter subreddit: ")
    result = recurse(subreddit)
    if result is not None:
        print(len(result))
    else:
        print("None")
