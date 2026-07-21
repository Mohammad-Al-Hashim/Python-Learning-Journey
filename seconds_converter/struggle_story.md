I built a program that converts a total number of seconds (entered by the user) into hours, minutes, and remaining seconds.

This project depends upon two operators: Floor division (//) — divides two numbers and keeps only the whole number result, dropping any remainder.
Modulo (%) — gives you the remainder left over after division. 

Before deeply understanding the modulo operator, I was trying to build the seconds converter program. Here is what I did:

First mistake: defining the minutes variable, instead of: minutes = total_seconds%3600//60 I wrote: minutes = total_seconds//60. The problem: this calculated the total minutes contained in the entire input — not just the minutes left over after the hours were already removed.
The fix: first take away the hours from the total seconds, and then take away the minutes from the leftover seconds after taking away hours, not taking away minutes from the total seconds.

Second mistake: Subtracting different units directly. Instead of writing: remain_seconds=total_seconds%60
I wrote: remain_seconds = total_seconds - (hours + minutes). 
This is totally wrong: I subtracted the count of hours and the count of minutes directly from the total_seconds, but those counts aren't measured in seconds. That is like trying to subtract kilometers from meters. 
The fix: uniting the units. remain_seconds = total_seconds-((hours*3600)+(minutes*60)) Or: define the variable in a different way: remain_seconds = (total_seconds%3600)%60
Or: shortcut: knowing that 3600 and 60 have a common factor: 60 and they are built by the same block 60. I can write: remain_seconds = total_seconds%60

All those mistakes happened because of the non-deep understanding of the modulo operator. I knew its definition and its benefit, but I did not really understand its real importance until I started writing the code and falling into errors and mistakes. I learned that just knowing the tools and concepts isn't helpful until I apply them myself in a program. I struggled for about 2 hours late at night to understand the concepts and the logic behind this program deeply and in the end I rewrote the program 5 times in different ways to make sure it stuck. I learned that the floor division operator is like a consumer, for example: 100//50, how many times can we consume or take (50) out of (100)? Two times, right? What about 187//60? We can extract the whole (60) from 187 three times, three is the result of the floor division, and the remainder: 7 is the modulo, if I want the modulo immediately I can write: 187%60, the result will be: 7. The concept is easy but the real challenge is to apply this concept to a real program. But I have overcomed this challenge and I finally builded the seconds converter program! I am a recent high school graduate right now and I am desperate to continue my Python learning journey and build more projects in Python and improve myself before university begins!
