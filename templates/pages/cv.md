---
author: Nicolas G. Hoermann, Albert K. Engstfeld
title: echemdb - The community database for electrochemical data
---
# Cyclic Voltammograms

template table

{{database | render("components/cv_table.md")}} 

other table  

{% for material in materials %}
## material
{% endfor %}
| identifier |
| ---------- |
{% for entry in database %}
| [{{ entry.identifier }}](entries/{{ entry.identifier }}) |
{% endfor %}

<!--
/* maybe here we could have some overview of the data, how many read
how man first is an analysis figure to see contributions w.r.t to time?!
website version on x axis ?!

Then periodic table overview to click to get to systems / elements

# Knowledge

Nico: I copied an own introduction

Cyclic voltammetry is a standard experimental technique for studying electrochemical interfaces that allows to infer surface compositions and interface reactions as a function of the applied electrode potential. In practice, cyclic voltammograms (CVs) are obtained by varying the electrode potential at fixed scan rate and measuring the current response of the electrode immersed in electrolyte solution. In general, CVs are characterized by potential regions within the stability window of the solvent which exhibit peaks of varying shape and height, and regions at low and high potentials, where faradaic, electrocatalytic reactions lead to exponentially increasing currents, e.g. due to the decomposition of the solvent. At high scan rates and/or in regions with faradaic reactions, CVs are governed by kinetic processes which typically induce a pronounced asymmetry for the forward and backward scan direction and/or a strong scan-rate dependence.
Evidently, any theoretical description of such CVs necessitates the use of kinetic models\cite{Tiwari2020}, including potentially also macroscopic mass transport\cite{Ringe2020}. 

On the other hand, at low scan rates and in potential windows without faradaic side reactions this asymmetry typically vanishes as does the scan-rate dependence (when currents are appropriately normalized). In this case, CV peak positions and shapes are related directly to the underlying thermodynamics of the electrified interface\cite{Wang2013}, and such CV experiments provide invaluable contributions to the understanding of the latter. In turn, such CVs can be understood and simulated based on equilibrium thermodynamic considerations\cite{Karlberg2007,Asiri2013, Chen2016, McCrum2016, McCrum2016b, Kristoffersen2018, Bagger2019, Yawei2019, Rossmeisl2020}. For such thermodynamic CVs the variation of the applied potential induces changes in the equilibrium surface charges, which can be traced back to changes in adsorbate coverages, as well as changes in the double layer charge, leading in sum to the observed electric current. As recently demonstrated for Ag(111) in halide containing solutions\cite{Hoermann2020JCTC}, double layer (DL) charging does not only add capacitive currents, but also affects equilibrium adsorbate coverages and the number of exchanged electrons per adsorbate -- as expressed by the electrosorption valency\cite{Hoermann2020JCTC,Vetter1972b,Schmickler1988,Hoermann2020Esorp}.

In this work we therefore analyse in most general terms thermodynamic CVs with included DL response. The derived equations can naturally explain Non-Nernstian behaviour and introduce a sensitive dependence of CV peaks to the electrolyte, via its impact on the interfacial capacitance\cite{Garlyyev2018,Ringe2019}. We hope, these results might help in the future to better understand according experiments and thus also help to validate and improve theoretical models. This is in particular important as at present all (atomistic) theoretical models of electrified interfaces necessarily introduce approximations due to computational time constraints, e.g in the complexity of the atomistic description (e.g. the surface with or without explicit water\cite{Noerskov2004, Urushihara2015,Hansen2016,Peterson2018,Hoermann2019NPJ}), the quality of the energetics (e.g. empirical potentials\cite{reaxff0}), the application of the electrode potential (e.g. absent or not\cite{Bonnet2012,Bouzid2018,Surendralal2018}, with explicit ions\cite{Hansen2016a,Le2020} or an implicit solvent model\cite{quantum-environment,Andreussi2012,Mathew2014,Held2014,SUNDARARAMAN2017g,Letchworth-Weaver2012,Bonnet2013,BONNET2014,Lespes2015, Fisicaro2016, Fisicaro2017, Ringe2017, Sundararaman2017,Sundararaman2017a, Sundararaman2017c,Goddard2017,Huang2018, Zhang2018, Peterson2018,Nattino2019, Andreussi2019, Hoermann2019, Gauthier2019,Hoermann2020Esorp}) or the derivation of macroscopic quantities (e.g. sampling \cite{Hansen2016a,Bagger2019,MITCHELL2000,MITCHELL2001,Chen2016,Weitzner2017,WeitznerClusterExpansion2017,Ambrosio2018}, mean field models\cite{Kristoffersen2018,Hoermann2020JCTC}). 
-->
