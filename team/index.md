---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# <i class="fas fa-users"></i>Team

The Hematoscope Lab is a translational research group. Our researchers are engaged to improve the diagnostics and prognosis of patients with hematological diseases. The team is composed of physicians, computational scientists, bioanalysts, and slide scanner engineers. We cultivate a supportive atmosphere where every individual is valued, ensuring that students not only feel appreciated but also benefit from the essential guidance required for their personal and academic growth.

{% include section.html %}

{%
include list.html
data="members"
component="portrait"
filters="role: pi"
%}
{%
include list.html
data="members"
component="portrait"
filters="role: md"
%}
{%
include list.html
data="members"
component="portrait"
filters="role: phd"
%}
{%
include list.html
data="members"
component="portrait"
filters="role: programmer"
%}
{%
include list.html
data="members"
component="portrait"
filters="role: engineer"
%}
{%
include list.html
data="members"
component="portrait"
filters="role: undergrad"
%}

<br/><br/>
# <i class="fas fa-user-graduate"></i>Alumni
{%
include list.html
data="members"
component="portrait"
filters="role: alumni"
%}

{:.center}

{% include section.html background="images/banner.jpg" dark=true%}

Currently, we welcome students and/or programmers with experience especially in medical data analysis (R or Python), software development, or HL7 FHIR implementation. Feel free to reach out!
{:.center}

{%
  include link.html
  icon="fas fa-hands-helping"
  text="Join the Team"
  link="contact"
  style="button"
%}
{:.center}

<!-- {%
include link.html
icon="fas fa-venus-mars"
text="Gender Equality Plan"
link="images/gep/gep.pdf"
style="button"
%}
{:.center}

-->

{% include section.html %}

## Funding

Our work is made possible by funding from several organizations.
{:.center}


{%
  include gallery.html
  style="square"

  image1="images/funding/hus.png"
  link1="https://www.hus.fi/en/"
  tooltip1="HUS"

  image2="images/funding/huslab.png"
  link2="https://www.hus.fi/en/patient/treatments-and-examinations/laboratories-and-imaging"
  tooltip2="HUSLAB"

  image3="images/funding/pss.png"
  link3="https://pss-saatio.fi/en/"
  tooltip3="Päivikki and Sakari Sohlberg Foundation"
  
  image4="images/funding/fls.png"
  link4="https://fls.fi/"
  tooltip4="Finska Läkaresällskapet Foundation"

  image5="images/funding/gyllenberg.png"
  link5="https://www.gyllenbergs.fi/en"
  tooltip5="Signe & Ane Gyllenberg Foundation"

  image6="images/funding/rbs.png"
  link6="https://runarbackstrominsaatio.fi/en/"
  tooltip6="Runar Bäckström Foundation"

  image7="images/funding/laaketieteensaatio.png"
  link7="https://laaketieteensaatio.fi/en/home/"
  tooltip7="Finnish Medical Foundation"
  
  image8="images/funding/syopasaatio.png"
  link8="https://syopasaatio.fi/"
  tooltip8="Finnish Cancer Foundation"
  
  image9="images/funding/minerva.png"
  link9="https://minervafoundation.fi"
  tooltip9="Minerva Foundation"
  
  image10="images/funding/KAlbinJohansson.png"
  link10="https://www.foundationweb.net/johansson/"
  tooltip10="K Albin Johansson Foundation"
  
  image11="images/funding/paulo.png"
  link11="https://www.paulo.fi/"
  tooltip11="Paulo Foundation"
  
  image12="images/funding/gilead.png"
  link12="https://www.gilead.com/science-and-medicine/research"
  tooltip12="Gilead Sciences"
  
  image13="images/funding/pfizer.png"
  link13="https://www.pfizer.com/science"
  tooltip13="Pfizer"
  
  image14="images/funding/aka.png"
  link14="https://www.aka.fi/en/"
  tooltip14="Academy of Finland"
%}
