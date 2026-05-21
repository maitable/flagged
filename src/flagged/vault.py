import os
import tomllib

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
    return toml_dict


print(load_config())
