---
author: Nicolas G. Hoermann
title: echemdb - {{ echemdb_id }} CV Data
---

# {{ echemdb_id }}

## Experimental Setup

{{ cvs[cvs['echemdb-id'] == echemdb_id][['electrode material', 'surface', 'electrolyte']].to_markdown(index=False) }}

## Experimental Results

{{ plotly(echemdb_id, cvs[cvs['echemdb-id'] == echemdb_id]['path'].values[0]) }}
