---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %} Team

The Hematoscope Lab is a translational research group. Our researchers are engaged to improve the diagnostics and prognosis of patients with hematological diseases. Team members include physicians, machine learning engineers, software engineers and slide scanner engineers. We foster an environment where everyone feels appreciated and students receive the guidance they need.

{% include list.html data="members" component="portrait" filters="role: pi" %}
{% include list.html data="members" component="portrait" filters="role: ^(?!pi$|alumni$)" %}


{% include section.html %}

# {% include icon.html icon="fa-solid fa-user-graduate" %} Alumni

{% include list.html data="members" component="portrait" filters="role: alumni" %}


{% include section.html background="images/banner.jpg" dark=true%}

Currently, we welcome students and/or programmers with experience especially in medical data analysis (R or Python). Our other key areas of development include cloud computing, software development, HL7 FHIR implementation, and database management. Feel free to reach out!

{%
  include button.html
  icon="fas fa-hands-helping"
  type="address"
  text="Join the Team"
  link="contact"
%}
<br/>
{%
  include button.html
  icon="fas fa-venus-mars"
  text="Gender Equality Plan"
  link="images/gep/gep.pdf"
%}

{% include section.html %}

{% include section.html %}

## Funding

Our work is made possible by funding from several organizations.

{% capture content %}


{% include figure.html image="images/funding/hus.png" link="https://www.hus.fi/en/" tooltip="HUS" %}
{% include figure.html image="images/funding/huslab.png" link="https://www.hus.fi/en/patient/treatments-and-examinations/laboratories-and-imaging/" tooltip="HUSLAB" %}
{% include figure.html image="images/funding/pss.png" link="https://pss-saatio.fi/en/" tooltip="Päivikki and Sakari Sohlberg Foundation" %}
{% include figure.html image="images/funding/fls.png" link="https://fls.fi/" tooltip="Finska Läkaresällskapet Foundation" %}
{% include figure.html image="images/funding/gyllenberg.png" link="https://www.gyllenbergs.fi/en/" tooltip="Signe & Ane Gyllenberg Foundation" %}
{% include figure.html image="images/funding/rbs.png" link="https://runarbackstrominsaatio.fi/en/" tooltip="Runar Bäckström Foundation" %}
{% include figure.html image="images/funding/laaketieteensaatio.jpg" link="https://laaketieteensaatio.fi/en/home/" tooltip="Finnish Medical Foundation" %}
{% include figure.html image="images/funding/syopasaatio.png" link="https://syopasaatio.fi/" tooltip="Finnish Cancer Foundation" %}
{% include figure.html image="images/funding/minerva.png" link="https://minervafoundation.fi/" tooltip="Minerva Foundation" %}
{% include figure.html image="images/funding/KAlbinJohansson.png" link="https://www.foundationweb.net/johansson/" tooltip="K Albin Johansson Foundation" %}
{% include figure.html image="images/funding/paulo.png" link="https://www.paulo.fi/" tooltip="Paulo Foundation" %}
{% include figure.html image="images/funding/gilead.png" link="https://www.gilead.com/science-and-medicine/research" tooltip="Gilead Sciences" %}
{% include figure.html image="images/funding/pfizer.png" link="https://www.pfizer.com/science" tooltip="Pfizer" %}
{% include figure.html image="images/funding/aka.png" link="https://www.aka.fi/en/" tooltip="Academy of Finland" %}

{% endcapture %}

{% include grid.html style="square" content=content %}