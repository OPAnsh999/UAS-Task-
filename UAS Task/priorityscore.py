# Sample list of casualties - 3.png
casualties = [
    {'id':'C1','shape':'star','emergency':'red'},
    {'id':'C2','shape':'star','emergency':'yellow'},
    {'id':'C3','shape':'star','emergency':'green'},
    {'id':'C4','shape':'square','emergency':'green'},
    {'id':'C5','shape':'square','emergency':'green'},
    {'id':'C6','shape':'square','emergency':'red'},
    {'id':'C7','shape':'square','emergency':'yellow'},
    {'id':'C8','shape':'triangle','emergency':'yellow'},
    {'id':'C9','shape':'triangle','emergency':'yellow'}
]

# Mapping tables
shape_score = {'star': 3, 'triangle': 2, 'square': 1}
emergency_score = {'red': 3, 'yellow': 2, 'green': 1}

# Build priority_score array
priority_score = []
for c in casualties:
    s = shape_score[c['shape'].lower()]
    e = emergency_score[c['emergency'].lower()]
    priority_score.append(s * e)
    
print(priority_score)