def solution(wallpaper):
    x = []
    y = []
    for i,j in enumerate(wallpaper, 0):
        if j.find('#') > -1:
            x += [i]
            y += [j.find('#'), j.rfind('#')]
    answer = [min(x), min(y), max(x)+1, max(y)+1]
    return answer