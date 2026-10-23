# Mastery Protocol

A checked box means you have evidence, not that you watched a lecture or read a page.

## Seven-part learning loop

1. Learn: read the relevant section actively.
2. Reconstruct: write definitions and central ideas from memory.
3. Derive: reproduce key equations, assumptions, and intermediate steps.
4. Solve: attempt exercises without looking at solutions.
5. Implement: translate the mathematics into Python/NumPy.
6. Test: use hand calculations, edge cases, and independent implementations.
7. Explain: describe the idea, its use, and its limitations without jargon hiding gaps.

## Chapter completion checklist

- [ ] I can define the central objects precisely.
- [ ] I can explain the geometric or probabilistic intuition.
- [ ] I can derive the main equations without copying.
- [ ] I can solve representative problems by hand.
- [ ] I can state the assumptions behind each result.
- [ ] I implemented the central idea with Python/NumPy.
- [ ] I tested dimensions, edge cases, and numerical behavior.
- [ ] I compared the implementation with an independent check.
- [ ] I can explain a failure mode or limitation.
- [ ] I can solve a fresh problem that is not a clone of an example.
- [ ] I recorded mistakes and revisited them after a delay.

## Scoring rubric

Score each dimension from 0 to 3:

| Score | Meaning |
|---|---|
| 0 | Cannot explain or perform it yet |
| 1 | Can follow a worked example but cannot reproduce it independently |
| 2 | Can solve standard problems independently; transfer or edge-case reasoning remains weak |
| 3 | Can derive, solve a new variant, implement, test, and explain assumptions and limitations |

Score these five dimensions: conceptual understanding; derivation and reasoning; hand calculations and exercises; implementation and numerical validation; transfer to unfamiliar problems.

**Pass rule:** at least 2 in every dimension and at least 12/15 overall. Core chapters must include both derivation and implementation evidence. A score of 3 means robust competence, not omniscience.

## Anti-illusion rules

- Familiarity with a formula is not proof of understanding.
- Code that runs is not proof that the algorithm is correct.
- Matching one library output is not enough; test multiple cases and tolerances.
- Memorized proofs do not count unless you can explain why each step is valid.
- Record failed attempts instead of hiding them.
- Use libraries for verification after you understand the method, not as a substitute.

## Derivation log template

For each important result, record:
- **Claim:** what are you trying to show?
- **Definitions:** what does each symbol mean?
- **Assumptions:** when is the claim valid?
- **Derivation:** every meaningful intermediate step.
- **Interpretation:** geometric, statistical, or computational meaning.
- **Sanity check:** a tiny hand-calculable example.
- **Failure boundary:** when assumptions fail or the result does not apply.
- **ML connection:** what model or training behavior uses this result?

## Error log template

| Date | Topic | Mistake | Root cause | Correct reasoning | Re-test date |
|---|---|---|---|---|---|
| YYYY-MM-DD | Example | What went wrong? | Concept / algebra / dimensions / code / assumption | What fixes it? | YYYY-MM-DD |

Re-test important mistakes after 1 day, 1 week, and 1 month. If you fail the re-test, return the concept to active study.

## Weekly review

1. What can I derive now that I could not derive last week?
2. Which assumptions did I use without understanding?
3. Which implementation disagreed with a hand calculation?
4. What mistake repeated, and what caused it?
5. Can I explain the main idea without notes?
6. What is the single biggest gap to fix next?

Measure progress by independent performance and retained understanding, not pages read or hours logged.
