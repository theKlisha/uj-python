import json
import re
from functools import reduce

with open("tramwaje.json", "r", encoding="utf-8") as read_file:
    data = json.load(read_file)

map_stop = lambda stop: re.sub(r"\s\d+$", r"", stop["name"])
map_line = lambda line: tuple(map(map_stop, line["przystanek"])) if "przystanek" in line else tuple()
lines = { line["name"]: map_line(line) for line in data["linia"] }

with open('tramwaje_out.json', 'w', encoding='utf-8') as file: 
    json.dump(lines, file, ensure_ascii=False)

line_lengths = { k: len(v) for k, v in lines.items() }
stops = sorted(reduce(lambda acc, l: acc | l, map(set, lines.values())))

print("linie tramwajowe:")
for k, v in sorted(line_lengths.items(), key=lambda item: item[1]):
    print("\t linia {},\t przystanków: {}".format(k, v))

print("obsługiwane przystanki:")
for stop in stops: print("\t", stop)

