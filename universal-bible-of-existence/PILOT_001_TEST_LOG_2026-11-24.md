# Pilot 001 Software Check — 24 November 2026

**Founder of ethical direction:** Paul McCombs (Coomsy), Wigan, UK.  
**Prepared and exercised by:** AI assistant with local Python 3.13.5 runner. This is **not an independent external audit**.

## What was tested

The source-controlled program `pilot001_check.py` checks the *structure and consistency of human-entered review records*. A 14-case local Python `unittest` suite covered:

1. Empty data correctly reports no result.
2. Demonstration-only data are identified as synthetic.
3. Exact duplicate reviewer records are rejected.
4. Synthetic and observed records cannot be pooled.
5. Source-free `supported` verdicts are rejected.
6. Unknown verdicts are rejected.
7. Rate denominator excludes unassessed rows.
8. Two reviewers can independently assess the same claim.
9. Duplicate entries by one reviewer are still rejected.
10. One response ID cannot be assigned to both arms.
11. Different study IDs cannot be pooled.
12. Reviewer identity field cannot be empty.
13. Arm must be A or B.
14. Study ID cannot be empty.

## Local run

```text
Python 3.13.5
Ran 14 tests in 0.005s
OK
```

Empty official review sheet returns:

```json
{"status": "no_data", "records": 0,
 "claim": "No reviews recorded; no result or impact can be inferred."}
```

The synthetic six-row fixture returns `synthetic_example_not_evidence`; arm A and B each have two assessed reviewer labels and both give 50.0% **of reviewer-assigned labels**, not independently verified correctness.

## Corrected defects

The original seven-test version rejected a *second reviewer* evaluating an existing claim, permitted multiple study IDs in one output, and allowed one response ID in conflicting comparison groups. Those have been corrected in the updated GitHub code and checked in a local equivalent run.

## Continuous integration

An automatic test-workflow definition was added at [`.github/workflows/covenant-pilot-checks.yml`](https://github.com/coomsey86/echocert/blob/main/.github/workflows/covenant-pilot-checks.yml), configured to run unit tests and check synthetic/blank inputs on code changes and pull requests.

**CI execution status:** Not verified at the time of this log. A workflow definition or a successful local test **does not prove that GitHub Actions ran successfully**.

## Evidence and scientific limitations

- **No real responses, human participants, independent reviewers or study results.**
- Verdicts are asserted by their human/data submitter; source URLs, reviewer identity and correctness are not independently verified by this software.
- Inter-rater reliability, statistical significance, causal impact and ecological outcomes are **not** evaluated.
- Tests examine record consistency, not the truth of the underlying Covenant or of any AI explanation.
- The synthetic demonstration is fictional and must never be cited as field research.

**Operational verdict:** Software mechanics **PASS (local tests)**; automatic CI **UNVERIFIED**; scientific effectiveness **NOT TESTED**; external independent validation **NOT YET DONE**.

### Further evidence required

Independent replication of the code tests, review of source-verification rules, a validated comparison protocol with consent/ethics safeguards, and actual data before claims of impact.
