x=int(input()) #3
y=int(input()) #7
z=int(input()) #5
if x<=y:
    if x<=z:
        mini=x
    else:
        mini=z
else:
    if y<=z:
        mini=y
    else:
        mini=z
print('наименьшее: ', mini)