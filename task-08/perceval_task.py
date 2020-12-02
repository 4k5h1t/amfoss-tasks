
from pprint import pprint 
import base64
from github import Github
from perceval.backends.core.git import Git
import os                            

g = Github()
# get that user by username
user = g.get_user('amfoss')

for repo in user.get_repos():
    cmd = "perceval git --json-line https://github.com/amfoss/" + repo.name + " >> commits.json"
    os.system(cmd)

