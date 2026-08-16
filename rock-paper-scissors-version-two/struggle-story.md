## Four full rewrites, from noon to night, red eyes and a headache.

I built this right after Place the Rabbit — same day, no real break in between, just noon straight into night. And I built it the way I seem to build everything when a bug won't let go of me: I don't patch it. I rewrite the entire project from scratch. Every single time. Four versions of this game exist because four times, something was wrong, and four times, instead of hunting for the one broken line, I sat back down and started over completely — partly to fix it, partly because starting over is the only way I actually force myself to sit with the logic long enough to understand it, instead of just patching around what I don't yet get.

## Version 1 — the first full attempt

I nested the whole win-check inside `if user_choice in right_choices:`, and built my win logic as a tuple of separate one-item lists:

```python
wins_computer = [computer_choice =="paper" and user_typed =="rock"], [computer_choice =="rock" and user_typed =="scissors"],[computer_choice=="scissors" and user_typed =="paper"]
if len(computer_choice) == len(user_typed):
```

I was comparing the computer's move against `user_typed` — a leftover variable from an entirely different question earlier in the script, not the player's actual rock/paper/scissors move. The whole win check was built on the wrong piece of data from the very start.

## Version 2 — rewritten from scratch, still not right

I scrapped it and rebuilt it. This time I compared against the correct variable, `user_choice` — but the deeper structural issues were still there. The tie check compared the *lengths* of the words instead of the words themselves, and `wins_computer` was still that same tangled tuple of separate lists, which meant `elif wins_computer:` was true no matter what actually happened in the game. It ran. It even looked like it worked, most of the time. It wasn't actually checking what I thought it was checking.

## Version 3 — rewritten again

Full rewrite, again. This time I pulled the win-check logic out of that nested structure entirely and rebuilt it as one real boolean expression, wrapped in a genuine list, checked with `any()`:

```python
computer_wins = [
    (computer_choice == "scissors" and user_choice == "paper") or
    (computer_choice == "paper" and user_choice == "rock") or
    (computer_choice == "rock" and user_choice == "scissors")
]
if any(computer_wins):
```

This one actually worked. But it still didn't feel clean — I was wrapping something in a list just to unwrap it again with `any()`, and something about that felt like I hadn't fully landed the idea yet.

## Version 4 — the version I kept

One more full rewrite. Same win logic, no list, no `any()` — just a direct boolean check:

```python
computer_wins = (
    (computer_choice == "scissors" and user_choice == "paper") or
    (computer_choice == "paper" and user_choice == "rock") or
    (computer_choice == "rock" and user_choice == "scissors")
)
tie = computer_choice == user_choice
if computer_wins:
    print("THE RESULT IS: YOU LOSE")
elif tie:
    print("THE RESULT IS: TIE")
else:
    print("THE RESULT IS: YOU WIN!")
```

## What I learned

Four complete rewrites, in one stretch, from noon to night, right after the hardest project I'd built up to that point. It took a great deal of time, and a lot of starting over — but starting over was never wasted. Every version taught me something the last one hadn't, and by the fourth one, I finally understood the logic instead of just getting it to run.
