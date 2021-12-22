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
We aim to develop novel clinical tools to study patient samples, to improve the prognosis of patients and to save resources by better allocating treatments to patients.

[See what we've published &nbsp;→](research)
{:.center}
{% endcapture %}

{%
  include feature.html
  image="images/home/strategy.jpeg"
  link="research"
  headline="Research strategy"
  text=text
%}

{% capture text %}
We invest most of our efforts on collecting the world's largest high-resolution image dataset of MGG-stained patient samples and on developing deep learning-based algorithms to combine images to other patient data.

[See our resources &nbsp;→](resources)
{:.center}
{% endcapture %}

{%
  include feature.html
  image="images/home/resources.jpeg"
  link="resources"
  headline="Our Resources"
  text=text
%}

{% capture text %}
Our team is composed of ambitious and innovative reseachers. We believe in an inclusive work environment where everyone has an important role in achieving our goals.

[Meet our team &nbsp;→](team)
{:.center}
{% endcapture %}

{%
  include feature.html
  image="images/home/team.jpeg"
  link="team"
  headline="Our Team"
  text=text
%}
