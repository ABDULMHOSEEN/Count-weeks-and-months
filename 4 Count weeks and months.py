# define a function that make seconds into other form
def format_duration(seconds):
    # if the seconds is less than 1 that mean now
    if seconds == 0: return "now"
    elif seconds < 0: return "Error invalid number of seconds"
    # make a list that will save the kinds of times
    time = [0, 0, 0, 0, 0]  # years - months - hour - minutes - seconds
    time[0] = seconds // (365 * 24 * 60 * 60)
    time[1] = seconds % (365 * 24 * 60 * 60) // (24 * 60 * 60)
    time[2] = seconds % (365 * 24 * 60 * 60) % (24 * 60 * 60) // (60 * 60)
    time[3] = seconds % (365 * 24 * 60 * 60) % (24 * 60 * 60) % (60 * 60) // 60
    time[4] = seconds % (365 * 24 * 60 * 60) % (24 * 60 * 60) % (60 * 60) % 60
    # make a string call out to git the format of final print
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
seconds = int(input("Enter the namber of seconds: "))
print(format_duration(seconds))