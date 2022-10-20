

def get_duration(string):
    string = string[2:]
    
    dur = []

    split = string.split("H")
    if len(split) > 1:
        dur.append(split[0])
        split = split[1]
    else:
        dur.append("00")
        split = split[0]

    split = split.split("M")
    if len(split) > 1:
        dur.append(split[0])
        split = split[1]
    else:
        dur.append("00")
        split = split[0]

    dur.append(split[:-1])
    return " : ".join(dur)