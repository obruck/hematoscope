---
---

# Hematology & microscopy

The Hematoscope Lab is an academic team of physicians, programmers, scanner engineers and students affiliated with the Hospital District of Helsinki and Uusimaa [HUS](https://www.hus.fi/en/) and [HUSLAB](https://www.hus.fi/en/patient/treatments-and-examinations/laboratories-and-imaging). We aim to solve how clinical experts can harness machines to better understand, diagnose and monitor hematological diseases. Our approach is to combine high-resolution automated imaging, big data analysis in the hospital Datalake and deep learning-based image analysis.

<!-- {%
  include button.html
  type="docs"
  link="https://greene-lab.gitbook.io/lab-website-template-docs"
%}
{%
  include button.html
  type="github"
  text="On GitHub"
  link="greenelab/lab-website-template"
%} -->

{%
include figure.html
image="images/members/Ryhmä2.jpg"
width="100%"
%}

{% include section.html %}

## Highlights

{% capture text %}

We aim to develop novel clinical tools to study patient samples, to improve the prognosis of patients and to save resources by better allocating treatments to patients.

{%
  include button.html
  link="research"
  text="See our publications"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/home/strategy1.jpg"
  link="research"
  title="Our Research"
  text=text
%}

{% capture text %}

We invest most of our efforts on collecting the world's largest high-resolution image dataset of MGG-stained patient samples and on developing deep learning-based algorithms to combine images to other patient data.

{%
  include button.html
  link="projects"
  text="Browse our resources"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/home/resources.png"
  link="projects"
  title="Our Resources"
  flip=true
  style="bare"
  text=text
%}

{% capture text %}

Our team is composed of ambitious and innovative reseachers. We believe in an inclusive work environment where everyone has an important role in achieving our goals.

{%
  include button.html
  link="team"
  text="Meet our team"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/home/team.png"
  link="team"
  title="Our Team"
  text=text
%}