# Pilot 001: Reproducible Claim Review Checker

**Founding ethical direction:** Paul McCombs (Coomsy), Wigan. Developed with AI coding assistance, 24 November 2026.

This is a minimal **Python standard-library** tool. It makes Pilot 001's record handling runnable without requiring APIs, agents, cloud services, subscriptions or private information.

It is **not** a working study of human comprehension, wellbeing, ecological impacts or the Universal Bible of Existence's effectiveness. It does not independently fact-check a claim or verify whether a reviewer or source is authentic.

## How to run

From the `universal-bible-of-existence` directory with Python 3.9+:

```bash
python pilot001_check.py PILOT_001_CLAIM_REVIEWS.csv
python pilot001_check.py PILOT_001_CLAIM_REVIEWS_SYNTHETIC.csv
python -m unittest -v test_pilot001_check.py
```

The first command is intentionally an empty, real-results template and must return `status: no_data`. The second command prints a **synthetic-only** demonstration summary, distinctly marked `synthetic_example_not_evidence`; it must never be cited as an actual result. The third command runs fourteen automated program checks.

## Independent reviewer workflow

1. Start with the [research protocol](PILOT_001.md) and [independent reviewer brief](REVIEWER_BRIEF.md).
2. Define evaluation items, prompts, answer keys and grading criteria before collecting model responses. Record source URLs, dates and provenance separately.
3. Obtain necessary research ethics permissions and participant consent before any work involving people.
4. Only after a real authorised claim-level review, enter one row per claim in a **separate copy** of [the blank template](PILOT_001_CLAIM_REVIEWS.csv), with `record_type=observed`. Use pseudonymous response and reviewer IDs. Do not include raw private participant data.
5. Use `arm=A` or `arm=B`; verdicts are `supported`, `contradicted`, `unsupported` or `unassessed`. Every source-supported or source-contradicted claim must contain `source_id`.
6. Run the checker. It rejects duplicate records by the **same reviewer**, mixed demo/real records, pooled studies, a response assigned to both groups, invalid categories and source-free supported claims. Separate reviewers may judge the same claim; their assessments remain separate records.
7. Interpret any percentages **only as the reviewers' recorded labels**, never as independent proof of truth or causal improvement.
8. Submit the method or a justified correction to [the public reviewer task](https://github.com/coomsey86/echocert/issues/2). Don't publish personal information.

- [Local test log, corrected defects and automatic workflow status](PILOT_001_TEST_LOG_2026-11-24.md)

## Limitations to fix before calling it research

- No validated item bank, independent source-verification mechanism, inter-rater reliability, or documented statistical analysis plan has been implemented.
- No model outputs or human responses have been collected here.
- A claim-level percentage cannot measure comprehension, autonomy or whether explanatory format caused an improvement.
- The synthetic CSV is an arithmetic smoke test with imaginary records. It is not evidence of real-world AI performance.
- A second reviewer, source audit and properly pre-specified trial design are needed for meaningful external evidence.

**Software check:** the fourteen included Python unit tests passed in the preparing environment on 24 November 2026. This is a reported local run, not independent code certification.

The public EchoCert repository's licensing applies to code according to its terms; the Covenant manuscript is separate and rights-reserved where applicable. No assumption of an unrestricted open-source licence is made.

## 24 November corrective regression

A follow-up inspection identified three errors in the original bookkeeping design: it prevented a second reviewer from evaluating the same claim, allowed different study IDs to be pooled, and allowed one response ID to appear in both study arms. The code now permits independently labelled reviews while rejecting pooling and conflicting assignment. **14/14 local unit tests pass in the preparing environment**. This is software verification, not independent research validation. The checker still does not verify cited sources, real reviewer identities, comprehension, ecological outcomes or inter-rater reliability; all these require additional work.
