## Turtle art

The `stamp()` command leaves a picture of the turtle, as if it were a rubber stamp.

--- task ---
Add the `stamp()` command to stamp the turtle shape.

--- code ---
---
language: python
line_numbers: true
line_number_start: 19
line_highlights: 22
---
shape("turtle")
randomcolour()
randomplace()
stamp()

--- /code ---
--- /task ---

--- task ---
Now add a loop to choose a random colour and a random place and then stamp the turtle 30 times.
Don't forget to indent the code for changing the turtle so that it is inside the loop

--- code ---
---
language: python
line_numbers: true
line_number_start: 21
line_highlights: 21-24
---
shape("turtle")

for i in range(30):
    randomcolour()
    randomplace()
    stamp()

--- /code ---

--- /task ---


--- task ---
Click **Run** and watch your turtle art appear.
--- /task ---