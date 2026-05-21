from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
import frontmatter

@dataclass
class Writeup:
    title : str
    ctf: str
    category: str
    date: date
    solved: bool=False
    flag:str=""
    points:int=0
    difficulty:str=""
    tags:list[str]=field(default_factory=list) #default_factory=list creates a new list for each Writeup instance while list[str]=[] wouldve used the same tags for all writeups
    path: Path = field(default=None, repr=False) #repr=False bc path is not useful output
    slug:str=""
    content:str=""

# post["title"] gets a frontmatter field
# post.content gets the markdown body below ---


def load(path:Path) -> Writeup:
    post=frontmatter.load(path)
    return Writeup(
        title = post['title'],
        ctf = post["ctf"],
        category = post["category"],
        date = post["date"],
        solved = post.get('solved',False),
        flag = post.get("flag", ""),
        points = post.get("points", 0),
        difficulty = post.get("difficulty", ""),
        tags = post.get("tags", []),
        path = path,
        slug=path.stem,
        content=post.content,
    )

#post['key'] will raise keyerror if missing (required)
#post.get('key', default) if they are optional


