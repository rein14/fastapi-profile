from functools import cache
import json
import typing
from dataclasses import dataclass, field
from fastapi import FastAPI, HTTPException, Response
from cached import cached
app = FastAPI()


@dataclass
class Profile:
    id: str
    name: str
    website: str
    github: str
    linkedin: str
    twitter: str
    education: str
    languages : list[str] = field(default_factory=list)
    frameworks : list[str] = field(default_factory=list)
    about_me: str = ""
    
 
profiles: dict[str, Profile] = {}


with open("profile.json", encoding="utf8") as profile:
    raw_profile = json.load(profile)
    profile = Profile(**raw_profile)
    profiles[profile.id] = profile

@app.get("/")
def get_root() -> Response:
    return Response("TO check profile gotto /profile")

class PrettyJSONResponse(Response):
    media_type = "application/json"

    def render(self, content: typing.Any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=5,
            separators=(',', ': '),
        ).encode('utf-8')

@cached
@app.get("/{profile_id}", response_model=Profile, response_class=PrettyJSONResponse)
def read_profile(profile_id: str):
    if profile_id not in profiles:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profiles[profile_id]
