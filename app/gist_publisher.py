from github import Github, Auth

from .config import settings


def publish_to_gist(comment_text: str) -> str:
    auth = Auth.Token(settings.github_token)
    github = Github(auth=auth)
    gist = github.get_gist(settings.gist_id)
    gist.create_comment(comment_text)
    return gist.html_url
