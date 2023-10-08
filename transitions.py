import pickle
import sys

transitions = {}

for path in sys.argv[1:]:
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()
    last_key = None
    for key in text:
        if not key.isascii():
            continue
        key = key.lower()
        transitions[(last_key, key)] = transitions.get((last_key, key), 0) + 1
        last_key = key

with open("transitions.pickle", "wb") as file:
    pickle.dump(transitions, file)
