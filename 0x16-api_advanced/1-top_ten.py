#!/usr/bin/python3
"""Function to print 10 hot posts on subreddit."""
import requests

def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a provided subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-agent": "linux:ubuntu20.04(by /u/roch_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
