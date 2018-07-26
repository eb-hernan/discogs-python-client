def strip_tag_name(t):
    idx = k = t.rfind('}')
    if idx != -1:
        t = t[idx + 1:]
    return t

def calculate_level(event, tname, level):
    if event == 'start' and tname == 'artist':
        return 1
    elif event == 'start':
        return level + 1
    elif event == 'end':
        return level - 1
