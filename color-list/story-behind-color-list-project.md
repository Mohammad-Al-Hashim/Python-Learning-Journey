# What I learned: a variable only ever holds one value

I built this project twice, on purpose — the first version taught me something, and the second version is me applying that lesson correctly.

## First version

```python
colors = []
first_color = input("Add the first color you like: ")
user_choice = input("Do you want to add more colors? type Yes Or No: ").lower()
if user_choice == "yes" or user_choice == "no":
    if user_choice == "yes":
        second_color = input("Add another color to the list: ")
        colors.append(first_color)
        colors.append(second_color)
        print(f"The colors you like are: {colors}")
    else:
        colors.append(first_color)
        print(f"The colors you like are: {colors}")
else:
    print("You must type either yes or no. Try again")
```

This version works — no bugs. But look closely: `colors.append(first_color)` shows up **twice**, once inside the "yes" branch and once inside the "no" branch. I wrote it that way because I only appended `first_color` *after* I already knew what the user wanted to do next. That meant I had to remember to do it in both places, or risk forgetting it in one of them.

That repetition made me stop and ask a question that turned out to matter a lot: *why does `first_color` need to be appended so carefully, in exactly the right spot, every single time?*

## The lesson

A variable can only hold **one value at a time**. Every time you write something new into it, the old value is gone — completely erased, like writing over a sticky note. So if I reuse a variable for something else without saving its current value into a list first, that value is lost forever, with no way to get it back.

A **list** works differently. It's a variable that can hold many values at once, in order, and once something is appended to it, it stays there permanently — nothing that happens to the original variable afterward can erase it.

So the real question, any time I'm about to reuse a variable, became: *"have I already saved this value somewhere safe?"*

I also ran into a smaller but sneaky bug along the way: I had written `.lower` without the parentheses (`input(...).lower` instead of `input(...).lower()`). Without `()`, Python doesn't run the method — it just refers to it as an object. So `user_choice` never actually became the string `"yes"` or `"no"`, and typing "yes" fell straight through to my `else` branch every time. That was a good reminder that **methods need `()` to actually execute** — leaving them off means you're pointing at the tool, not using it.

## Second version — applying the lesson

```python
colors = []
best_color = input("Add the first color you like: ")
colors.append(best_color)
user_choice = input("Do you want to add more colors? type Yes Or No: ").lower()
if user_choice == "yes" or user_choice == "no":
    if user_choice == "no":
        print(f"The colors you like are: {colors}")
    else:
        best_color = input("Add another color to the list: ")
        colors.append(best_color)
        print(f"The colors you like are: {colors}")
else:
    print("You must type either yes or no. Try again")
```

Here, I append `best_color` into `colors` **immediately** after collecting it — right after the first `input()`, before anything else has a chance to overwrite it, and before I even know what the user is going to choose next. That means I only need one `.append()` call for the first color, not two duplicated ones tucked inside separate branches.

Later, if the user wants to add a second color, I reuse the exact same variable name (`best_color`) for the new input. That's completely safe now, because the first value is already locked away inside `colors` — reusing `best_color` afterward can't touch or erase what's already been saved.

## The core idea

A normal variable holds exactly one value, and reusing it means losing whatever was there before. The safest habit is to append a value into permanent storage (a list) the moment you're done needing it in its temporary variable — not later, and not conditionally in multiple different places, since that's exactly where a value can accidentally slip through and get lost.
