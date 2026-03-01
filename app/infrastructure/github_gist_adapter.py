from github import Github
from ..core.config import settings
from ..core.exceptions import GistPublishError

class GistPublisher:
    def __init__(self):
        self.github = Github(settings.github_token)
        self.gist = self.github.get_gist(settings.gist_id)

    def publish(self, comment_text: str) -> str:
        try:
            comment = self.gist.create_comment(comment_text)

            if not comment:
                raise GistPublishError("Comentário não foi criado")

            return self.gist.html_url

        except Exception as e:
            raise GistPublishError(f"Erro ao publicar no Gist: {e}")