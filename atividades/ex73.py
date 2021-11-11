times = ('palmeiras', 'corinthians', 'santos', 'são paulo', 'chapecoence', 'gremio', 'atletico', 'Flamengo', 'paris', 'barcelona')

for c in range(0, 5):
    print(times[c])
for a in range(len(times[-1])):
    print(times[a])
print(times.index('chapecoence')+1)
print(sorted(times))