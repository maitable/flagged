import os
from dataclasses import dataclass
import tomllib

@dataclass
class VaultConfig:
    author: str = ""
    editor: str = ""
    date_format: str = "%T-%m-%d"

def find_vault_root():
    ls = os.listdir()
    cwd = os.getcwd()
    if ".ctf.toml" in ls:
        return str(cwd) + '/.ctf.toml'
    return None
    
def load_config():
    path = find_vault_root()
    if path is not None:
        with open(path, "rb") as toml:
            toml_dict = tomllib.load(toml)
    return VaultConfig(author=toml_dict["author"], editor=toml_dict["editor"], date_format=toml_dict["date_format"])


print(load_config())
