#!/usr/bin/python3
"""Write a function that queries the Reddit API and returns the
number of subscribers (not active users, total subscribers)
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"user-agent": "Chrome/126.0.0.0"}

    subscribers, data = "", ""
    response = requests.get(
        url=url, headers=headers, allow_redirects=False
    )
    if response.status_code == 200 and not response.is_redirect:
        response = response.json()
        data = response["data"]
        subscribers = data["subscribers"]
        return subscribers
    else:
        return 0
