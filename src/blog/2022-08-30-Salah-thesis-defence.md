---
description: Salah's thesis defence
---

# 🗓️ 2022-08-30 — Sequence analysis with **GALACTIC** - Generic approach combining **F**ormal **C**oncept **A**nalysis and pattern mining

Salah Eddine Boukhetta defended his thesis on August 30th, 2022. Here is the video of the presentation (in french) and a short summary.

<div style="
  position: relative;
  overflow: hidden;
  width: 100%;
  padding-top: 56.25%; /* 16:9 Aspect Ratio (divide 9 by 16 = 0.5625) */
">
  <iframe
  src="https://videos.univ-lr.fr/video/2469-these-de-salah-eddine-boukhetta/?is_iframe=true"
  style="
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    width: 100%;
    height: 100%;
  "
  allowfullscreen
  >Your browser does not support iframe.</iframe>
</div>

Sequence data are nowadays used in many domains in order to better analyze and extract knowledge.
A sequence is a sequence of ordered elements such as travel trajectories or sequences of product purchases
in a supermarket. There are three types of sequences, simple sequences, temporal sequences and interval
sequences. Sequence mining is a domain of data mining that aims at extracting frequent sequential
patterns from a set of sequences, where these patterns are most often common subsequences. A sequential
pattern can be a subsequence, and it is frequent if it is shared by a sufficiently representative number
of objetcs in the data. Support is a monotonic measure that defines the proportion of data sharing a
sequential pattern. Several algorithms have been proposed for frequent sequential pattern extraction.
With the evolution of computing capabilities, the task of frequent sequential pattern extraction has
become faster. The difficulty then lies in the large number of extracted sequential patterns, which makes
it difficult to read and therefore to interpret. We speak about "deluge of patterns". A first approach
to solve this problem is to reduce the generated frequent patterns to the only closed patterns that
carry the same information. It has been observed that the set of all closed patterns can be organized
in a structure called a lattice. This structure is the basis of Formal Concept Analysis (**FCA**) which
is a field of data analysis for identifying relationships in the data set. **FCA** is classically designed to
deal with data described by sets of attributes, thus binary data. The pattern structure formalism and
the abstract conceptual navigation extend **FCA** to handle complex data such as sequences. Inspired
by pattern structures, the NᴇxᴛPʀɪᴏʀɪᴛʏCᴏɴᴄᴇᴘᴛ algorithm proposes a pattern extraction approach
for heterogeneous and complex data. This algorithm allows a generic pattern computation through
specific descriptions of objects by monadic predicates. It also proposes to refine a set of objects into
a smaller set through specific exploration strategies of the user. This allows to reduce the number of
patterns and thus to limit the deluge of generated patterns. The **GALACTIC** platform implements the
NextPriorityConcept algorithm and offers an ecosystem of extensions for data processing. In this work,
we are interested in the analysis of sequential data using **GALACTIC**. We propose several descriptions
and strategies adapted to simple, temporal and interval sequences. The descriptions are based on the
maximum common subsequences with descriptions more specific to the types of sequences. We propose
also a naive strategy allowing the generation of all concepts and more elaborate strategies allowing to
reduce the size of the lattice. We propose unsupervised quality measures to be able to compare between
the obtained lattices. A qualitative and quantitative analysis is conducted on real and synthetic datasets
to show the efficiency of our approach.
