def clear_from_line(line : int = 12): 
    """line = 12 (height of static render : logo.txt)"""
    print(f"\033[H\033[{line}B\033[J", end="")