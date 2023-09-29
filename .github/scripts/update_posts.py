import requests
from bs4 import BeautifulSoup
from github import Github, Auth
import os
import re

TOKEN = os.environ.get('GH_TOKEN')
URL = "https://hunj.dev"
HEADER = "### Recent Blog Posts"
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

shithub = Github(auth=Auth.Token(TOKEN))
repo = shithub.get_repo(REPO)
readme = repo.get_readme()

new_content = re.sub(REGEX, posts_text, readme.decoded_content.decode())
repo.update_file(readme.path, 'Update recent blog posts', new_content, readme.sha)
