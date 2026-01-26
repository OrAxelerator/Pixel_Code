def get_name_repo(url):
    """
    in: get the name of the repo with the web url use to clone
    out: just the name of the repo
    """
    for i, letter in enumerate(url[19::]): # delete start and start after github.com/
        if letter == "/": # after name 
            return  url[i+20 : len(url )-4:] # len(url)-4 : delete .git 