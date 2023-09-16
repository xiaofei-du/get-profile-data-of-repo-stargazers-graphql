#!/usr/bin/env python
__author__ = "Nova Kwok"
__license__ = "GPLv3"
import csv
import datetime
from datetime import date
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--token', required=True, help="The GitHub Token.")
parser.add_argument('-r', '--repo', required=True,
                    help="The GitHub Repo,in the form like 'user/repo'.")
args = parser.parse_args()

owner = args.repo.split('/')[0]
repo = args.repo.split('/')[1]

headers = {"Authorization": "token "+args.token}

fields = ["name", "email", "company", "twitter_username", "username", "bio", "num_followers",
          "num_following", "star_time", "blog", "repo_count", "avatar_url", "hireable", "created_at", "updated_at"]


def run_query(query):
    request = requests.post('https://api.github.com/graphql',
                            json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(
            request.status_code, query))


query = """
{{
  repository(owner: "{0}", name: "{1}") {{
    stargazers(first: 100 {2}) {{
      pageInfo {{
        endCursor
        hasNextPage
        hasPreviousPage
        startCursor
      }}
      edges {{
        starredAt
        node {{
          login
          email
          name
          bio
          company
          repositories(first:100, isFork: false) {{
            totalCount
          }}
          isHireable
          avatarUrl
          createdAt
          updatedAt
          twitterUsername
          websiteUrl
          followers(first: 0) {{
            totalCount
          }}
          following(first: 0) {{
            totalCount
          }}
        }}
      }}
    }}
  }}
}}
"""

star_list = []
hasNextPage = True
endCursor = ""  # Start from begining
count = 0
email_count = 0

# Month abbreviation, day and year
today = date.today()
today = today.strftime("%b-%d-%Y")

user_filename = owner + "_" + repo + "_" + today + ".csv"
with open(user_filename, 'w') as stars:
    stars_writer = csv.writer(stars)
    stars_writer.writerow(fields)
    while hasNextPage:
        this_query = query.format(owner, repo, endCursor)
        result = run_query(this_query)  # Execute the query
        hasNextPage = result['data']['repository']['stargazers']['pageInfo']['hasNextPage']
        endCursor = result['data']['repository']['stargazers']['pageInfo']['endCursor']
        endCursor = ', after: "' + endCursor + '"'
        data = result['data']['repository']['stargazers']['edges']

        for item in data:
            count += 1
            email = item['node']['email']

            # Skip empty email
            if email == "":
                continue

            email_count += 1

            username = item['node']['login']
            name = item['node']['name']
            twitter_username = item['node']['twitterUsername']
            num_followers = item['node']['followers']['totalCount']
            num_following = item['node']['following']['totalCount']
            hireable = item['node']['isHireable']
            company = item['node']['company']
            bio = item['node']['bio']
            avatar_url = item['node']['avatarUrl']
            blog = item['node']['websiteUrl']

            repo_count = item['node']['repositories']['totalCount']

            created_at = item['node']['createdAt']
            created_at = datetime.datetime.strptime(
                created_at, '%Y-%m-%dT%H:%M:%SZ')
            created_at = created_at.strftime('%Y-%m-%d %H:%M:%S')

            updated_at = item['node']['updatedAt']
            updated_at = datetime.datetime.strptime(
                updated_at, '%Y-%m-%dT%H:%M:%SZ')
            updated_at = updated_at.strftime('%Y-%m-%d %H:%M:%S')

            star_time = datetime.datetime.strptime(
                item['starredAt'], '%Y-%m-%dT%H:%M:%SZ')
            star_time = star_time.strftime('%Y-%m-%d %H:%M:%S')
            star_list.append((username, star_time))
            stars_writer.writerow([name, email, company, twitter_username, username, bio, num_followers,
                                  num_following, star_time, blog, repo_count, avatar_url, hireable, created_at, updated_at])

        print(str(email_count) + "/" + str(count) + " users processed.")
