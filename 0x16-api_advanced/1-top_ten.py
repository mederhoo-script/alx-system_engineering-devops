#!/usr/bin/python3
"""recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive,
delimited by spaces.
Javascript should count as javascript,
but java should not)."""

import requests


def top_ten(subreddit, word_list=[], after=None, counts=None):
    """recursive count"""
    if not counts:  # Initialize counts only in the first call
        counts = {}

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
            title = post['data']['title']
            for word in word_list:
                word = word.lower()  # Convert word to lowercase
                title_words = title.lower().split()
                if word in title_words:
                    if word in counts:
                        counts[word] += 1
                    else:
                        counts[word] = 1
        after = data['data']['after']
        if after is None:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
            return

        return count_words(subreddit, word_list, after, counts)
    elif response.status_code == 404:
        # If the subreddit is invalid or no results found, print nothing
        return
    else:
        # If there is an error, print nothing
        return


# Test the function
if __name__ == '__main__':
    subreddit = input("Enter subreddit: ")
    word_list = input("Enter keywords separated by spaces: ").split()
    count_words(subreddit, word_list)
