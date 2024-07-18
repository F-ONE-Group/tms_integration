

## HOW TO USE IT 

### Import Example
```
from tms_integration.utils.sftp.base import SftpConfig
from tms_integration.lis_winsped import LisWinSped
from tms_integration.lis_winsped.models import LisInAuftrag
from tms_integration.lis_winsped.models.types import *


lis_winsped = LisWinSped(
    config=SftpConfig(
        host="<host_ip>",
        username="<username>",
        password="<password>",
        no_host_key=True, # False by default
    ),
    import_dest_folder="/Input",
)

records = [
    Ladeli(referenz="AUFGEBER1-27594406", tladenr="123"),
    Auftrag(
        referenz="AUFGEBER1-27594406", tladenr="123", aufnr=999, aufdatum="20220101"
    ),
    Posit(referenz="AUFGEBER1-27594406", tladenr="123", aufnr=999, aufposnr=1),
    Ggut(
        referenz="AUFGEBER1-27594406",
        tladenr="123",
        aufnr=999,
        lfdnrggut=1,
        klasse="3",
        unnummer="1993",
    ),
    Adr(
        referenz="AUFGEBER1-27594406",
        tladenr="123",
        aufnr=999,
        kunart=10,
        kundennr=12345,
    ),
    Adr(
        referenz="AUFGEBER1-27594406",
        tladenr="123",
        aufnr=999,
        kunart=10,
        kundennr=12345,
    ),
    Text(
        referenz="AUFGEBER1-27594406",
        tladenr="123",
        aufnr=999,
        txtartnr=111,
        txtstr1="Auf dem Gelände nicht rauchen",
    ),
]


payload = LisInAuftrag(
    start=Start(referenz="AUFGEBER1-27594406", datum="20220101"),
    ende=Ende(),
)
payload.records = records
lis_winsped.import_auftrag(payload, "test_f_one")

```