# AL08: Workshop Access — Traversal and Restricted Routes

Name: [John Elijah B. Ferrer]
Partner(s): [Parker Audetat]
My contribution: [handled tuesday's workload]
Issued personal case: [ B ]

## Run

```powershell
py -3.14 main.py
py -3.14 test_assignment.py
```

Final settings: STAGE = 3 and TEST_STAGE = 3 if using the starter switches.

## Work Notes

- Model: [the rooms are Entrance,Reception,Hallway,ToolRoom,Assembly,Inspection,Packing,Loading,Office,BreakRoom, It show which way is the fastest route to go to, only exception is the annex as it's is own seperate thing]
- Monday check: [I added a new room called Breakroom as an office neighbor, the validator scanned and flagged it as an unknown room. I removed the entry from the copy and it passed the validations check. ]
- Traversal: [stacks are what is used in DFS, it checks the most recent added room first and avoids going around loops by skipping room it already processed]
- Personal restriction: [i picked B, Office and packing are blocked which results in no route to loading, because those two rooms are loading's two neighboring access rooms]
- Collaboration: [I mostly did the assertions and tuesday work]
Keep notes brief in your own words; the app/tests contain the detailed evidence.

## Assistance

[Had AI to help me with explaining certain concepts and figure out what to code in myself.]

## Instructor Comments

[Reserved for instructor feedback.]
