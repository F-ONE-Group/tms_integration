import xml.etree.ElementTree as ET
from typing import Optional

from pydantic import BaseModel, Field


class WindispoExportBaseModel(BaseModel):
    model_config = {"populate_by_name": True}


class WindispoExportError(WindispoExportBaseModel):
    error_msg: str = Field(alias="ErrorMsg")


class WindispoExportHeader(WindispoExportBaseModel):
    kd_nr: str = Field(alias="KdNr")
    msg_time: str = Field(alias="MsgTime")
    msg_from: str = Field(alias="MsgFrom")
    process_type: str = Field(alias="ProcessType")
    processed_file: str = Field(alias="ProcessedFile")


class WindispoExportJob(WindispoExportBaseModel):
    doc_id: Optional[str] = Field(default=None, alias="DocID")
    ext_id: Optional[str] = Field(default=None, alias="ExtID")
    af_kd_nr: Optional[str] = Field(default=None, alias="AfKdNr")
    error: Optional[WindispoExportError] = Field(default=None, alias="Error")


class WindispoExportCreateJob(WindispoExportBaseModel):
    header: WindispoExportHeader
    job: WindispoExportJob
    jobcount: int = Field(default=1, alias="jobcount")

    @staticmethod
    def _read_text(parent: ET.Element, tag: str) -> Optional[str]:
        element = parent.find(tag)
        if element is None:
            return None
        return element.text

    @classmethod
    def from_xml(cls, xml_text: str) -> "WindispoExportCreateJob":
        root = ET.fromstring(xml_text)
        header = root.find("header")
        job = root.find("job")

        if header is None or job is None:
            raise ValueError("Invalid Windispo export XML: missing header or job")

        payload = {
            "header": {
                "KdNr": cls._read_text(header, "KdNr") or "",
                "MsgTime": cls._read_text(header, "MsgTime") or "",
                "MsgFrom": cls._read_text(header, "MsgFrom") or "",
                "ProcessType": cls._read_text(header, "ProcessType") or "",
                "ProcessedFile": cls._read_text(header, "ProcessedFile") or "",
            },
            "job": {
                "DocID": cls._read_text(job, "DocID"),
                "ExtID": cls._read_text(job, "ExtID"),
                "AfKdNr": cls._read_text(job, "AfKdNr"),
            },
            "jobcount": int(cls._read_text(root, "jobcount") or 1),
        }

        error = job.find("Error")
        if error is not None:
            payload["job"]["Error"] = {
                "ErrorMsg": cls._read_text(error, "ErrorMsg") or ""
            }

        return cls.model_validate(payload)
