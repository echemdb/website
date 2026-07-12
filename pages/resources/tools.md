# Software Tools

A summary of tools from open-source repositories, for loading, converting, storing,
and analyzing electrochemical measurement data.
The list is non-exhaustive and the maintenance status of community projects may change.
To add a project to this list, see [suggest a link](index.md#suggest-a-link).

## Loaders and converters — interfacial electrochemistry and general

| Name | Scope / formats |
|---|---|
| [galvani](https://github.com/echemdata/galvani) | reads BioLogic `.mpr`/`.mpt` and Arbin `.res` into `pandas` |
| [eclabfiles](https://github.com/vetschn/eclabfiles) | BioLogic `.mpt`/`.mpr`/`.mps`; largely folded into yadg |
| [yadg](https://github.com/dgbowl/yadg) | many instrument formats to NetCDF datagrams; EIS supported |
| [ixdat](https://github.com/ixdat/ixdat) | in-situ data; BioLogic, Autolab, Ivium, CH Instruments, EC-MS, echemdb |
| [unitpackage](https://github.com/echemdb/unitpackage) | header-aware [loaders](https://echemdb.github.io/unitpackage/usage/loaders.html) creating unit-aware frictionless datapackages (echemdb project) |
| [impedance.py](https://github.com/ECSHackWeek/impedance.py) | EIS; BioLogic, Gamry `.DTA`, CSV; fitting and plotting |
| [MADAP](https://github.com/fuzhanrahmanian/MADAP) | common formats; EIS, Arrhenius, voltammetry analysis |

## Loaders — battery cyclers

| Name | Scope / formats |
|---|---|
| [cellpy](https://github.com/jepegit/cellpy) | Arbin, Maccor, PEC, Neware, BioLogic |
| [BEEP](https://github.com/TRI-AMDD/beep) | Arbin, BioLogic, Maccor, Neware; featurization |
| [galv (Galvanalyser)](https://github.com/Battery-Intelligence-Lab/galv) | Maccor, Ivium, BioLogic; storage platform with metadata |
| [PyProBE](https://github.com/ImperialCollegeLondon/PyProBE) | several cyclers; Polars/Parquet backend |

## Simulation and mechanism fitting

| Name | Scope / formats |
|---|---|
| [ElectroKitty](https://github.com/RedrumKid/ElectroKitty) | electrochemical simulator; fits reaction mechanisms and kinetic parameters to voltammograms |

## Databases and data platforms

| Name | Scope / formats |
|---|---|
| [DUCK](https://gitlab.com/dgarayr/duck) | Database Utility for Cyclovoltammetry Knowledge; ontology-based knowledge graphs and visualization for CV data |

## Utilities

| Name | Scope / formats |
|---|---|
| [reference_electrode_converter](https://gitlab.com/electrochemistry/reference_electrode_converter) | convert potentials between reference electrode scales |
| [reference-electrode-converter (Streamlit)](https://github.com/ganglix/reference-electrode-converter) | web app to convert potentials between reference electrode scales |
| [unitpackage reference electrode module](https://echemdb.github.io/unitpackage/api/electrochemistry/reference_electrode.html) | convert potentials between reference electrode scales (echemdb project) |
