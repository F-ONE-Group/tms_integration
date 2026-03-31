"""Business partner types for Carlo TMS integration based on FOneOrderImport-v3.xsd."""

from typing import Optional, List
from pydantic import BaseModel, Field

from .enums import ImportExportAction, InttraReferenceType
from .base import Address


class ContactPerson(BaseModel):
    """Contact person from master data."""

    number: Optional[int] = Field(None, serialization_alias="Number")
    matchcode: Optional[str] = Field(
        None, max_length=10, serialization_alias="Matchcode"
    )
    first_name: Optional[str] = Field(
        None, max_length=20, serialization_alias="FirstName"
    )
    last_name: Optional[str] = Field(
        None, max_length=20, serialization_alias="LastName"
    )
    phone_number: Optional[str] = Field(
        None, max_length=30, serialization_alias="PhoneNumber"
    )
    mobile_number: Optional[str] = Field(
        None, max_length=30, serialization_alias="MobileNumber"
    )
    fax_number: Optional[str] = Field(
        None, max_length=30, serialization_alias="FaxNumber"
    )
    email_address: Optional[str] = Field(
        None, max_length=255, serialization_alias="EmailAddress"
    )
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class BusinessPartner(BaseModel):
    """Business partner from CarLo master data."""

    number: Optional[int] = Field(None, serialization_alias="Number")
    external_number: Optional[str] = Field(
        None, max_length=20, serialization_alias="ExternalNumber"
    )
    matchcode: Optional[str] = Field(
        None, max_length=10, serialization_alias="Matchcode"
    )
    global_location_number: Optional[str] = Field(
        None, max_length=50, serialization_alias="GlobalLocationNumber"
    )
    name1: Optional[str] = Field(None, max_length=40, serialization_alias="Name1")
    name2: Optional[str] = Field(None, max_length=40, serialization_alias="Name2")
    name3: Optional[str] = Field(None, max_length=40, serialization_alias="Name3")
    name4: Optional[str] = Field(None, max_length=40, serialization_alias="Name4")
    phone_number_head_office: Optional[str] = Field(
        None, max_length=30, serialization_alias="PhoneNumberHeadOffice"
    )
    contact_persons: Optional[List[ContactPerson]] = Field(
        None, serialization_alias="ContactPersons"
    )
    appendix: Optional[str] = Field(None, max_length=35, serialization_alias="Appendix")
    fin_acc_account_debtor: Optional[str] = Field(
        None, max_length=20, serialization_alias="FinAccAccountDebtor"
    )
    fin_acc_account_creditor: Optional[str] = Field(
        None, max_length=20, serialization_alias="FinAccAccountCreditor"
    )
    inttra_ref_number: Optional[str] = Field(
        None, max_length=50, serialization_alias="InttraRefNumber"
    )
    inttra_ref_type: Optional[InttraReferenceType] = Field(
        None, serialization_alias="InttraRefType"
    )
    home_edit_address: Optional[Address] = Field(
        None, serialization_alias="HomeEditAddress"
    )
    sender_receiver: Optional[bool] = Field(None, serialization_alias="SenderReceiver")
    freight_business_partner: Optional[bool] = Field(
        None, serialization_alias="FreightBusinessPartner"
    )
    value_added_tax_number: Optional[str] = Field(
        None, max_length=30, serialization_alias="ValueAddedTaxNumber"
    )
    vat_iso_two_character_country_code: Optional[str] = Field(
        None, max_length=2, serialization_alias="VATIsoTwoCharacterCountryCode"
    )
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class ConsignmentContactPerson(BaseModel):
    """Free contact person for consignment."""

    first_name: Optional[str] = Field(
        None, max_length=20, serialization_alias="FirstName"
    )
    last_name: Optional[str] = Field(
        None, max_length=20, serialization_alias="LastName"
    )
    phone_number: Optional[str] = Field(
        None, max_length=30, serialization_alias="PhoneNumber"
    )
    email_address: Optional[str] = Field(
        None, max_length=255, serialization_alias="EmailAddress"
    )
    master_data_contact_person: Optional[ContactPerson] = Field(
        None, serialization_alias="MasterDataContactPerson"
    )
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class ConsignmentBusinessPartner(BaseModel):
    """Free consignment business partner (Sender/Receiver/etc.)."""

    master_data_business_partner: Optional[BusinessPartner] = Field(
        None, serialization_alias="MasterDataBusinessPartner"
    )
    name1: Optional[str] = Field(None, max_length=40, serialization_alias="Name1")
    name2: Optional[str] = Field(None, max_length=40, serialization_alias="Name2")
    street: Optional[str] = Field(None, max_length=60, serialization_alias="Street")
    house_number: Optional[str] = Field(
        None, max_length=10, serialization_alias="HouseNumber"
    )
    country: Optional[str] = Field(
        None, max_length=2, serialization_alias="Country"
    )  # ISO 2-char country code
    zip_code: Optional[str] = Field(None, max_length=10, serialization_alias="ZipCode")
    city1: Optional[str] = Field(None, max_length=70, serialization_alias="City1")
    city2: Optional[str] = Field(None, max_length=70, serialization_alias="City2")
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")
