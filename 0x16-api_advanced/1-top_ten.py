#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests
import sys


def top_tens(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "linux"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 404:
        print("Subreddit not found")
        return
    elif response.status_code != 200:
        print("Failed to retrieve data from Reddit API")
        return
    
    try:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title']
                print(title)
        else:
            print("No posts found")
    except Exception as e:
        print("Error decoding JSON response:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py subreddit")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
