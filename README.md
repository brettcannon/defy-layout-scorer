# Defy keyboard layout scorer

## Step 1 -- create corpus
Pass the paths to files you want to have be included in your corpus to the `transitions.py` file. E.g.,

```python
python3 transitions.py Documents/**/*.txt ~/Repositories/brettcannon/**/*.py ~/Repositories/brettcannon/**/*.md
```

This will generate a `transitions.pickle` file which compares character pairs: the previous character and the (current) character.

## Step 2 -- analyze data

Run the `compare.py` file:
```python
python3 compare.py
```

This will calculate a score for each keyboard layout.
The lower the score the better (i.e., points are penalties), with each keyboard sorted from "best" to "worst" along with a percentage difference of the score from the "best" keyboard.
You can change the values in the `penalties` dict and `efforts` tuple to use your own weights based on your own preferences.

Do note that the scoring is very simple and very much oriented towards a columnar/matrix keyboard layout!
Take the time to tweak the effort grid and any other metrics to your personal preference.

The `compare.py` script will also output the most used characters to help you make any decisions about your keyboard layers.

### Keyboard layouts

The keyboards are stored in the `keyboard_layouts` dict.
URLs are provided in a comment for each layout if you want to look up more
information.
You can add any other keyboards you want and they will automatically be included in any future runs for the `compare.py` script.

## Example
```text
Key usage (higher is better):
  e t o a i n s r h l p c d u '\n' m y g f . w b " , v / _ k ( ) - : 1 x ' 0 = 2 3 [ ] j 6 4 q 5 8 > z # 7 ^ * ! 9 ? + { } ` ; % < @ ~ & $ \ | '\t'

Scores (lower is better):
  1,619,338 ( 0.0%) : Workman
  1,641,154 ( 1.3%) : MTGAP’s Layout 2.0
  1,644,484 ( 1.6%) : Graphite
  1,644,773 ( 1.6%) : Colemak Mod-DH
  1,654,541 ( 2.2%) : Capewell
  1,655,320 ( 2.2%) : Canary
  1,655,766 ( 2.2%) : Dsend thumbshift
  1,660,312 ( 2.5%) : Carpalx (QGMLWB)
  1,664,793 ( 2.8%) : Colemak
  1,668,011 ( 3.0%) : Norman
  1,670,890 ( 3.2%) : Soul
  1,679,443 ( 3.7%) : Colemak Mod-DHk
  1,681,960 ( 3.9%) : Asset
  1,684,285 ( 4.0%) : Beakl 4 mod ian 1
  1,688,283 ( 4.3%) : Hand Down alt ts
  1,690,256 ( 4.4%) : 3I
  1,690,604 ( 4.4%) : RSTHD
  1,692,134 ( 4.5%) : Phynnboi
  1,698,387 ( 4.9%) : Boo
  1,704,921 ( 5.3%) : Kaehi
  1,714,026 ( 5.8%) : Hands Down reference
  1,726,662 ( 6.6%) : 16-Maks
  1,732,051 ( 7.0%) : Carpalx (QYLDGB)
  1,736,475 ( 7.2%) : Halmak
  1,736,633 ( 7.2%) : Poqtea
  1,750,658 ( 8.1%) : OneProduct
  1,766,414 ( 9.1%) : Sturdy
  1,778,687 ( 9.8%) : Evolved
  1,790,726 (10.6%) : APT
  1,802,712 (11.3%) : Carpalx (QFMLWY)
  1,819,673 (12.4%) : Dvorak
  1,819,673 (12.4%) : Dvorak (Programmer)
  1,839,138 (13.6%) : Blick DHIATENSOR
  1,857,501 (14.7%) : Engram
  2,055,836 (27.0%) : Minimak
  2,418,032 (49.3%) : QWERTY
```
