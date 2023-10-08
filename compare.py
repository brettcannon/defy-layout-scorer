"""Compare various keyboard layouts for the Dygma Defy keyboard."""
import operator
import pickle

keyboard_layouts = {
    "QWERTY": ("qwertyuiop" "asdfghjkl;" "zxcvbnm,./"),
    # https://en.wikipedia.org/wiki/Dvorak_keyboard_layout
    "Dvorak": ("',.pyfgcrl" "aoeuidhtns" ";qjkxbmwvz"),
    # https://en.wikipedia.org/wiki/Dvorak_keyboard_layout#Programmer_Dvorak
    "Dvorak (Programmer)": (";,.pyfgcrl" "aoeuidhtns" "'qjkxbmwvz"),
    # https://colemakmods.github.io/mod-dh/
    "Colemak Mod-DH": ("qwfpbjluy;" "arstgmneio" "zxcdvkh,./"),
    "Colemak Mod-DHk": ("qwfpbjluy;" "arstgkneio" "zxcdvmh,./"),
    # https://colemak.com
    "Colemak": ("qwfpgjluy;" "arstdhneio" "zxcvbkm,./"),
    # https://github.com/kaievns/halmak
    "Halmak": ("wlrbz;qudj" "shnt,.aeoi" "fmvc/gpxky"),
    # https://workmanlayout.org
    "Workman": ("qdrwbjfup;" "ashtgyneoi" "zxmcvkl<>?"),
    # https://normanlayout.info
    "Norman": ("qwdfkjurl;" "asetgynioh" "zxcvbpm,./"),
    # http://mkweb.bcgsc.ca/carpalx/
    "Carpalx (QFMLWY)": ("qfmlwyuobj" "dstnriaeh;" "zvgcxpk,./"),
}

penalties = {
    "same hand": 1,
    "top row": 2,
    "inner column, top row (delta)": +4,  # 6
    "inner column, home row (delta)": +3,  # 3
    "bottom row": 4,
    "inner column, bottom row (delta)": +1,  # 5
    "missing": 10,
}


with open("transitions.pickle", "rb") as file:
    transitions = pickle.load(file)

keyboards = {}
for keyboard_name, keyboard_layout in keyboard_layouts.items():
    keyboards[keyboard_name] = {"all keys": set(keyboard_layout)}
    keyboards[keyboard_name]["top row"] = set(keyboard_layout[:10])
    keyboards[keyboard_name]["bottom row"] = set(keyboard_layout[-10:])
    left_hand = set()
    for start in range(0, 30, 10):
        left_hand |= set(keyboard_layout[start : start + 5])
    keyboards[keyboard_name]["left hand"] = left_hand
    right_hand = set()
    for start in range(5, 30, 10):
        right_hand |= set(keyboard_layout[start : start + 5])
    keyboards[keyboard_name]["right hand"] = right_hand
    keyboards[keyboard_name]["inner columns"] = {
        keyboard_layout[4],
        keyboard_layout[5],
        keyboard_layout[14],
        keyboard_layout[15],
        keyboard_layout[24],
        keyboard_layout[25],
    }

scores = {name: 0 for name in keyboard_layouts}
keys = {}
for keyboard_name, keyboard in keyboards.items():
    for (last_key, key), total in transitions.items():
        keys[key] = keys.get(key, 0) + total
        score = 0
        if key not in keyboard["all keys"]:
            score += penalties["missing"]
        else:
            same_hand_penalty = 0
            for hand in "left hand", "right hand":
                if last_key in keyboard[hand] and key in keyboard[hand]:
                    same_hand_penalty = penalties["same hand"]
                    break
            score += same_hand_penalty

            if key in keyboard["top row"]:
                score += penalties["top row"]
                if key in keyboard["inner columns"]:
                    score += penalties["inner column, top row (delta)"]
            elif key in keyboard["bottom row"]:
                score += penalties["bottom row"]
                if key in keyboard["inner columns"]:
                    score += penalties["inner column, bottom row (delta)"]
            elif key in keyboard["inner columns"]:  # Must be home row
                score += penalties["inner column, home row (delta)"]
        scores[keyboard_name] += score * total

print("Key usage (higher is better):")
key_ranking = list(
    map(
        lambda k: k if k.isprintable() else repr(k),
        sorted(keys, key=keys.get, reverse=True),
    )
)
print(" ".join(key_ranking))

print()
print("Scores (lower is better):")
prev_score = None
top_score = None
for name, score in sorted(scores.items(), key=operator.itemgetter(1)):
    if not prev_score:
        top_score = score
        prev_score = score
        diff = 0
    else:
        diff = score - top_score
    print(f"  {score:,} ({diff/top_score * 100:4.1f}%) : {name}")
