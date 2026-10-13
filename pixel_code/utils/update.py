import json
import logging
import re
import subprocess
import sys
from importlib.metadata import distribution, PackageNotFoundError
from urllib.parse import unquote, urlparse

import requests


REPO = "OrAxelerator/Pixel_Code"
RELEASES_URL = f"https://api.github.com/repos/{REPO}/releases"
TIMEOUT = 3 # seconds, so Pixel_Code launches fast without connection


def parse_version(text: str) -> tuple | None:
    """ "v0.5.2" or "0.5.2" -> (0, 5, 2). None if the text is not a version."""
    match = re.match(r"v?(\d+)\.(\d+)\.(\d+)", str(text))
    if match is None:
        return None
    return tuple(int(n) for n in match.groups())


def get_latest_release(allow_prerelease: bool = True) -> dict | None:
    """
    Return the most recent release of github (dict of the github api).
    Return None if user doesn't have connection, github block us (rate limit)
    or if there is no release.
    """
    try:
        r = requests.get(RELEASES_URL, timeout=TIMEOUT)
        if r.status_code != 200:
            logging.warning(f"Github api answer {r.status_code} while checking update")
            return None
        releases = r.json()
    except (requests.RequestException, ValueError) as e:
        logging.info(f"No connection to github, update check skipped ({e})")
        return None

    candidates = [
        release for release in releases
        if isinstance(release, dict)
        and not release.get("draft")
        and (allow_prerelease or not release.get("prerelease"))
        and parse_version(release.get("tag_name", "")) is not None
    ]
    if not candidates:
        return None

    return max(candidates, key=lambda release: parse_version(release["tag_name"]))


def is_newer(latest_tag: str, current_version: str) -> bool:
    latest = parse_version(latest_tag)
    current = parse_version(current_version)
    if latest is None or current is None:
        return False
    return latest > current


def get_editable_location() -> str | None:
    """
    Return the path of the source code if Pixel_Code is installed with "pip install -e ."
    Return None for a normal install (pipx install . / pip install .)
    """
    try:
        direct_url = distribution("pixel-code").read_text("direct_url.json")
    except PackageNotFoundError:
        return None
    if not direct_url:
        return None

    data = json.loads(direct_url)
    if data.get("dir_info", {}).get("editable"):
        return unquote(urlparse(data.get("url", "")).path)
    return None


def install_release(tag: str) -> bool:
    """
    Install the release 'tag' with pip of the python that run Pixel_Code
    (work for pipx and pip). User data (platformdirs) is not touched.
    Must be called after curses is closed, pip output is shown in the terminal.
    """
    zip_url = f"https://github.com/{REPO}/archive/refs/tags/{tag}.zip"
    cmd = [sys.executable, "-m", "pip", "install", "--upgrade", zip_url]
    logging.info(f"Update command : {' '.join(cmd)}")
    try:
        return subprocess.run(cmd).returncode == 0
    except OSError as e:
        logging.error(f"Update failed : {e}")
        return False
