is_anagram( s: str, t: str) -> bool:
    while len(s) != 0:
        character = s[0]
        if character in t and (t.count(character) == s.count(character)):
            t = t.replace(character, "")
            s = s.replace(character, "")
        else:
            return False
    if len(s) == 0 and len(t) == 0:
        return True
    else:
        return False
