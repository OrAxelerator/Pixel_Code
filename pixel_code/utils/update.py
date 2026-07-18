import requests


REPO = "OrAxelerator/Pixel_Code"
URL = f"https://api.github.com/repos/{REPO}/releases"



def get_latest_version():
    """ can return release and pre-release"""
    r = requests.get(URL)
    releases = r.json()

    # print(releases[0]["tag_name"])      # la plus récente, même si c'est une prerelease
    # print(releases[0]["prerelease"])    # True ou False

    return r.json()