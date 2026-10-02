total_seconds = int(input())
hours = total_seconds // 3600
min = (total_seconds % 3600) // 60
sec = total_seconds % 60

print(hours, 'ч', min, 'мин', sec, 'с')