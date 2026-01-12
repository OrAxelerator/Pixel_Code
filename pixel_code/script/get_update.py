import requests

def get_update() -> str :
    """Retun last release/version on github repo"""
    url = "https://api.github.com/repos/OrAxelerator/Pixel_Code/releases"
    releases = requests.get(url).json()
    for r in releases:
        if r["prerelease"]:
            v = r["tag_name"]
            return v  