from pydantic import BaseModel

class WeatherCommentResponse(BaseModel):
    message: str
    comment_url: str