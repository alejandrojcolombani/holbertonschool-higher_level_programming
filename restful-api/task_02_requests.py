#!/usr/bin/python3
"""Module for consuming and processing API data."""

import csv
import requests


def fetch_and_print_posts():
    """Fetch all posts and print their titles."""
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch all posts and save them to a CSV file."""
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    if response.status_code == 200:
        posts = response.json()

        csv_data = []

        for post in posts:
            csv_data.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        with open(
            "posts.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["id", "title", "body"]
            )

            writer.writeheader()
            writer.writerows(csv_data)
