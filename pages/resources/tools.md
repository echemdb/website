# Software Tools

A summary of tools from open-source repositories, for loading, converting, storing,
and analyzing electrochemical measurement data.
The list is non-exhaustive and the maintenance status of community projects may change.
To add a project to this list, see [suggest a link](index.md#suggest-a-link).

## Loaders and converters — interfacial electrochemistry and general

| Name | Scope / formats | Reference |
|---|---|---|
| [eclabfiles](https://github.com/vetschn/eclabfiles) | BioLogic `.mpt`/`.mpr`/`.mps`; largely folded into yadg | |
| [galvani](https://github.com/echemdata/galvani) | reads BioLogic `.mpr`/`.mpt` and Arbin `.res` into `pandas` | |
| [impedance.py](https://github.com/ECSHackWeek/impedance.py) | EIS; BioLogic, Gamry `.DTA`, CSV; fitting and plotting | [DOI](https://doi.org/10.21105/joss.02349) |
| [ixdat](https://github.com/ixdat/ixdat) | in-situ data; BioLogic, Autolab, Ivium, CH Instruments, EC-MS, echemdb | |
| [MADAP](https://github.com/fuzhanrahmanian/MADAP) | common formats; EIS, Arrhenius, voltammetry analysis | [DOI](https://doi.org/10.1038/s41597-023-01936-3) |
| [unitpackage](https://github.com/echemdb/unitpackage) | header-aware [loaders](https://echemdb.github.io/unitpackage/usage/loaders.html) creating unit-aware frictionless datapackages (echemdb project) | [DOI](https://doi.org/10.5334/dsj-2025-013) |
| [yadg](https://github.com/dgbowl/yadg) | many instrument formats to NetCDF datagrams; EIS supported | [DOI](https://doi.org/10.21105/joss.04166) |

## Loaders — battery cyclers

| Name | Scope / formats | Reference |
|---|---|---|
| [BEEP](https://github.com/TRI-AMDD/beep) | Arbin, BioLogic, Maccor, Neware; featurization | [DOI](https://doi.org/10.1016/j.softx.2020.100506) |
| [cellpy](https://github.com/jepegit/cellpy) | Arbin, Maccor, PEC, Neware, BioLogic | [DOI](https://doi.org/10.21105/joss.06236) |
| [galv (Galvanalyser)](https://github.com/Battery-Intelligence-Lab/galv) | Maccor, Ivium, BioLogic; storage platform with metadata | [arXiv](https://arxiv.org/abs/2010.14959) |
| [PyProBE](https://github.com/ImperialCollegeLondon/PyProBE) | several cyclers; Polars/Parquet backend | [DOI](https://doi.org/10.21105/joss.07474) |

## Simulation and mechanism fitting

| Name | Scope / formats | Reference |
|---|---|---|
| [ElectroKitty](https://github.com/RedrumKid/ElectroKitty) | electrochemical simulator; fits reaction mechanisms and kinetic parameters to voltammograms | [DOI](https://doi.org/10.1021/acselectrochem.4c00218) |
| [frumkin](https://github.com/lucasdekam/frumkin) | modeling of electric double layers with modified Poisson–Boltzmann theory; comparison with experimental capacitance data | |

## Databases and data platforms

| Name | Scope / formats | Reference |
|---|---|---|
| [DUCK](https://gitlab.com/dgarayr/duck) | Database Utility for Cyclovoltammetry Knowledge; ontology-based knowledge graphs and visualization for CV data | [DOI](https://doi.org/10.1039/d6dd00019c) |

## Utilities

| Name | Scope / formats | Reference |
|---|---|---|
| [reference-electrode-converter (Streamlit)](https://github.com/ganglix/reference-electrode-converter) | web app to convert potentials between reference electrode scales | |
| [reference_electrode_converter](https://gitlab.com/electrochemistry/reference_electrode_converter) | convert potentials between reference electrode scales | |
| [unitpackage reference electrode module](https://echemdb.github.io/unitpackage/api/electrochemistry/reference_electrode.html) | convert potentials between reference electrode scales (echemdb project) | [DOI](https://doi.org/10.5334/dsj-2025-013) |
