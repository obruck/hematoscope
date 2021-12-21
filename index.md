---
title: Home
---

# Hematology & microscopy

The Hematoscope Lab is an academic team of physicians, programmers, scanner engineers and students affiliated with the Hospital District of Helsinki and Uusimaa [HUS](https://www.hus.fi/en/) and [HUSLAB](https://www.hus.fi/en/patient/treatments-and-examinations/laboratories-and-imaging). We aim to solve how clinical experts can harness machines to better understand, diagnose and monitor hematological diseases. Our approach is to combine high-resolution automated imaging, big data analysis in the hospital Datalake and deep learning-based image analysis.
  
<!--{%
  include link.html
  type="github"
  icon=""
  text="See the template on GitHub"
  link="greenelab/lab-website-template"
  style="button"
%}
{%
  include link.html
  type="docs"
  icon=""
  text="See the documentation"
  link="https://github.com/greenelab/lab-website-template/wiki"
  style="button"
%}
{:.center}
-->

{% include section.html full=true %}

{% include banner.html image="images/banner.jpg" %}

{% include section.html %}

# Highlights

{% capture text %}
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

[See what we've published &nbsp;→](research)
{:.center}
{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="research"
  headline="Our Research"
  text=text
%}

{% capture text %}
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

[See our resources &nbsp;→](resources)
{:.center}
{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="resources"
  headline="Our Resources"
  text=text
%}

{% capture text %}
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

[Meet our team &nbsp;→](team)
{:.center}
{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="team"
  headline="Our Team"
  text=text
%}
