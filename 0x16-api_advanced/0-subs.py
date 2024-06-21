#!/usr/bin/python3
"""Write a function that queries the Reddit API and returns the
number of subscribers (not active users, total subscribers)
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "balmain"}

    response = requests.get(url=url, headers=headers, allow_redirects=False)

    if response.status_code == 200 and not response.is_redirect:
        # Parse the JSON response and extract the number of subscribers
        data = response.json()
        subscribers_count = data["data"]["subscribers"]
        return subscribers_count
    else:
        # Return 0 for invalid subreddit or other errors
        return 0
