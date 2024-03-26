from collections import defaultdict

with open('input.txt', 'r') as file:
    lines = file.readlines()
n = list(map(int, lines[0].split()))[0]

songs_all = []

i = 1
while i < 2 * n:
    k = list(map(int, lines[i].split()))[0]
    songs = set(lines[i + 1].split())
    songs_all.append(songs)
    i += 2

s = songs_all[0]
for songs in songs_all:
    s = s.intersection(songs)
print(len(s))
print(*sorted(list(s)))