#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    # Check if the response is successful
    if response.status_code == 200:
        # Extract the number of subscribers from the JSON response
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        # Return 0 if the subreddit is invalid or there is an error
        return 0


# Test the function
if __name__ == '__main__':
    subreddit = input("Enter subreddit: ")
    print(number_of_subscribers(subreddit))
