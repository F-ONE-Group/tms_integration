# Windispo Integration

This module provides Windispo import generation for the `createjob.v1` XML schema.

## Features

- Typed payload models for `header`, `job`, `jobdetail`, and optional `file` entries.
- XML generation via `WindispoCreateJob.generate_xml()`.
- SFTP import helper via `Windispo.import_auftrag(...)`.

## Usage

```python
from tms_integration.windispo.models import (
    WindispoCreateJob,
    WindispoHeader,
    WindispoJob,
    WindispoJobDetail,
)

payload = WindispoCreateJob(
    header=WindispoHeader(
        KdNr="39",
        MsgTime="20241127151739",
        MsgFrom="HB",
        ProcessType="new",
    ),
    job=WindispoJob(
        JobOwner="rs@windispo.at",
        ExtID="aaa1",
        AfKdNr="3",
        AfName1="Neele-Vat Transport B.V.",
        AfStraße="Bierbrouwerstraat 2",
        AfLand="NL",
        AfPlz="3194",
        AfOrt="Ap Hoogvliet",
        FzKdNr="3",
        FzName1="Neele-Vat Transport B.V.",
        FzStraße="Bierbrouwerstraat 2",
        FzLand="NL",
        FzPlz="3194",
        FzOrt="Ap Hoogvliet",
        Referenz="1802176771 FTL 90",
        FzgArt1="Planensattel",
        Whrg="EUR",
        jobdetail=[
            WindispoJobDetail(
                ZNr=1,
                Laden=1,
                Name1="Neele-Vat Transport BV",
                Straße="Seattleweg 3",
                Land="NL",
                Plz="3195",
                Ort="Pernis",
                TerminVon="202208171100",
                TerminBis="202208171430",
                FixTermin=0,
                Ladungsanzahl="66.00",
                Ladungsart="Euro-Pal.",
                Ladungsbezeichnung="Foodstuff",
                Gewicht="4854.00",
                ldm="13.60",
                cbm="0.00",
                Referenz="400154657",
            )
        ],
    ),
    jobcount=1,
)

xml_text = payload.generate_xml()
print(xml_text)
```
