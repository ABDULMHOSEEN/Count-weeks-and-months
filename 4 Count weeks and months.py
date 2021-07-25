def format_duration(seconds):
    if seconds < 1: return "now"
    time = [0, 0, 0, 0, 0]
    time[0] = seconds // (365 * 24 * 60 * 60)
    time[1] = seconds % (365 * 24 * 60 * 60) // (24 * 60 * 60)
    time[2] = seconds % (365 * 24 * 60 * 60) % (24 * 60 * 60) // (60 * 60)
    time[3] = seconds % (365 * 24 * 60 * 60) % (24 * 60 * 60) % (60 * 60) // 60
    time[4] = seconds % (365 * 24 * 60 * 60) % (24 * 60 * 60) % (60 * 60) % 60

    out = ""
    for i in range(len(time)):
        if i == 0:
            per = " year"
        elif i == 1:
            per = " day"
        elif i == 2:
            per = " hour"
        elif i == 3:
            per = " minute"
        else:
            per = " second"
        if time[i] > 0:
            if out and sum(time[i + 1:]) != 0:
                out += ", "
            elif out:
                out += " and "
            out += str(time[i]) + per + ("s" if time[i] > 1 else "")
    return out
print(format_duration(400))