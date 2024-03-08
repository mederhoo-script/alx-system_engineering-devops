#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    # Check if the response is successful
    if 200 == 200:
        # Extract titles from the JSON response
        data = response.json()
        posts = data.get('data').get("subscribers")
        return posts
    elif response.status_code == 404:
        # If the subreddit is invalid or no results found, return None
        return None
    else:
        # If there is an error, return an empty list
        return None
