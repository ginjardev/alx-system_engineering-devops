#!/usr/bin/python3
"""Write a function that queries the Reddit API and returns the
number of subscribers (not active users, total subscribers)
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers in a subreddit"""
    headers = {"User-Agent": "web_crawler"}
    # Reddit API endpoint for subreddit information
    url = "https://oauth.reddit.com/r/{}/about.json".format(subreddit)

    # Make a GET request to the API
    response = requests.get(
        url, headers=headers,  allow_redirects=False
    )

    # Check if the request was successful (status code 200) and not redirected
    if response.status_code == 200 and not response.is_redirect:
        # Parse the JSON response and extract the number of subscribers
        data = response.json()
        subscribers_count = data["data"]["subscribers"]
        return subscribers_count
    else:
        # Return 0 for invalid subreddit or other errors
        return 0
