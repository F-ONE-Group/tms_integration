"""Base types for Carlo TMS integration based on FOneOrderImport-v3.xsd."""

from typing import Optional, List
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field

from .enums import ImportExportAction, LoadingUnitPostingsGeneration


class Country(BaseModel):
    """Country information."""

    iso_two_character_country_code: Optional[str] = Field(
        None, max_length=2, serialization_alias="IsoTwoCharacterCountryCode"
    )
    iso_three_character_country_code: Optional[str] = Field(
        None, max_length=3, serialization_alias="IsoThreeCharacterCountryCode"
    )
    iso_numeric_country_code: Optional[str] = Field(
        None, max_length=3, serialization_alias="IsoNumericCountryCode"
    )
    country_id: Optional[str] = Field(
        None, max_length=3, serialization_alias="CountryId"
    )
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class Address(BaseModel):
    """Address information."""

    location1: Optional[str] = Field(
        None, max_length=70, serialization_alias="Location1"
    )
    location2: Optional[str] = Field(
        None, max_length=70, serialization_alias="Location2"
    )
    zip_code: Optional[str] = Field(None, max_length=10, serialization_alias="ZipCode")
    street: Optional[str] = Field(None, max_length=60, serialization_alias="Street")
    house_number: Optional[str] = Field(
        None, max_length=10, serialization_alias="HouseNumber"
    )
    country: Optional[Country] = Field(None, serialization_alias="Country")
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class Weights(BaseModel):
    """Weight information."""

    effective_weight_in_kilogram: Optional[Decimal] = Field(
        None, serialization_alias="EffectiveWeightInKilogram"
    )
    freight_weight_in_kilogram: Optional[Decimal] = Field(
        None, serialization_alias="FreightWeightInKilogram"
    )
    carrier_weight_in_kilogram: Optional[Decimal] = Field(
        None, serialization_alias="CarrierWeightInKilogram"
    )
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class Size(BaseModel):
    """Size dimensions."""

    length_in_meters: Optional[Decimal] = Field(
        None, serialization_alias="LengthInMeters"
    )
    width_in_meters: Optional[Decimal] = Field(
        None, serialization_alias="WidthInMeters"
    )
    height_in_meters: Optional[Decimal] = Field(
        None, serialization_alias="HeightInMeters"
    )
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class Dimensions(BaseModel):
    """Dimension information (linear, area, volume measurements)."""

    meter: Optional[Decimal] = Field(None, serialization_alias="Meter")
    square_meter: Optional[Decimal] = Field(None, serialization_alias="SquareMeter")
    cubic_meter: Optional[Decimal] = Field(None, serialization_alias="CubicMeter")
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class Money(BaseModel):
    """Money value with amount and currency."""

    amount: Decimal = Field(..., serialization_alias="Amount")
    currency: Optional[str] = Field(None, serialization_alias="Currency")


class GeoCoordinate(BaseModel):
    """Geographic coordinates."""

    latitude: Decimal = Field(..., serialization_alias="Latitude")
    longitude: Decimal = Field(..., serialization_alias="Longitude")


class CustomTypeValue(BaseModel):
    """Custom type value."""

    number: Optional[int] = Field(None, serialization_alias="Number")
    matchcode: Optional[str] = Field(
        None, max_length=10, serialization_alias="Matchcode"
    )
    designation: Optional[str] = Field(
        None, max_length=100, serialization_alias="Designation"
    )
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class LoadingUnit(BaseModel):
    """Loading unit master data."""

    number: Optional[int] = Field(None, serialization_alias="Number")
    external_number: Optional[str] = Field(
        None, max_length=35, serialization_alias="ExternalNumber"
    )
    matchcode: Optional[str] = Field(
        None, max_length=10, serialization_alias="Matchcode"
    )
    designation: Optional[str] = Field(
        None, max_length=30, serialization_alias="Designation"
    )
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class ConsignmentLoadingUnitGrai(BaseModel):
    """GRAI number for loading unit."""

    grai_number: Optional[str] = Field(
        None, max_length=50, serialization_alias="GraiNumber"
    )
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class ConsignmentLoadingUnitItem(BaseModel):
    """Loading unit item for consignment."""

    item_number: Optional[int] = Field(None, serialization_alias="ItemNumber")
    generate_loading_unit_postings: Optional[LoadingUnitPostingsGeneration] = Field(
        None, serialization_alias="GenerateLoadingUnitPostings"
    )
    grai_numbers: Optional[List["ConsignmentLoadingUnitGrai"]] = Field(
        None, serialization_alias="GraiNumbers"
    )
    quantity: Optional[int] = Field(None, serialization_alias="Quantity")
    loading_unit: Optional[LoadingUnit] = Field(None, serialization_alias="LoadingUnit")
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class ConsignmentTimes(BaseModel):
    """Times for consignment (loading and delivery dates)."""

    loading_date_start: Optional[datetime] = Field(
        None, serialization_alias="LoadingDateStart"
    )
    loading_date_end: Optional[datetime] = Field(
        None, serialization_alias="LoadingDateEnd"
    )
    delivery_date_start: Optional[datetime] = Field(
        None, serialization_alias="DeliveryDateStart"
    )
    delivery_date_end: Optional[datetime] = Field(
        None, serialization_alias="DeliveryDateEnd"
    )
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class AmountData(BaseModel):
    """Amount data for rates."""

    amount: Optional[Money] = Field(None, serialization_alias="Amount")
    currency: Optional[str] = Field(None, max_length=3, serialization_alias="Currency")
    info: Optional[str] = Field(None, max_length=255, serialization_alias="Info")
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class DangerousGoods(BaseModel):
    """Dangerous goods specification."""

    carrier_number: Optional[str] = Field(
        None, max_length=4, serialization_alias="CarrierNumber"
    )
    technical_name: Optional[str] = Field(
        None, max_length=2000, serialization_alias="TechnicalName"
    )
    additional_text: Optional[str] = Field(
        None, max_length=255, serialization_alias="AdditionalText"
    )
    hazard_class: Optional[str] = Field(
        None, max_length=10, serialization_alias="Class"
    )
    classification_code: Optional[str] = Field(
        None, max_length=10, serialization_alias="ClassificationCode"
    )
    packing_group: Optional[str] = Field(
        None, max_length=10, serialization_alias="PackingGroup"
    )
    un_number: Optional[str] = Field(
        None, max_length=10, serialization_alias="UnNumber"
    )
    are_danger_to_environment: Optional[bool] = Field(
        None, serialization_alias="AreDangerToEnvironment"
    )
    limited_amount: Optional[bool] = Field(None, serialization_alias="LimitedAmount")
    net_weight_in_kilogram: Optional[Decimal] = Field(
        None, serialization_alias="NetWeightInKilogram"
    )
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class SaleType(BaseModel):
    """Sales type."""

    number: Optional[int] = Field(None, serialization_alias="Number")
    external_number: Optional[str] = Field(
        None, max_length=30, serialization_alias="ExternalNumber"
    )
    matchcode: Optional[str] = Field(
        None, max_length=10, serialization_alias="Matchcode"
    )
    designation: Optional[str] = Field(
        None, max_length=40, serialization_alias="Designation"
    )
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class TrafficType(BaseModel):
    """Traffic type."""

    number: Optional[int] = Field(None, serialization_alias="Number")
    external_number: Optional[str] = Field(
        None, max_length=30, serialization_alias="ExternalNumber"
    )
    matchcode: Optional[str] = Field(
        None, max_length=10, serialization_alias="Matchcode"
    )
    designation: Optional[str] = Field(
        None, max_length=40, serialization_alias="Designation"
    )
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class TransportType(BaseModel):
    """Transport type."""

    number: Optional[int] = Field(None, serialization_alias="Number")
    matchcode: Optional[str] = Field(
        None, max_length=10, serialization_alias="Matchcode"
    )
    designation: Optional[str] = Field(
        None, max_length=40, serialization_alias="Designation"
    )
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class VehicleType(BaseModel):
    """Vehicle type."""

    matchcode: Optional[str] = Field(
        None, max_length=10, serialization_alias="Matchcode"
    )
    designation: Optional[str] = Field(
        None, max_length=40, serialization_alias="Designation"
    )
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class Currency(BaseModel):
    """Currency information."""

    matchcode: Optional[str] = Field(
        None, max_length=3, serialization_alias="Matchcode"
    )
    iso_currency_code: Optional[str] = Field(
        None, max_length=3, serialization_alias="IsoCurrencyCode"
    )
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class ContainerType(BaseModel):
    """Container type."""

    number: Optional[int] = Field(None, serialization_alias="Number")
    matchcode: Optional[str] = Field(
        None, max_length=10, serialization_alias="Matchcode"
    )
    designation: Optional[str] = Field(
        None, max_length=40, serialization_alias="Designation"
    )
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class AreaRelation(BaseModel):
    """Area relation information."""

    number: Optional[int] = Field(None, serialization_alias="Number")
    matchcode: Optional[str] = Field(
        None, max_length=10, serialization_alias="Matchcode"
    )
    designation: Optional[str] = Field(
        None, max_length=40, serialization_alias="Designation"
    )
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class ContraAccountGroup(BaseModel):
    """Contra account group for financial accounting."""

    number: Optional[int] = Field(None, serialization_alias="Number")
    matchcode: Optional[str] = Field(
        None, max_length=10, serialization_alias="Matchcode"
    )
    designation: Optional[str] = Field(
        None, max_length=40, serialization_alias="Designation"
    )
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class OrganizationalUnit(BaseModel):
    """Organizational unit."""

    number: Optional[int] = Field(None, serialization_alias="Number")
    matchcode: Optional[str] = Field(
        None, max_length=10, serialization_alias="Matchcode"
    )
    designation: Optional[str] = Field(
        None, max_length=80, serialization_alias="Designation"
    )
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class Header(BaseModel):
    """Header information for the document."""

    send_date: datetime = Field(..., serialization_alias="SendDate")
    export_item_reference: str = Field(..., serialization_alias="ExportItemReference")


class ChannelOfDistribution(BaseModel):
    """Channel of distribution - indicates how the sale came about (e.g., direct sale, phone sale)."""

    matchcode: Optional[str] = Field(
        None, max_length=10, serialization_alias="Matchcode"
    )
    number: Optional[int] = Field(None, serialization_alias="Number")
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class OrderOfferBordereauData(BaseModel):
    """Bordereau data for order/offer."""

    traffic_type: Optional[str] = Field(
        None, max_length=100, serialization_alias="TrafficType"
    )
    sender_id: Optional[str] = Field(
        None, max_length=10, serialization_alias="SenderId"
    )
    receiver_id: Optional[str] = Field(
        None, max_length=10, serialization_alias="ReceiverId"
    )
    carrier_address: Optional[str] = Field(
        None, max_length=2000, serialization_alias="CarrierAddress"
    )
    vehicle_license_plate: Optional[str] = Field(
        None, max_length=30, serialization_alias="VehicleLicensePlate"
    )
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class OrderOfferBaseInformation(BaseModel):
    """Extended information fields for order/offer (Info1-Info20)."""

    info1: Optional[str] = Field(None, max_length=2000, serialization_alias="Info1")
    info2: Optional[str] = Field(None, max_length=2000, serialization_alias="Info2")
    info3: Optional[str] = Field(None, max_length=2000, serialization_alias="Info3")
    info4: Optional[str] = Field(None, max_length=2000, serialization_alias="Info4")
    info5: Optional[str] = Field(None, max_length=2000, serialization_alias="Info5")
    info6: Optional[str] = Field(None, max_length=2000, serialization_alias="Info6")
    info7: Optional[str] = Field(None, max_length=2000, serialization_alias="Info7")
    info8: Optional[str] = Field(None, max_length=2000, serialization_alias="Info8")
    info9: Optional[str] = Field(None, max_length=2000, serialization_alias="Info9")
    info10: Optional[str] = Field(None, max_length=2000, serialization_alias="Info10")
    info11: Optional[str] = Field(None, max_length=2000, serialization_alias="Info11")
    info12: Optional[str] = Field(None, max_length=2000, serialization_alias="Info12")
    info13: Optional[str] = Field(None, max_length=2000, serialization_alias="Info13")
    info14: Optional[str] = Field(None, max_length=2000, serialization_alias="Info14")
    info15: Optional[str] = Field(None, max_length=2000, serialization_alias="Info15")
    info16: Optional[str] = Field(None, max_length=2000, serialization_alias="Info16")
    info17: Optional[str] = Field(None, max_length=2000, serialization_alias="Info17")
    info18: Optional[str] = Field(None, max_length=2000, serialization_alias="Info18")
    info19: Optional[str] = Field(None, max_length=2000, serialization_alias="Info19")
    info20: Optional[str] = Field(None, max_length=2000, serialization_alias="Info20")
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class SsccCurrent(BaseModel):
    """Serial Shipping Container Code (SSCC) current."""

    code: Optional[str] = Field(None, max_length=35, serialization_alias="Code")
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")
