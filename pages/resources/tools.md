# Software Tools

Open-source software tools and data-exchange formats for loading, converting, storing,
and analyzing electrochemical measurement data, grouped by topic.
The list is non-exhaustive and the maintenance status of community projects may change.
To add a project to this list, see [suggest a link](index.md#suggest-a-link).

## Exchange and storage formats

| Name | Scope / formats |
|---|---|
| [Frictionless Data Package](https://specs.frictionlessdata.io) | CSV plus a JSON descriptor; metadata-extensible |
| [unitpackage](https://github.com/echemdb/unitpackage) | unit-aware frictionless datapackage with a Python API (echemdb project) |
| [JCAMP-DX](https://github.com/nzhagen/jcamp) | IUPAC text exchange format (spectroscopy origin) |
| [AnIML](https://www.animl.org) | ASTM XML standard for analytical data |
| [HDF5](https://www.hdfgroup.org/solutions/hdf5/) | binary container for large or operando datasets |
| [Battery Data Format (BDF)](https://batterydataalliance.energy) | LF Energy open battery-data standard |

## Loaders and converters — interfacial electrochemistry and general

| Name | Scope / formats |
|---|---|
| [galvani](https://github.com/echemdata/galvani) | reads BioLogic `.mpr`/`.mpt` and Arbin `.res` into `pandas` |
| [eclabfiles](https://github.com/vetschn/eclabfiles) | BioLogic `.mpt`/`.mpr`/`.mps`; largely folded into yadg |
| [yadg](https://github.com/dgbowl/yadg) | many instrument formats to NetCDF datagrams; EIS supported |
| [ixdat](https://github.com/ixdat/ixdat) | in-situ data; BioLogic, Autolab, Ivium, CH Instruments, EC-MS, echemdb |
| [echemdb-converters](https://github.com/echemdb/echemdb-converters) | header-aware loaders to frictionless datapackages (echemdb project) |
| [impedance.py](https://github.com/ECSHackWeek/impedance.py) | EIS; BioLogic, Gamry `.DTA`, CSV; fitting and plotting |
| [MADAP](https://github.com/fuzhanrahmanian/MADAP) | common formats; EIS, Arrhenius, voltammetry analysis |

## Loaders — battery cyclers

| Name | Scope / formats |
|---|---|
| [cellpy](https://github.com/jepegit/cellpy) | Arbin, Maccor, PEC, Neware, BioLogic |
| [BEEP](https://github.com/TRI-AMDD/beep) | Arbin, BioLogic, Maccor, Neware; featurization |
| [galv (Galvanalyser)](https://github.com/Battery-Intelligence-Lab/galv) | Maccor, Ivium, BioLogic; storage platform with metadata |
| [PyProBE](https://github.com/ImperialCollegeLondon/PyProBE) | several cyclers; Polars/Parquet backend |

## Registries and infrastructure

| Name | Scope / formats |
|---|---|
| [Datatractor / MaRDA](https://yard.datatractor.org) | registry mapping file types to extractor tools |
| [Kadi4Mat](https://gitlab.com/iam-cms/kadi) | research data management platform and ELN with converters and workflows |
