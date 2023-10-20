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
You can change the values in the `penalties` dict to use your own weights based on your own preferences.
Do note that some penalty values are absolute while others are deltas added to other penalties
(e.g., "top row" is the absolute penalty for any key on the top row, while "inner column, top row (delta)" gets added to "top row").

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

## Example
```text
Key usage (higher is better):
  e t o a i n s r h l p c d u '\n' m y g f . w b " , v / _ k ( ) - : 1 x ' 0 = 2 3 [ ] j 6 4 q 5 8 > z # 7 ^ * ! 9 ? + { } ` ; % < @ ~ & $ \ | '\t'

Scores (lower is better):
  5,087,383 ( 0.0%) : Halmak
  5,151,684 ( 1.3%) : Colemak
  5,163,886 ( 1.5%) : Colemak Mod-DH
  5,198,556 ( 2.2%) : Colemak Mod-DHk
  5,208,624 ( 2.4%) : Dvorak
  5,211,170 ( 2.4%) : Norman
  5,215,668 ( 2.5%) : Dvorak (Programmer)
  5,414,568 ( 6.4%) : Workman
  5,493,109 ( 8.0%) : Carpalx (QFMLWY)
  6,544,124 (28.6%) : QWERTY
```
