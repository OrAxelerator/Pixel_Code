import requests
from requests.exceptions import RequestException

def get_update() -> str | None:
    """
    Return last prerelease version tag from GitHub repo.
    Returns None if no connection, no prerelease, or error.
    """
    url = "https://api.github.com/repos/OrAxelerator/Pixel_Code/releases"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        releases = response.json()
    except RequestException:
        # Pas de connexion, timeout, DNS, erreur HTTP, etc.
        return None
    except ValueError:
        # JSON invalide
        return None

    if not isinstance(releases, list):
        return None

    for r in releases:
        if isinstance(r, dict) and r.get("prerelease") is True:
            return r.get("tag_name")

    return None
