---
description: Strings description
---

# 🗓️ 2026-11-13 — Strings description

As part of the **GALACTIC** project, I developed a Python function that
builds string descriptions in the form of regular expressions.

Given a list {math}`l`, the function looks for expressions {math}`e` that recognize
every input: {math}`l\subseteq L(e)`, also written {math}`l\sqsubseteq e` by abuse
of notation. It retains the most precise expressions within a defined
family: their languages cannot be reduced further while covering the inputs.

The algorithm searches for common subsequences, determines intervals between
their characters, and compares languages using automata. Several incomparable
descriptions may remain: for `["abX", "abY"]` with alphabet `ab`,
allowing at most one literal, the results are `.b.` and `a.{2}`.

Parameters control the literal count and the gaps before, between, and after
literals. I optimized the common-prefix and common-suffix cases with an
unrestricted opposite edge, as well as the no-literal case, which bounds
string lengths.

