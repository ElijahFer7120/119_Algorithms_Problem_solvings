# AL04: Search Contracts and Correctness

Name: [John Elijah B. Ferrer]
My contribution: [brief note; individual assignment]

## Run

Keep main.py, test_assignment.py, ticket_data.py, search_support.py,
ticket_display.py, and console_style.py together.

```powershell
py -3.14 main.py
py -3.14 test_assignment.py
```

## Contract and Work Notes

- Ordering precondition: [why the original-list T401 binary search failed: Binary search needs the tickets to be sorted by IDs. it failed because the list itself was unsorted which the search discarded the wrong section ]
- Result agreement: [why positions can differ; how duplicate categories are handled both linear and binary searches can return stuff differently because of their different list, T403 is in 0 for the original while in the ID-list it's in position two. categories are repeatable in a sense, so either searches can return any tickets back with the category of "account"]
- Reflection/debugging/learning: [brief observation; append as useful : there were a lot of things i've done and learn when typing down this code, Binary search needed a sort list to work while linear doesn't and figuring out how to config my asserts in my assignments]

The two small traces can stay in console output. No separate report or essay.

## Assistance

I had AI to help with assisting me with figuring out how to code things and explain certain concepts i couldn't understand

## Instructor Comments

[Reserved for instructor feedback.]