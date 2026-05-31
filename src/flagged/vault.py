import os
from dataclasses import dataclass
import tomllib
from pathlib import Path

@dataclass
class VaultConfig:
    author: str = ""
    editor: str = ""
    date_format: str = "%Y-%m-%d"

def find_vault_root():
    start = Path.cwd()
    for directory in [start, *start.parents]:
        if(directory / ".ctf.toml").exists():
            return directory
    return None
    
def load_config():
    root = find_vault_root()
    if root is None:
        return VaultConfig()
    with open(root / ".ctf.toml", "rb") as toml:
        toml_dict = tomllib.load(toml)
    return VaultConfig(
        author=toml_dict.get("author", ""),
        editor=toml_dict.get("editor", ""),
        date_format=toml_dict.get("date_format", "%Y-%m-%d"),
    )

def require_vault():
    root = find_vault_root()
    if root is None:
        print("You need a vault! Run flagged init to create one")
        raise SystemExit(1)

    return root, load_config()


