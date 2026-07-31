import requests


REPO = "OrAxelerator/Pixel_Code"
URL = f"https://api.github.com/repos/{REPO}/releases"



def get_latest_version()-> object | None:
    """ 
    can return release and pre-release.
    And None if 404 or user don't have connection
    """

    try:
        r = requests.get(URL)

        if r.status_code == 404:
            return None
        else:
            releases = r.json()
    except:
        return None
    
    # print(releases[0]["tag_name"])      # la plus récente, même si c'est une prerelease
    # print(releases[0]["prerelease"])    # True ou False
    return releases