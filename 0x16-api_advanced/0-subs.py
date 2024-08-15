#!/usr/bin/python3
"""This returns the number of total subscribers for a subreddit."""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    Args:
        subreddit (str): The name of the subreddit.
    Returns:
        int: The number of subscribers for the subreddit. Returns 0 if the
        request fails or the subreddit does not exist.
    """
    response = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        allow_redirects=False,
        headers={"user-agent": "my_browser-01"},
        timeout=60,
    )
    return (response.json()["data"]["subscribers"]
            if response.status_code == 200 else 0)
