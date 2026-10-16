# Week 8: Make CI tell the truth (25–30 minutes)

## Goal
Configure a GitHub Actions check, interpret its failure, and distinguish a test failure from an underspecified requirement. This is a practice lab, not a graded submission. Your instructor has provided this separate CI lab repository, so **do not use your graded Sprint repository**.

## Setup (5–8 minutes)
1. Open your team's CI lab repository in GitHub. Use **Add file** in GitHub or a Codespace to create a workflow file at `.github/workflows/tests.yml`.
2. Copy the text of `WORKFLOW_TO_ADD.yml` into that new workflow file and commit to the repository's `main` branch. Do not rename or delete the starter files.
3. Open the **Actions** tab and find the newly triggered **Python tests** workflow run. If Actions aren't enabled, your instructor can use local testing as a fallback.

## Investigation (10 minutes)
4. Open the failed job and find the first failing assertion. Note expected and actual outcomes. Is it a broken workflow, a bad test, or incorrect implementation? Why?
5. Fix the implementation (not the test), commit your change, and watch the next run. What does a green run establish—and what does it not?

## Requirements challenge (7 minutes)
6. Temporarily change `visitor_age < 0` to `visitor_age <= 0` and execute the existing tests. Does the current suite detect the mutation?
7. Consult `SPECIFICATION.md`. Does the mutation violate the documented age constraint? What exact additional test would detect it?
8. Restore the original age check. Do not leave the temporary mutation committed.

## Exit question (2 minutes)
Name one thing a green CI run proves and one thing it does not prove.

**No secrets, API keys, or dependency installation are needed.** This lab uses Python's standard `unittest`.
