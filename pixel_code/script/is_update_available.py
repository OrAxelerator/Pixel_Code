def is_update_available(current, latest) -> bool:
    """
    Return True when the version 
    Arg : need self.parametre.version
    """
    return current.lstrip("v") != latest.lstrip("v")