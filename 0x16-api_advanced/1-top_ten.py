#!/usr/bin/python3
"""Prints the titles of the first 10 top posts for a subreddit."""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the top 10 hot posts from subreddit.
    Args:
        subreddit (str): The name of the subreddit.
    Returns:
        None
    """
    # Send a GET request to the Reddit API to retrieve the top 10 hot posts
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit),
        headers={"User-Agent": "my_browser-01"},
        allow_redirects=False,
    )
    # Check if the request was successful
    if response.status_code != 200:
        print(None)
        return
    # Print the titles of the top 10 hot posts
    for post in response.json()["data"]["children"]:
        print(post["data"]["title"])
