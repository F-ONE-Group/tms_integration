"""Order types for Carlo TMS integration based on FOneOrderImport-v3.xsd.

This module provides Pydantic models for Carlo order import/export functionality,
similar to the LisInAuftrag pattern used in lis_winsped.
"""

from typing import Optional, List, Any, Tuple
from datetime import datetime
from datetime import date as date_type
from decimal import Decimal
import xml.etree.ElementTree as ET
from pathlib import Path
from pydantic import BaseModel, Field
import uuid
from lxml import etree as lxml_etree

from .types.enums import ImportExportAction, OrderContext
from .types.base import (
    Header,
    OrganizationalUnit,
    Currency,
)
from .types.business_partner import BusinessPartner, ContactPerson
from .types.consignment import Consignment


class Order(BaseModel):
    """The order."""

    date: Optional[date_type] = Field(None, serialization_alias="Date")
    object_owner: Optional[OrganizationalUnit] = Field(
        None, serialization_alias="ObjectOwner"
    )
    number: Optional[int] = Field(None, serialization_alias="Number")
    external_number: Optional[str] = Field(
        None, max_length=50, serialization_alias="ExternalNumber"
    )
    order_context: Optional[OrderContext] = Field(
        None, serialization_alias="OrderContext"
    )
    order_date: Optional[date_type] = Field(None, serialization_alias="OrderDate")
    order_reference1: Optional[str] = Field(
        None, max_length=256, serialization_alias="OrderReference1"
    )
    order_reference2: Optional[str] = Field(
        None, max_length=256, serialization_alias="OrderReference2"
    )
    order_reference3: Optional[str] = Field(
        None, max_length=256, serialization_alias="OrderReference3"
    )
    info: Optional[str] = Field(None, max_length=2000, serialization_alias="Info")
    customer: Optional[BusinessPartner] = Field(None, serialization_alias="Customer")
    customer_contact_person: Optional[ContactPerson] = Field(
        None, serialization_alias="CustomerContactPerson"
    )
    freight_payer: Optional[BusinessPartner] = Field(
        None, serialization_alias="FreightPayer"
    )
    consignments: Optional[List[Consignment]] = Field(
        None, serialization_alias="Consignments"
    )
    custom_integer1: Optional[int] = Field(None, serialization_alias="CustomInteger1")
    custom_integer2: Optional[int] = Field(None, serialization_alias="CustomInteger2")
    custom_integer3: Optional[int] = Field(None, serialization_alias="CustomInteger3")
    custom_integer4: Optional[int] = Field(None, serialization_alias="CustomInteger4")
    custom_float1: Optional[Decimal] = Field(None, serialization_alias="CustomFloat1")
    custom_float2: Optional[Decimal] = Field(None, serialization_alias="CustomFloat2")
    custom_float3: Optional[Decimal] = Field(None, serialization_alias="CustomFloat3")
    custom_float4: Optional[Decimal] = Field(None, serialization_alias="CustomFloat4")
    custom_float5: Optional[Decimal] = Field(None, serialization_alias="CustomFloat5")
    custom_date_time1: Optional[datetime] = Field(
        None, serialization_alias="CustomDateTime1"
    )
    custom_date_time2: Optional[datetime] = Field(
        None, serialization_alias="CustomDateTime2"
    )
    custom_date_time3: Optional[datetime] = Field(
        None, serialization_alias="CustomDateTime3"
    )
    custom_date_time4: Optional[datetime] = Field(
        None, serialization_alias="CustomDateTime4"
    )
    custom_date_time5: Optional[datetime] = Field(
        None, serialization_alias="CustomDateTime5"
    )
    custom_date_time6: Optional[datetime] = Field(
        None, serialization_alias="CustomDateTime6"
    )
    is_empty_trip: Optional[bool] = Field(None, serialization_alias="IsEmptyTrip")
    posting_reference1: Optional[str] = Field(
        None, max_length=30, serialization_alias="PostingReference1"
    )
    posting_reference2: Optional[str] = Field(
        None, max_length=30, serialization_alias="PostingReference2"
    )
    posting_reference3: Optional[str] = Field(
        None, max_length=30, serialization_alias="PostingReference3"
    )
    posting_reference4: Optional[str] = Field(
        None, max_length=30, serialization_alias="PostingReference4"
    )
    vessel_exchange_currency: Optional[Currency] = Field(
        None, serialization_alias="VesselExchangeCurrency"
    )
    vessel_exchange_rate: Optional[Decimal] = Field(
        None, serialization_alias="VesselExchangeRate"
    )
    vessel_exchange_date: Optional[date_type] = Field(
        None, serialization_alias="VesselExchangeDate"
    )
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class OrderData(BaseModel):
    """Collection of orders - root element for XML import."""

    header: Optional[Header] = Field(None, serialization_alias="Header")
    orders: List[Order] = Field(
        default_factory=list[Order], serialization_alias="Order"
    )

    model_config = {"populate_by_name": True}


class NormalOrderData(BaseModel):
    """
    Main class for Carlo order data similar to LisInAuftrag.

    This class provides validation and XML generation functionality for
    Carlo TMS order import.

    Usage:
        ```python
        from tms_integration.carlo.models import NormalOrderData, Order, Consignment

        order_data = NormalOrderData(
            orders=[
                Order(
                    date=date.today(),
                    customer=BusinessPartner(number=123456),
                    consignments=[
                        Consignment(
                            item_number=1,
                            sender=ConsignmentBusinessPartner(
                                name1="Sender Company",
                                city1="Berlin",
                                country="DE"
                            ),
                            receiver=ConsignmentBusinessPartner(
                                name1="Receiver Company",
                                city1="Munich",
                                country="DE"
                            )
                        )
                    ]
                )
            ]
        )

        xml_string = order_data.generate_xml()
        ```
    """

    header: Optional[Header] = Field(None, serialization_alias="Header")
    orders: List[Order] = Field(
        default_factory=list[Order], serialization_alias="Order"
    )

    model_config = {"populate_by_name": True}

    def validate_orders(self) -> None:
        """
        Validate that the order data has required fields.

        Raises:
            ValueError: If validation fails (e.g., no orders provided)
        """
        if not self.orders:
            raise ValueError("At least one order is required")

        for i, order in enumerate(self.orders):
            if order.consignments:
                for j, consignment in enumerate(order.consignments):
                    if not consignment.sender and not consignment.receiver:
                        raise ValueError(
                            f"Order {i + 1}, Consignment {j + 1}: "
                            "At least sender or receiver is required"
                        )

    def _model_to_xml_element(self, tag: str, model: BaseModel) -> ET.Element:
        """Convert a Pydantic model to an XML element using serialization aliases."""
        element = ET.Element(tag)

        for field_name, field_info in type(model).model_fields.items():
            # Get the serialization alias or use the field name
            alias = field_info.serialization_alias or field_name
            value: Any = getattr(model, field_name)

            if value is None:
                continue

            if isinstance(value, BaseModel):
                child = self._model_to_xml_element(alias, value)
                element.append(child)
            elif isinstance(value, list):
                for item in value:  # type: ignore
                    if isinstance(item, BaseModel):
                        # For list items, use the alias as the tag
                        # (e.g., Consignments -> each item is Consignments)
                        child = self._model_to_xml_element(alias, item)
                        element.append(child)
                    else:
                        child = ET.SubElement(element, alias)
                        child.text = self._format_value(item)
            elif isinstance(value, datetime):
                child = ET.SubElement(element, alias)
                child.text = value.strftime("%Y-%m-%dT%H:%M:%S")
            elif isinstance(value, date_type):
                child = ET.SubElement(element, alias)
                child.text = value.strftime("%Y-%m-%d")
            elif isinstance(value, bool):
                child = ET.SubElement(element, alias)
                child.text = "true" if value else "false"
            elif isinstance(value, (int, float, Decimal)):
                child = ET.SubElement(element, alias)
                child.text = str(value)
            else:
                child = ET.SubElement(element, alias)
                child.text = str(value)

        return element

    def _format_value(self, value: Any) -> str:
        """Format a value for XML output."""
        if isinstance(value, datetime):
            return value.strftime("%Y-%m-%dT%H:%M:%S")
        elif isinstance(value, date_type):
            return value.strftime("%Y-%m-%d")
        elif isinstance(value, bool):
            return "true" if value else "false"
        else:
            return str(value)

    def generate_xml(self, validate: bool = True) -> str:
        """
        Generate XML string from the order data.

        Args:
            validate: If True, validate the order data before generating XML.
                     Defaults to True.

        Returns:
            str: XML string representation of the order data.

        Raises:
            ValueError: If validation is enabled and fails.
        """
        if validate:
            self.validate_orders()

        # Create root element with namespace
        root = ET.Element("OrderData")
        root.set("xmlns", "SoloplanOrderImport.v2")

        # Add Header if present, or create a default one
        if self.header:
            header_element = self._model_to_xml_element("Header", self.header)
        else:
            header_element = ET.SubElement(root, "Header")
            send_date = ET.SubElement(header_element, "SendDate")
            send_date.text = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            export_ref = ET.SubElement(header_element, "ExportItemReference")
            export_ref.text = str(uuid.uuid4())

        if self.header:
            root.append(header_element)

        # Add Orders
        for order in self.orders:
            order_element = self._model_to_xml_element("Order", order)
            root.append(order_element)

        # Generate XML string with declaration
        xml_declaration = '<?xml version="1.0" encoding="utf-8"?>\n'
        xml_body = ET.tostring(root, encoding="unicode")

        return xml_declaration + xml_body

    @staticmethod
    def get_xsd_path() -> Path:
        """
        Get the path to the XSD schema file.

        Returns:
            Path: Path to FOneOrderImport-v3.xsd
        """
        return Path(__file__).parent / "xsd" / "FOneOrderImport-v3.xsd"

    def validate_against_xsd(
        self, xml_string: Optional[str] = None
    ) -> Tuple[bool, List[str]]:
        """
        Validate the XML against the XSD schema.

        Args:
            xml_string: Optional XML string to validate. If not provided,
                       generates XML from the current order data.

        Returns:
            Tuple[bool, List[str]]: A tuple containing:
                - bool: True if validation passed, False otherwise
                - List[str]: List of validation error messages (empty if valid)

        Raises:
            ImportError: If lxml is not installed
            FileNotFoundError: If the XSD file is not found

        Example:
            ```python
            order_data = NormalOrderData(orders=[...])
            is_valid, errors = order_data.validate_against_xsd()
            if not is_valid:
                for error in errors:
                    print(f"Validation error: {error}")
            ```
        """
        if lxml_etree is None:
            raise ImportError(
                "lxml is required for XSD validation. "
                "Install it with: pip install lxml"
            )

        xsd_path = self.get_xsd_path()
        if not xsd_path.exists():
            raise FileNotFoundError(f"XSD schema file not found: {xsd_path}")

        # Generate XML if not provided
        if xml_string is None:
            xml_string = self.generate_xml(validate=False)

        errors: List[str] = []

        try:
            # Parse the XSD schema
            with open(xsd_path, "rb") as xsd_file:
                xsd_doc = lxml_etree.parse(xsd_file)
                xsd_schema = lxml_etree.XMLSchema(xsd_doc)

            # Parse the XML
            xml_doc = lxml_etree.fromstring(xml_string.encode("utf-8"))

            # Validate
            is_valid: bool = xsd_schema.validate(xml_doc)

            if not is_valid:
                for error in xsd_schema.error_log:  # type: ignore[union-attr]
                    errors.append(f"Line {error.line}: {error.message}")  # type: ignore

            return is_valid, errors

        except lxml_etree.XMLSyntaxError as e:
            errors.append(f"XML syntax error: {e}")
            return False, errors
        except lxml_etree.XMLSchemaParseError as e:
            errors.append(f"XSD schema parse error: {e}")
            return False, errors

    def generate_and_validate_xml(self) -> str:
        """
        Generate XML and validate it against the XSD schema.

        Returns:
            str: Valid XML string

        Raises:
            ValueError: If XML validation fails
            ImportError: If lxml is not installed
            FileNotFoundError: If the XSD file is not found

        Example:
            ```python
            order_data = NormalOrderData(orders=[...])
            try:
                xml = order_data.generate_and_validate_xml()
                print("XML is valid!")
            except ValueError as e:
                print(f"Validation failed: {e}")
            ```
        """
        xml_string = self.generate_xml(validate=True)
        is_valid, errors = self.validate_against_xsd(xml_string)

        if not is_valid:
            error_msg = "XML validation against XSD failed:\n" + "\n".join(errors)
            raise ValueError(error_msg)

        return xml_string
