# I struggled a lot. But I learned a lot more!

From dawn to noon. 7 Hours, Red eyes. A headache. Pure frustration. Many failures, over and over, I'd fix one thing, run it, and something else would break. I'd fix that, and another one would show up. Again and again, for hours, until I genuinely felt tortured by my own code. I kept going anyway, and came out understanding logic and programming in a way I never would have by getting it right the first time. I struggled very hard, but the achievement at the end made it worth every second.

The goal sounded simple: draw a 3×3 field of grass, ask the user for a row and a column, and place a rabbit there. I challenged myself to do this project by myself, After learning the basics about: nested list, string parsing, boolean logic, and operator precedence. This project needs all these things, all stacked on top of each other — and I hit almost every single trap that combination has to offer.

There's also a pattern running underneath all twelve versions that I only noticed at the end: almost every single time, I was staring so hard at one specific error that I stopped paying attention to everything else around it. I'd fix exactly the line that was broken, feel a flash of relief, run the code again — and discover I'd quietly broken something else nearby, sometimes something much simpler than the bug I'd just solved. Tunnel vision, over and over. You'll see it happen many times below:


## Version 1 — starting from a place of total confusion

```python
user_number = [input("Please choose a row and a column: \n")]
if user_number[0] == 1 or user_number[0] == 2 or user_number[0] == 3:
    if user_number[1] == 1 or user_number[1] == 2 or user_number[1] ==3:
        total_list.insert(user_number[0] and user_number[1], "🐇")
```

I wrapped the input in a list (`[input(...)]`), which meant `user_number` only ever had **one** item in it — `user_number[1]` didn't exist yet, and I hadn't noticed. I compared a string like `"1"` against the number `1` (never equal — Python doesn't consider them the same thing). And I tried to use `.insert(user_number[0] and user_number[1], ...)`, genuinely believing `and` would combine two values into one position. It doesn't. It never did.

## Version 2 — a different way to be wrong

```python
user_number = int(input("Please choose a row and a column: \n"))
row = user_number[0]
```

I tried converting the whole input straight to an integer. That immediately broke the idea of "indexing into it" — you can't do `some_integer[0]`, because a plain number isn't a sequence of anything. `int` was the wrong tool here, and it took actually running this to understand why. I was so focused on getting rid of the string-vs-number mismatch from version 1 that I didn't notice I'd just made indexing impossible altogether.

## Version 3 — closer, still wrong

I went back to treating the input as a plain string and indexing into its characters — `user_number[0]`, `user_number[1]` — which was the right idea. But I was still comparing those characters to bare numbers (`== 1`, `== 2`, `== 3`) instead of the strings `"1"`, `"2"`, `"3"`. The whole condition quietly failed every time, and I didn't understand yet why nothing was happening. I'd been so locked in on fixing the indexing problem that I completely forgot the comparison lines underneath it needed fixing too — they'd been wrong since version 1 and I just hadn't gotten to them yet.

## Version 4 — the string comparison finally clicks

Changed `== 1` to `== "1"` across the board. Small change, huge difference — this is the version where I actually understood that a character typed by the user is *always* a string, never a number, until I explicitly convert it. This is the one version where fixing the thing I was focused on didn't break anything else — a rare clean win in this whole story.

## Version 5 — a new bug hiding in plain sight

I cleaned up the structure with a proper `if`/`else`, and I was mostly focused on making the printed output nicer, splitting the grid across separate lines. While I was busy improving how it looked, I didn't notice that my `else` only attached to the **outer** `if` (checking the first digit). If the first digit was valid but the second digit wasn't, my program did... nothing. No rabbit, no error message, total silence. Focusing on the display cost me the control-flow correctness underneath it — a bug that doesn't crash and doesn't shout at you is somehow worse than one that does.

## Version 6 — the `and`/`or` trap

Trying to fix version 5's silent failure, I decided to combine both checks into a single line, so the `else` would definitely catch a bad digit no matter which one it was:

```python
if number[0] =="1" or number[0] =="2" or number[0] =="3" and number[1] =="1" or number[1] =="2" or number[1] =="3":
```

This looks reasonable to a human eye. It is not reasonable to Python. `and` silently binds *tighter* than `or`, so this doesn't mean what it looks like it means at all — it means something closer to "first digit is 1, OR first digit is 2, OR (first digit is 3 AND second digit is 1), OR second digit is 2, OR second digit is 3." Almost any input satisfied it. I was so focused on solving the "silent failure" bug that I introduced a much bigger one in the exact same line — I just couldn't see it yet because it "looked right."

## Version 7 — parentheses save the day

```python
if (number[0] =="1" or number[0] =="2" or number[0] =="3") and (number[1] =="1" or number[1] =="2" or number[1] =="3"):
```

Wrapping each group in its own parentheses forced Python to check "is the first digit valid" as one complete thought, and "is the second digit valid" as another, then combine those two *results* with `and`. This is the version where operator precedence stopped being an abstract warning and became something I'd actually been burned by.

## Version 8 — two steps forward, one step way back

Trying to add a length check on top of a version that finally worked, I wrote `len(number) == "2"` — comparing a number (`len()` always returns an integer) to the string `"2"`. Never true. On top of that I wrote `field=[int(number[0])-1][int(number[1])-1]`, which doesn't touch my actual grid at all — it builds a brand-new one-item list and indexes into *that*, then overwrites my entire `field` variable with garbage. I was so focused on adding this one new safety check that I didn't notice I'd broken the placement logic that had just started working in version 7. This version made things actively worse while I was trying to make them better.

## Version 9 — copy-paste confusion

```python
row = int(field[0])
column = int(field[1])
field = [row-1][column-1] = "🐇"
```

Trying to fix version 8's broken indexing, I accidentally typed `field[0]` where I meant `number[0]` — trying to convert an entire row of grass emojis into an integer, which can't work. And I chained an assignment across two bracketed expressions in a way that doesn't do what I wanted at all, once again destroying my own grid variable in the process. I was staring so hard at "how do I index correctly" that I stopped noticing which variable name I was even typing. This is the point where my head genuinely started hurting and I had to step away for a bit.

## Version 10 — the bug that deserves its own paragraph

```python
if len(number) == 2 and number[0] in ["1","2","3"] and number[1] in ["1","2","3"]:
    row = int(number[0])
    column = int(number[1])
    field [row-1 and column-1] = "🐇"
```

Two things happened here at once. The good news: I finally wrote clean validation, using `len(number) == 2` (comparing int to int, correctly this time) and `in ["1","2","3"]` instead of long chains of `or`. The bad news: `field[row-1 and column-1]` — I genuinely believed `and` here meant "do both of these at the same time," like plain English. It doesn't. This is the clearest example of the tunnel-vision pattern in the whole file: I put so much focus into finally getting the validation line right that I didn't give the placement line — one bracket below it — any real attention at all, and it quietly broke in a way I didn't even notice until I tested it. It's not a small typo, it's a real misunderstanding of what `and` actually is, and it cost me more confusion than almost anything else in this entire file.

## Version 11 — it finally works

```python
field [row-1][column-1] = "🐇"
```

Two separate brackets. Two separate coordinates. That's what a 2D list actually needs — not one merged expression, but one index for the row, and a second index into *that row* for the column. Paired with the validation from version 10, this is the first version that placed the rabbit correctly, every time, for real inputs and bad ones alike.

## Version 12 — the finish line

Just a capitalization fix on the welcome message. Nothing left to fix. I sat back and actually felt it.

## What I learned

- **A 2D list is a list of lists.** To reach a single cell you need two separate indexes, `field[row][col]` — not one combined value.
- **Operator precedence is real and it is silent.** `and` binds tighter than `or`. Without parentheses, a condition that reads correctly to a human can mean something completely different to Python — and it won't warn you.
- **A character from `input()` is always a string.** Comparing it to a bare number, or converting the whole input to `int` before you're ready to index into it, breaks in two very different ways — I managed to hit both.
- **`in ["1","2","3"]` beats a long chain of `or`.** Once I saw it, I couldn't unsee how much cleaner it was than three separate equality checks.
- **A silent bug is scarier than a crash.** The version where a bad second digit just... did nothing, taught me that "it didn't crash" is not the same as "it works."
- **Tunnel vision is a real cost, not just a phrase.** Almost every version in this file was me fixing exactly the error in front of me and, in doing so, losing track of something else nearby — sometimes something much simpler than the bug I was solving. Discovering an error made me focus so hard on that one line that everything around it stopped getting checked. That habit, more than any single Python concept, is the thing I most want to be careful about on my next project.

Twelve versions, real headache, real red eyes, real frustration — I struggled hard on this one, but I came out the other side understanding logic and programming in a way I never would have by getting it right the first time. Every wrong turn taught me something the easy path never could have, and the achievement at the end made all of it worth it.
