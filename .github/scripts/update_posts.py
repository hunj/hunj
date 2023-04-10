import requests
from bs4 import BeautifulSoup
from github import Github
import os
import re

URL = "https://hunj.dev"
HEADER = "### Recent Blog Posts\n"
REPO = 'hunj/hunj'
END = "Read more"
REGEX = rf"{HEADER}[\s\S]*?(?={END})"

req = requests.get(URL)
soup = BeautifulSoup(req.content, "html.parser")
posts = [HEADER]

for post in soup.select('article.post'):
    title = post.select_one('h2.post-title').text.strip()
    path = post.select_one('a.post-title-link')['href']
    text = f"- [{title}]({URL}{path})"

    posts.append(text)

posts.append('\n')
posts_text = '\n'.join(posts)

shithub = Github("access_token")
repo = shithub.get_repo(REPO)
readme = repo.get_readme()

with open(readme, 'rw') as readme_file:
    re.sub(REGEX, posts_text, readme_file)
    shithub.update_contents(repo, 'README.md', 'Update recent blog posts', readme['sha'], readme_file)
