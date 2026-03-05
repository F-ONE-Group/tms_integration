import xml.etree.ElementTree as ET
from typing import List, Optional
from xml.dom.minidom import parseString

from pydantic import BaseModel, Field


class WindispoBaseModel(BaseModel):
    model_config = {"populate_by_name": True}


def _append_text_element(parent: ET.Element, tag: str, value: Optional[object]) -> None:
    element = ET.SubElement(parent, tag)
    if value is not None:
        element.text = str(value)


class WindispoHeader(WindispoBaseModel):
    kd_nr: str = Field(alias="KdNr")
    msg_time: str = Field(alias="MsgTime")
    msg_from: str = Field(alias="MsgFrom")
    process_type: str = Field(default="new", alias="ProcessType")


class WindispoJobDetail(WindispoBaseModel):
    z_nr: int = Field(alias="ZNr")
    laden: int = Field(alias="Laden")
    ladeadressen_nr: Optional[int] = Field(default=None, alias="LadeadressenNr")  # Existing address number
    anrede: Optional[str] = Field(default=None, alias="Anrede")
    name1: str = Field(alias="Name1")
    name2: Optional[str] = Field(default=None, alias="Name2")
    name3: Optional[str] = Field(default=None, alias="Name3")
    strasse: str = Field(alias="Straße")
    land: str = Field(alias="Land")
    plz: str = Field(alias="Plz")
    ort: str = Field(alias="Ort")
    termin_von: Optional[str] = Field(default=None, alias="TerminVon")
    termin_bis: Optional[str] = Field(default=None, alias="TerminBis")
    fix_termin: Optional[int] = Field(default=None, alias="FixTermin")
    ladungsanzahl: Optional[str] = Field(default=None, alias="Ladungsanzahl")
    ladungsart: Optional[str] = Field(default=None, alias="Ladungsart")
    ladungsbezeichnung: Optional[str] = Field(default=None, alias="Ladungsbezeichnung")
    gewicht: Optional[str] = Field(default=None, alias="Gewicht")
    ldm: Optional[str] = Field(default=None, alias="ldm")
    cbm: Optional[str] = Field(default=None, alias="cbm")
    referenz: Optional[str] = Field(default=None, alias="Referenz")
    info1: Optional[str] = Field(default=None, alias="Info1")
    container_nr1: Optional[str] = Field(default=None, alias="ContainerNr1")
    container_nr2: Optional[str] = Field(default=None, alias="ContainerNr2")
    geo_lat: Optional[str] = Field(default=None, alias="GeoLat")
    geo_lng: Optional[str] = Field(default=None, alias="GeoLng")



class WindispoFile(WindispoBaseModel):
    idx: int
    document_extension: Optional[str] = Field(default=None, alias="DocumentExtension")
    ablage_datum: Optional[str] = Field(default=None, alias="AblageDatum")
    betreff: Optional[str] = Field(default=None, alias="Betreff")
    content: str = ""

    def to_xml_element(self) -> ET.Element:
        element = ET.Element("file")
        element.set("idx", str(self.idx))
        if self.document_extension is not None:
            element.set("DocumentExtension", self.document_extension)
        if self.ablage_datum is not None:
            element.set("AblageDatum", self.ablage_datum)
        if self.betreff is not None:
            element.set("Betreff", self.betreff)
        element.text = self.content
        return element


class WindispoJob(WindispoBaseModel):
    job_owner: str = Field(alias="JobOwner")
    ext_id: str = Field(alias="ExtID")

    af_kd_nr: str = Field(alias="AfKdNr")
    af_anrede: Optional[str] = Field(default=None, alias="AfAnrede")
    af_name1: str = Field(alias="AfName1")
    af_name2: Optional[str] = Field(default=None, alias="AfName2")
    af_name3: Optional[str] = Field(default=None, alias="AfName3")
    af_strasse: str = Field(alias="AfStraße")
    af_land: str = Field(alias="AfLand")
    af_plz: str = Field(alias="AfPlz")
    af_ort: str = Field(alias="AfOrt")

    fz_kd_nr: str = Field(alias="FzKdNr")
    fz_anrede: Optional[str] = Field(default=None, alias="FzAnrede")
    fz_name1: str = Field(alias="FzName1")
    fz_name2: Optional[str] = Field(default=None, alias="FzName2")
    fz_name3: Optional[str] = Field(default=None, alias="FzName3")
    fz_strasse: str = Field(alias="FzStraße")
    fz_land: str = Field(alias="FzLand")
    fz_plz: str = Field(alias="FzPlz")
    fz_ort: str = Field(alias="FzOrt")

    referenz: str = Field(alias="Referenz")
    info1: Optional[str] = Field(default=None, alias="Info1")
    info2: Optional[str] = Field(default=None, alias="Info2")
    tscaa_id: Optional[str] = Field(default=None, alias="TScaaID")
    fzg_art1: Optional[str] = Field(default=None, alias="FzgArt1")
    fzg_art2: Optional[str] = Field(default=None, alias="FzgArt2")
    kuehltemperatur: Optional[str] = Field(default=None, alias="Kuehltemperatur")
    job_sg: str = Field(default="0", alias="jobSG")
    whrg: str = Field(default="EUR", alias="Whrg")

    jobdetails: List[WindispoJobDetail] = Field(default_factory=list, alias="jobdetail")
    files: List[WindispoFile] = Field(default_factory=list, alias="file")

    jobdetailcount: Optional[int] = Field(default=None, alias="jobdetailcount")
    filecount: Optional[int] = Field(default=None, alias="filecount")


class WindispoCreateJob(WindispoBaseModel):
    header: WindispoHeader
    job: WindispoJob
    jobcount: int = 1

    def _serialize_model_fields(
        self,
        parent: ET.Element,
        model: WindispoBaseModel,
        skip: Optional[set] = None,
    ) -> None:
        excluded = skip or set()
        for field_name, field_info in model.__class__.model_fields.items():
            if field_name in excluded:
                continue
            tag = field_info.alias or field_name
            value = getattr(model, field_name)
            _append_text_element(parent, tag, value)

    def to_xml_element(self) -> ET.Element:
        root = ET.Element("createjob.v1")

        header_element = ET.SubElement(root, "header")
        self._serialize_model_fields(header_element, self.header)

        job_element = ET.SubElement(root, "job")
        self._serialize_model_fields(
            job_element,
            self.job,
            skip={"jobdetails", "files", "jobdetailcount", "filecount"},
        )

        for detail in self.job.jobdetails:
            detail_element = ET.SubElement(job_element, "jobdetail")
            self._serialize_model_fields(detail_element, detail)

        for file in self.job.files:
            job_element.append(file.to_xml_element())

        _append_text_element(job_element, "jobdetailcount", len(self.job.jobdetails))
        _append_text_element(job_element, "filecount", len(self.job.files))

        _append_text_element(root, "jobcount", self.jobcount)
        return root

    def generate_xml(self) -> str:
        root = self.to_xml_element()
        xml_bytes = ET.tostring(root, encoding="utf-8")
        pretty_xml = parseString(xml_bytes).toprettyxml(indent="  ", encoding="utf-8")
        return pretty_xml.decode("utf-8")
