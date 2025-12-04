"""Compare various keyboard layouts for the Dygma Defy keyboard."""
import operator
import pickle
import secrets

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
                "zxmcvkl,./"),
    # https://normanlayout.info
    "Norman": ("qwdfkjurl;"
               "asetgynioh"
               "zxcvbpm,./"),
    # http://mkweb.bcgsc.ca/carpalx/
    "Carpalx (QFMLWY)": ("qfmlwyuobj"
                         "dstnriaeh;"
                         "zvgcxpk,./"),
    "Carpalx (QGMLWB)": ("QGMLW" "BYUV;"
                         "DSTNR" "IAEOH"
                         "ZXCFJ" "KP,./"),
    "Carpalx (QYLDGB)": ("QYLDGBMUWJ"
                         "RITOSHAEN;"
                         "XKCVZPF,./"),
    # https://github.com/apsu/canary
    "Canary": ("wlypbzfou'"
               "crstgmneia"
               "qjvdkxh/,."),
    # https://deskthority.net/wiki/Alternative_keyboard_layouts#Evolved
    "Evolved": ("K,UYP" "WLMFC"
                "OAEID" "RNTHS"
                "Q.';Z" "XVGBJ"),
    # https://deskthority.net/wiki/Alternative_keyboard_layouts#Blick_DHIATENSOR
    "Blick DHIATENSOR": ("'PWFU" "LCMY/"
                         "DHIAT" "ENSOR"
                         "ZXKGB" "VQJ,."),
    # https://deskthority.net/wiki/Alternative_keyboard_layouts#3l
    "3I": ("QFUYZ" "XKCWB"
           "OHEAI" "DRTNS"
           ",M.J;" "GLPV"),
    # https://deskthority.net/wiki/Alternative_keyboard_layouts#The_Capewell_Layout
    # http://www.michaelcapewell.com/projects/keyboard/layout_capewell.htm
    "Capewell": (".YWDF" "JPLUQ"
                 "AERSG" "BTNIO"
                 "XZCV;" "KWH,'"),
    # https://mathematicalmulticore.wordpress.com/2010/06/21/mtgaps-keyboard-layout-2-0/
    "MTGAP’s Layout 2.0": (",FHDKJCUL."
                           "OANTGMSERI"
                           "QXBPZYW'V;"),
    # https://mathematicalmulticore.wordpress.com/rate-these-keyboard-layouts/
    "Phynnboi": ("QY.;,JCLFX"
                 "HOEAUGTSNR"
                 "P/KIZWDMVB"),
    # https://kennetchaz.github.io/symmetric-typing/soul.html
    "Soul": ("qwldp" "kmuy;"
             "arstg" "fneio"
             "jzxcv" "bh,./"),
    # http://www.minimak.org
    "Minimak": ("qwdrkyuiop"
               "astfghjel;"
               "zxcvbnm,./"),
    # https://millikeys.sourceforge.net/asset/
    "Asset": ("qwjfgypul;"
              "asetdhnior"
              "zxcvbkm,./"),
    # https://github.com/Apsu/APT
    "APT": ("wgdfbqluoy"
            "rsthkjneai"
            "xcmpvz,.'/"),
    # https://github.com/rdavison/graphite-layout
    "Graphite": ("bldwz"  "'fouj"
                 "nrtsg"  "yhaei"
                 "qxmcv"  "kp.-/"),
    # https://www.reddit.com/r/KeyboardLayouts/comments/oehliv/comment/h4ah6tp/?utm_name=iossmf&context=3
    "16-Maks": ("qwudfkloyp"
                "rsetghnaic"
                "zx;vbjm,./"),
    # https://ballerboo.github.io/boolayout/
    "Boo": (",.ucv" "qfdly"
            "aoesg" "bntri"
            ";x'wz" "phmkj"),
    # https://engram.dev/
    "Engram": ("byou'" "ldwvz"
               "ciea," "htsnq"
               "gxjk-" "?rmfp"),
    # https://elliotgeorge.net/2018/11/22/the-kaehi-keyboard-layout/
    "Kaehi": ("qwldgjuop/"
              "nrstmkaehi"
              "zxcvbyf,.;"),
    # https://geekhack.org/index.php?topic=67604.0
    "OneProduct": ("pldwg" "jxoyq"
                   "nsrtm" "uaeih"
                   "zcfvb" ",.?;k"),
    # https://xsznix.wordpress.com/2016/05/16/introducing-the-rsthd-layout/
    # https://www.keyboard-design.com/letterlayout.html?layout=rsthd-2.en.matrix
    "RSTHD": ("jcyfk" "zl,uq"
              "rsthd" "mnaio"
              "/vgpb" "xw.;-"),
    # https://oxey.dev/sturdy/index.html
    "Sturdy": ("vmlcp" "xfouj"
               "strdy" ".naei"
               "zkqgw" "bh';,"),
    # https://www.keyboard-design.com/letterlayout.html?layout=dsend-thumbshift.en.ergodox
    "Dsend thumbshift": ("xclfv" "/;upq"
                         "rsntg" ",aehi"
                         "zwmdb" ".oykj"),
    # https://www.keyboard-design.com/letterlayout.html?layout=beakl-4-mod-ian-1.en.ergodox
    "Beakl 4 mod ian 1": ("kyo.q" "fclpz"
                          "hieau" "dstnr"
                          "j\"'," "wgmbv"),
    # https://www.keyboard-design.com/letterlayout.html?layout=poqtea.en.ergodox
    "Poqtea": ("ywflm" "kpoq'"
               "ursnh" "dteai"
               "zxcvj" "bg,.;"),
    # https://www.keyboard-design.com/letterlayout.html?layout=hands-down-reference-ts.en.ergodox
    "Hands Down reference": ("qchpv" "kyoj'"
                             "rsntg" "wueai"
                             "xmldb" "zf/,."),
    # https://www.keyboard-design.com/letterlayout.html?layout=hands-down-alt-ts.en.ergodox
    "Hand Down alt ts": ("wchpv" "'yujq"
                         "rsntg" "kieoa"
                         "xmldb" "zf/,."),
    # https://github.com/GalileoBlues/Gallium
    "Gallium": ("bldcv" "jfou,"
                "nrtsg" "yhaei"
                "xqmwz" "kp';."),
}

keyboard_layouts = {name: layout.lower() for name, layout in keyboard_layouts.items()}

penalties = {
    "same hand": 0,
    "missing": 2,
    "same finger": 0,
}

effort_grid = (
# From Colemak Mod-DH.
#     3.0, 2.4, 2.0, 2.2, 3.2,   3.2, 2.2, 2.0, 2.4, 3.0,  # Top row
#     1.6, 1.3, 1.1, 1.0, 2.9,   2.9, 1.0, 1.1, 1.3, 1.6,  # Home row
#     3.2, 2.6, 2.3, 1.6, 3.0,   3.0, 1.6, 2.3, 2.6, 3.2,  # Bottom row
# From Workman.
#     4.0, 2.0, 2.0, 3.0, 4.0,   4.0, 3.0, 2.0, 2.0, 4.0,  # Top row
#     1.5, 1.0, 1.0, 1.0, 3.0,   3.0, 1.0, 1.0, 1.0, 1.5,  # Home row
#     4.0, 4.0, 3.0, 2.0, 4.0,   4.0, 2.0, 3.0, 4.0, 4.0,  # Bottom row
# Personal.
     4.0, 2.2, 2.0, 3.0, 4.0,   4.0, 3.0, 2.0, 2.2, 4.0,  # Top row
     1.5, 1.2, 1.0, 1.0, 2.0,   2.0, 1.0, 1.0, 1.2, 1.5,  # Home row
     4.0, 4.0, 2.5, 2.0, 4.0,   4.0, 2.0, 2.5, 4.0, 4.0,  # Bottom row

)
# fmt: on


def score_keyboard(keyboard_layout, transitions):
    keyboard = {"all keys": set(keyboard_layout)}

    keyboard["top row"] = set(keyboard_layout[:10])
    keyboard["bottom row"] = set(keyboard_layout[-10:])
    left_hand = set()
    for start in range(0, 30, 10):
        left_hand |= set(keyboard_layout[start : start + 5])
    keyboard["left hand"] = left_hand
    right_hand = set()
    for start in range(5, 30, 10):
        right_hand |= set(keyboard_layout[start : start + 5])
    keyboard["right hand"] = right_hand
    keyboard["inner columns"] = {
        keyboard_layout[4],
        keyboard_layout[5],
        keyboard_layout[14],
        keyboard_layout[15],
        keyboard_layout[24],
        keyboard_layout[25],
    }
    keyboard["columns"] = [set(keyboard_layout[i::10]) for i in range(10)]
    keyboard["effort"] = dict(zip(keyboard_layout, effort_grid))

    total_score = 0
    for (last_key, key), total in transitions.items():
        score = 0
        if not key.isalpha():
            continue
        elif key not in keyboard["all keys"]:
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

        total_score += score * total

    return total_score


def key_frequency(transitions):
    keys = {}
    for (last_key, key), total in transitions.items():
        keys[key] = keys.get(key, 0) + total

    print("Key usage (higher is better):")
    key_ranking = list(
        map(
            lambda k: k if k.isprintable() else repr(k),
            sorted(keys, key=keys.get, reverse=True),
        )
    )
    print(" ".join(key_ranking))


def score_predefined_keyboards(transitions):
    scores = {}
    for layout in keyboard_layouts.values():
        scores[layout] = score_keyboard(layout, transitions)

    print("Scores (lower is better):")
    layout_names = {layout: name for name, layout in keyboard_layouts.items()}
    prev_score = None
    top_score = None
    predefined_keyboards = sorted(scores.items(), key=operator.itemgetter(1))
    for layout, score in predefined_keyboards:
        if not prev_score:
            top_score = score
            prev_score = score
            diff = 0
        else:
            diff = score - top_score
        name = layout_names[layout]
        print(f"  {int(score):,} ({diff/top_score * 100:4.1f}%) : {name}")

    return predefined_keyboards[0]


def improve_layout(transitions, best_layout, best_score):
    print("Looking for a better layout...")
    initial_best_score = best_score
    scores = {best_layout: best_score}
    try:
        while True:
            new_layout = list(best_layout)
            swap_1 = secrets.randbelow(len(best_layout))
            swap_2 = secrets.randbelow(len(best_layout))
            if swap_1 == swap_2:
                print("x", end="", flush=True)
                continue
            new_layout[swap_1], new_layout[swap_2] = (
                new_layout[swap_2],
                new_layout[swap_1],
            )
            new_layout_key = "".join(new_layout)
            if new_layout_key in scores:
                print("=", end="", flush=True)
                continue
            scores[new_layout_key] = score_keyboard(new_layout, transitions)
            if scores[new_layout_key] < best_score:
                best_layout = new_layout
                best_score = scores[new_layout_key]
                diff = scores[new_layout_key] - initial_best_score
                print(
                    f"\n{int(best_score):,} ({diff/scores[new_layout_key] * 100:4.1f}%): {best_layout}"
                )
            else:
                print(".", end="", flush=True)
    except KeyboardInterrupt:
        print("\n\nBest layout found:")
        diff = best_score - initial_best_score
        print(f"{int(best_score):,} ({diff/best_score * 100:4.1f}%): {best_layout}")


def main():
    with open("transitions.pickle", "rb") as file:
        transitions = pickle.load(file)

    print()
    key_frequency(transitions)

    print()
    best_layout, best_score = score_predefined_keyboards(transitions)

    print()
    improve_layout(transitions, best_layout, best_score)


if __name__ == "__main__":
    main()
