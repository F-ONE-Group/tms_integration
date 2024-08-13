from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel, validator
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString

from tms_integration.utils.xml import XmlAttribute, to_xml_element


class BaseCarloClass(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    @validator("Action", pre=True, check_fields=False)
    def set_action(cls, v):
        return XmlAttribute(v)


class Address(BaseCarloClass):
    Street: str
    HouseNumber: str
    Location1: str
    ZipCode: str
    IsoTwoCharacterCountryCode: str


class OriginalBusinessPartner(BaseCarloClass):
    Action: XmlAttribute
    GlobalLocationNumber: str
    Name1: str
    Addresses: Address


class Receiver(BaseCarloClass):
    OriginalBusinessPartner: OriginalBusinessPartner


class Sender(BaseCarloClass):
    OriginalBusinessPartner: OriginalBusinessPartner


class Package(BaseCarloClass):
    Matchcode: Optional[str] = None


class SsccCurrent(BaseCarloClass):
    Code: str


class ConsignmentItem(BaseCarloClass):
    PositionNumber: int
    Quantity: int
    Package: Package
    EffectiveWeightInKilogram: float
    StoragePlaces: Optional[float] = None
    Meter: Optional[float] = None
    SsccCurrents: Optional[List[SsccCurrent]] = None


class Times(BaseCarloClass):
    LieferdatumStart: datetime
    LieferdatumEnd: datetime
    LadedatumStart: datetime
    LadedatumEnd: datetime


class InformationClass(BaseCarloClass):
    Info10: str


class EditStatusClass(BaseCarloClass):
    Matchcode: str = "335"


class Consignment(BaseCarloClass):
    Number: int
    ConsignmentReference2: str
    Times: Times
    Incoterms: int
    Receiver: Receiver
    Sender: Sender
    ConsignmentItems: List[ConsignmentItem]
    ConsignmentReference1: Optional[str] = None
    ExternalNumber: Optional[str] = None
    ContainsDangerousGoods: Optional[bool] = None
    Information: Optional[InformationClass] = None
    EditStatus: Optional[EditStatusClass] = None


class Customer(BaseCarloClass):
    GlobalLocationNumber: str


class NormalOrder(BaseCarloClass):
    Action: XmlAttribute = "updateorcreate"
    ExternalNumber: str
    Date: datetime
    Info1: str = "Normal"
    Customer: Customer
    Consignments: List[Consignment]


class NormalOrderData(BaseCarloClass):
    NormalOrder: NormalOrder

    def generate_xml(self) -> str:
        # Create the root element
        root = to_xml_element("NormalOrderData", self)

        # Generate the XML string
        xml_str = ET.tostring(root, encoding="utf-8").decode("utf-8")

        # Add XML declaration and namespaces manually
        xml_declaration = '<?xml version="1.0" encoding="utf-8"?>'

        final_xml = f"{xml_declaration}{xml_str}"

        # Pretty-print the XML and return it
        dom = parseString(final_xml)
        return dom.toprettyxml(indent="  ")
