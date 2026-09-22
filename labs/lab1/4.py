sec = int(input())
hours = sec // 3600
minutes = (sec % 3600) // 60
seconds = (sec % 3600) % 60
print( f"{hours:02d}:{minutes :02d}:{seconds :02d}")