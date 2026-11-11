---
layout: page
permalink: /publications/
title: publications
description: publications in reversed chronological order
years: [2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2007, 2006, 2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991]
nav: true
nav_order: 2
---
<!-- _pages/publications.md -->
<div class="publications">

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f {{ site.scholar.bibliography }} -q @*[year={{y}}]* %}
{% endfor %}

</div>
