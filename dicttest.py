d = {'a':4, 'd':2, 'm':1, 'c':4}

print([{k:v} for k, v in d.items() if v == max(d.values())])



min_out = {}
max_out = {}
for k,v in d.items():
    if v == min(d.values()):
        min_out[k] = v
    if v == max(d.values()):
        max_out[k] = v
        
print(min_out, max_out)
