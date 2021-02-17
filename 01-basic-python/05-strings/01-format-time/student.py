# Write your code hereµ
def format_time(h,m,s):
    if h < 10:
        str('0'+h)
    if m < 10:
        str('0'+m)
    if s < 10:
        str('0'+s)
    return f"{h}:{m}:{s}"
