# AL07: Greedy Claims and Memoization Evidence

Name: [John Elijah B. Ferrer]
Partner(s): [Garreth Hickie]
My contribution: [made coding work on tuesday's function and made some assertions for thurdays demo]

## Run

```powershell
py -3.14 main.py
py -3.14 main.py --n 5
py -3.14 test_assignment.py
```

The --n option is used after enabling Thursday's stage.

## Work Notes

- Payment finding: With our first two test cases (A shorter exact payment existing & Largest-first coin getting stuck), we can see that our greedy payment is not always the most efficient. In the first example, choosing the largest coin results in 3 total coins needed, whereas using the fewest would only need 2. Even worse, in the second test, being greedy fails to produce an exact payment. 
- Saved-answer finding: Uncached calls counts every time that the (uncached) Fibonacci function runs. Cached calls count every time the cached Fibonacci function is called, including hits, but it excludes recursive calls that the uncached function would perform. The 3 hits are on values already within the cache, and the 6 distinct inputs are new values added to the cache. Data is stored in the cache when a new value is found through the Fibonacci function, and it is reused when it is "hit". 
- Pair question/decision: We were trying to bring argparse over to our main file for some time before deciding together that it ran fine calling from the supplied module. Using argparse when running the file is enough. Instead, we followed "Run" instructions above with "--n 5", "--n 1", or "--n 0" to test different values.

Keep observations brief. Append debugging/learnings as useful; no separate report.
Shared code/results are allowed; these observations are in your own words.

## Assistance

[Had Ai assist with explaining certain terms and concepts and how to code in certain strings]

## Instructor Comments

[Reserved for instructor feedback.]
