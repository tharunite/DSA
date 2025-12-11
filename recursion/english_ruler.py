def draw_line(length,mark=''):
    line='-'*length
    if mark:
        line+=' '+str(mark)
    print(line)

def draw_ticks(center):
    if center>=0:
        draw_ticks(center-1)
        draw_line(center)
        draw_ticks(center-1)

def draw_ruler(n,max_ticks):
    draw_line(n,mark='0')
    for i in range(1,n+1):
        draw_ticks(max_ticks-1)
        draw_line(max_ticks,mark=i)

draw_ruler(5,4)