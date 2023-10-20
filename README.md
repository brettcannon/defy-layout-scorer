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
This was a quick hack to see if [Colemak Mod-DH](https://colemakmods.github.io/mod-dh/) scored well enough for me to keep learning it (which it did).

The `compare.py` script will also output the most used characters to help you make any decisions about your keyboard layers.

### Keyboard layouts

The keyboards are stored in the `keyboard_layouts` dict.
You can add any other keyboards you want and they will automatically be included in any future runs for the `compare.py` script.
The built-in layouts are:

1. QWERTY
2. [Dvorak](https://en.wikipedia.org/wiki/Dvorak_keyboard_layout)
3. [Dvorak (Programmer)](https://en.wikipedia.org/wiki/Dvorak_keyboard_layout#Programmer_Dvorak)
4. [Colemak](https://colemak.com)
5. [Colemak Mod-DH](https://colemakmods.github.io/mod-dh/)
6. [Colemak Mod-DHk](https://colemakmods.github.io/mod-dh/)
7. [Halmak](https://github.com/kaievns/halmak)
8. [Workman](https://workmanlayout.org)
9. [Norman](https://normanlayout.info)
10. [Carpalx (QFMLWY)](http://mkweb.bcgsc.ca/carpalx/)
11. [Canary](https://github.com/apsu/canary)

## Example
```text
Key usage (higher is better):
  e t o a i n s r h l p c d u '\n' m y g f . w b " , v / _ k ( ) - : 1 x ' 0 = 2 3 [ ] j 6 4 q 5 8 > z # 7 ^ * ! 9 ? + { } ` ; % < @ ~ & $ \ | '\t'

Scores (lower is better):
  3,486,968 ( 0.0%) : Colemak Mod-DH
  3,488,701 ( 0.0%) : Colemak Mod-DHk
  3,512,914 ( 0.7%) : Canary
  3,537,332 ( 1.4%) : Halmak
  3,538,483 ( 1.5%) : Colemak
  3,557,923 ( 2.0%) : Norman
  3,589,561 ( 2.9%) : Workman
  3,683,999 ( 5.7%) : Carpalx (QFMLWY)
  3,685,740 ( 5.7%) : Dvorak
  3,686,445 ( 5.7%) : Dvorak (Programmer)
  4,110,397 (17.9%) : QWERTY
```
