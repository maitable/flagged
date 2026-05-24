from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
import frontmatter
from difflib import get_close_matches

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

def save(writeup:Writeup) -> None:
    post = frontmatter.load(writeup.path)
    post['solved'] = writeup.solved
    post["flag"] = writeup.flag
    with open(writeup.path, "w") as f:
        frontmatter.dump(post, f)

def list_all(vault: Path) -> list[Writeup]:
    writeups = []
    for p in vault.rglob("*.md"):
        try:
            writeups.append(load(p))
        except KeyError:
            print(f"Skipping ctf {p.name} because missing needed fields")
    return sorted(writeups, key=lambda w: w.date, reverse=True) #date filter

def resolve_slug(vault:Path, query:str) -> Writeup | None:
    all_writeups = list_all(vault)
    slugs = [w.slug for w in all_writeups]
    slug_name = {w.slug:w for w in all_writeups}

    for w in all_writeups:
        if w.slug == query:
            return w

    matches = get_close_matches(query, slugs, n=1, cutoff=0.5)
    if matches:
        print(f"Matched {matches[0]}")
        return slug_name[matches[0]]
    return None

