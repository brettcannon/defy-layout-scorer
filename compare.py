"""Compare various keyboard layouts for the Dygma Defy keyboard."""
import operator
import pickle

# fmt: off
keyboard_layouts = {
    "QWERTY": ("qwertyuiop"
               "asdfghjkl;"
               "zxcvbnm,./"),
    # https://en.wikipedia.org/wiki/Dvorak_keyboard_layout
    "Dvorak": ("',.pyfgcrl"
               "aoeuidhtns"
               ";qjkxbmwvz"),
    # https://en.wikipedia.org/wiki/Dvorak_keyboard_layout#Programmer_Dvorak
    "Dvorak (Programmer)": (";,.pyfgcrl"
                            "aoeuidhtns"
                            "'qjkxbmwvz"),
    # https://colemakmods.github.io/mod-dh/
    "Colemak Mod-DH": ("qwfpbjluy;"
                       "arstgmneio"
                       "zxcdvkh,./"),
    "Colemak Mod-DHk": ("qwfpbjluy;"
                        "arstgkneio"
                        "zxcdvmh,./"),
    # https://colemak.com
    "Colemak": ("qwfpgjluy;"
                "arstdhneio"
                "zxcvbkm,./"),
    # https://github.com/kaievns/halmak
    "Halmak": ("wlrbz;qudj"
               "shnt,.aeoi"
               "fmvc/gpxky"),
    # https://workmanlayout.org
    "Workman": ("qdrwbjfup;"
                "ashtgyneoi"
                "zxmcvkl<>?"),
    # https://normanlayout.info
    "Norman": ("qwdfkjurl;"
               "asetgynioh"
               "zxcvbpm,./"),
    # http://mkweb.bcgsc.ca/carpalx/
    "Carpalx (QFMLWY)": ("qfmlwyuobj"
                         "dstnriaeh;"
                         "zvgcxpk,./"),
    # https://github.com/apsu/canary
    "Canary": ("wlypbzfou'"
               "crstgmneia"
               "qjvdkxh/,."),
}

penalties = {
    "same hand": 0,
    "missing": 5,
    "same finger": 1,
}

# From Colemak Mod-DH.
effort_grid = (
    3.0, 2.4, 2.0, 2.2, 3.2,   3.2, 2.2, 2.0, 2.4, 3.0,  # Top row
    1.6, 1.3, 1.1, 1.0, 2.9,   2.9, 1.0, 1.1, 1.3, 1.6,  # Home row
    3.2, 2.6, 2.3, 1.6, 3.0,   3.0, 1.6, 2.3, 2.6, 3.2,  # Bottom row
)
# fmt: on


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
    keyboards[keyboard_name]["columns"] = [
        set(keyboard_layout[i::10]) for i in range(10)
    ]
    keyboards[keyboard_name]["effort"] = dict(zip(keyboard_layout, effort_grid))

scores = {name: 0 for name in keyboard_layouts}
keys = {}
for keyboard_name, keyboard in keyboards.items():
    for (last_key, key), total in transitions.items():
        keys[key] = keys.get(key, 0) + total

        score = 0
        if key not in keyboard["all keys"]:
            score += penalties["missing"]
        else:
            score += keyboard["effort"][key]

            same_hand_penalty = 0
            for hand in "left hand", "right hand":
                if last_key in keyboard[hand] and key in keyboard[hand]:
                    same_hand_penalty = penalties["same hand"]
                    break
            score += same_hand_penalty

            same_finger_penalty = 0
            if last_key != key:
                for column in keyboard["columns"]:
                    if all(key in column for key in (last_key, key)):
                        same_finger_penalty = penalties["same finger"]
                        break
            score += same_finger_penalty

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
    print(f"  {int(score):,} ({diff/top_score * 100:4.1f}%) : {name}")
