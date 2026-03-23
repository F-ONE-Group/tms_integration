"""Consignment types for Carlo TMS integration based on FOneOrderImport-v3.xsd."""

from typing import Optional, List
from datetime import datetime, time, date
from decimal import Decimal
from pydantic import BaseModel, Field

from .enums import (
    ImportExportAction,
    Incoterms,
    DeliveryTerms,
    TransportDateType,
    ConsignmentPaymentType,
    PaymentStatus,
    ContainerLoadType,
    HazardousMaterial,
    WaterHazardClass,
    FreightType,
    RegulatedEntityCategory,
    MovementType,
)
from .base import (
    Weights,
    Size,
    Dimensions,
    Money,
    ConsignmentTimes,
    ConsignmentLoadingUnitItem,
    DangerousGoods,
    AmountData,
    SaleType,
    TrafficType,
    TransportType,
    VehicleType,
    Address,
    AreaRelation,
    ContraAccountGroup,
    Currency,
    ContainerType,
    CustomTypeValue,
    Country,
)
from .business_partner import (
    BusinessPartner,
    ConsignmentBusinessPartner,
    ConsignmentContactPerson,
)


class ConsignmentCustomFields(BaseModel):
    """Custom fields for consignment."""

    custom_type_value1: Optional[CustomTypeValue] = Field(
        None, serialization_alias="CustomTypeValue1"
    )
    custom_type_value2: Optional[CustomTypeValue] = Field(
        None, serialization_alias="CustomTypeValue2"
    )
    custom_type_value3: Optional[CustomTypeValue] = Field(
        None, serialization_alias="CustomTypeValue3"
    )
    custom_type_value4: Optional[CustomTypeValue] = Field(
        None, serialization_alias="CustomTypeValue4"
    )
    custom_type_value5: Optional[CustomTypeValue] = Field(
        None, serialization_alias="CustomTypeValue5"
    )
    custom_type_value6: Optional[CustomTypeValue] = Field(
        None, serialization_alias="CustomTypeValue6"
    )
    custom_type_value7: Optional[CustomTypeValue] = Field(
        None, serialization_alias="CustomTypeValue7"
    )
    custom_type_value8: Optional[CustomTypeValue] = Field(
        None, serialization_alias="CustomTypeValue8"
    )
    custom_type_value9: Optional[CustomTypeValue] = Field(
        None, serialization_alias="CustomTypeValue9"
    )
    custom_type_value10: Optional[CustomTypeValue] = Field(
        None, serialization_alias="CustomTypeValue10"
    )
    custom_bool1: Optional[bool] = Field(None, serialization_alias="CustomBool1")
    custom_bool2: Optional[bool] = Field(None, serialization_alias="CustomBool2")
    custom_bool3: Optional[bool] = Field(None, serialization_alias="CustomBool3")
    custom_bool4: Optional[bool] = Field(None, serialization_alias="CustomBool4")
    custom_bool5: Optional[bool] = Field(None, serialization_alias="CustomBool5")
    custom_bool6: Optional[bool] = Field(None, serialization_alias="CustomBool6")
    custom_bool7: Optional[bool] = Field(None, serialization_alias="CustomBool7")
    custom_bool8: Optional[bool] = Field(None, serialization_alias="CustomBool8")
    custom_bool9: Optional[bool] = Field(None, serialization_alias="CustomBool9")
    custom_bool10: Optional[bool] = Field(None, serialization_alias="CustomBool10")
    custom_string1: Optional[str] = Field(
        None, max_length=255, serialization_alias="CustomString1"
    )
    custom_string2: Optional[str] = Field(
        None, max_length=255, serialization_alias="CustomString2"
    )
    custom_string3: Optional[str] = Field(
        None, max_length=255, serialization_alias="CustomString3"
    )
    custom_string4: Optional[str] = Field(
        None, max_length=255, serialization_alias="CustomString4"
    )
    custom_string5: Optional[str] = Field(
        None, max_length=255, serialization_alias="CustomString5"
    )
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
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class ConsignmentAirAndSea(BaseModel):
    """Air and sea freight specific fields."""

    is_shipper_secure: Optional[bool] = Field(
        None, serialization_alias="IsShipperSecure"
    )
    transport_way: Optional[MovementType] = Field(
        None, serialization_alias="TransportWay"
    )
    freight_type: Optional[FreightType] = Field(None, serialization_alias="FreightType")
    regulated_entity_category: Optional[RegulatedEntityCategory] = Field(
        None, serialization_alias="RegulatedEntityCategory"
    )
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class ConsignmentItem(BaseModel):
    """Consignment item (position)."""

    item_number: Optional[int] = Field(None, serialization_alias="ItemNumber")
    quantity: Optional[Decimal] = Field(None, serialization_alias="Quantity")
    content1: Optional[str] = Field(
        None, max_length=2000, serialization_alias="Content1"
    )
    content2: Optional[str] = Field(
        None, max_length=2000, serialization_alias="Content2"
    )
    weights: Optional[Weights] = Field(None, serialization_alias="Weights")
    size: Optional[Size] = Field(None, serialization_alias="Size")
    storage_places: Optional[Decimal] = Field(None, serialization_alias="StoragePlaces")
    mark: Optional[str] = Field(None, max_length=255, serialization_alias="Mark")
    loading_unit_item: Optional[ConsignmentLoadingUnitItem] = Field(
        None, serialization_alias="LoadingUnitItem"
    )
    dangerous_goods: Optional[DangerousGoods] = Field(
        None, serialization_alias="DangerousGoods"
    )
    hazardous_material: Optional[HazardousMaterial] = Field(
        None, serialization_alias="HazardousMaterial"
    )
    packaging: Optional[str] = Field(
        None, max_length=10, serialization_alias="Packaging"
    )
    float1: Optional[Decimal] = Field(None, serialization_alias="Float1")
    float2: Optional[Decimal] = Field(None, serialization_alias="Float2")
    float3: Optional[Decimal] = Field(None, serialization_alias="Float3")
    float4: Optional[Decimal] = Field(None, serialization_alias="Float4")
    float5: Optional[Decimal] = Field(None, serialization_alias="Float5")
    custom_float6: Optional[Decimal] = Field(None, serialization_alias="CustomFloat6")
    custom_float7: Optional[Decimal] = Field(None, serialization_alias="CustomFloat7")
    custom_float8: Optional[Decimal] = Field(None, serialization_alias="CustomFloat8")
    custom_float9: Optional[Decimal] = Field(None, serialization_alias="CustomFloat9")
    custom_float10: Optional[Decimal] = Field(None, serialization_alias="CustomFloat10")
    best_before_date: Optional[datetime] = Field(
        None, serialization_alias="BestBeforeDate"
    )
    storage_period: Optional[datetime] = Field(
        None, serialization_alias="StoragePeriod"
    )
    temperature_in_celsius: Optional[Decimal] = Field(
        None, serialization_alias="TemperatureInCelsius"
    )
    temperature_variation_in_celsius: Optional[Decimal] = Field(
        None, serialization_alias="TemperatureVariationInCelsius"
    )
    water_hazard_class: Optional[WaterHazardClass] = Field(
        None, serialization_alias="WaterHazardClass"
    )
    origin_country: Optional[Country] = Field(None, serialization_alias="OriginCountry")
    commodity_tariff_code: Optional[str] = Field(
        None, max_length=20, serialization_alias="CommodityTariffCode"
    )
    net_mass: Optional[Decimal] = Field(None, serialization_alias="NetMass")
    article_number: Optional[str] = Field(
        None, max_length=30, serialization_alias="ArticleNumber"
    )
    unit: Optional[str] = Field(None, max_length=10, serialization_alias="Unit")
    fzg_matchcode: Optional[str] = Field(
        None, max_length=10, serialization_alias="FzgMatchcode"
    )
    fzg_description: Optional[str] = Field(
        None, max_length=256, serialization_alias="FzgDescription"
    )
    ean_code: Optional[str] = Field(None, max_length=35, serialization_alias="EanCode")
    price_per_unit: Optional[Money] = Field(None, serialization_alias="PricePerUnit")
    total_price: Optional[Money] = Field(None, serialization_alias="TotalPrice")
    article_quantity: Optional[Decimal] = Field(
        None, serialization_alias="ArticleQuantity"
    )
    manufacturer: Optional[str] = Field(
        None, max_length=255, serialization_alias="Manufacturer"
    )
    currency_matchcode: Optional[str] = Field(
        None, max_length=3, serialization_alias="CurrencyMatchcode"
    )
    iso_currency_code: Optional[str] = Field(
        None, max_length=3, serialization_alias="IsoCurrencyCode"
    )
    batch_number: Optional[str] = Field(
        None, max_length=30, serialization_alias="BatchNumber"
    )
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")


class Consignment(BaseModel):
    """Consignment / transport order."""

    item_number: Optional[int] = Field(None, serialization_alias="ItemNumber")
    external_number: Optional[str] = Field(
        None, max_length=50, serialization_alias="ExternalNumber"
    )
    sender: Optional[ConsignmentBusinessPartner] = Field(
        None, serialization_alias="Sender"
    )
    sender_contact_person: Optional[ConsignmentContactPerson] = Field(
        None, serialization_alias="SenderContactPerson"
    )
    receiver: Optional[ConsignmentBusinessPartner] = Field(
        None, serialization_alias="Receiver"
    )
    receiver_contact_person: Optional[ConsignmentContactPerson] = Field(
        None, serialization_alias="ReceiverContactPerson"
    )
    different_loading_point: Optional[ConsignmentBusinessPartner] = Field(
        None, serialization_alias="DifferentLoadingPoint"
    )
    different_delivery_point: Optional[ConsignmentBusinessPartner] = Field(
        None, serialization_alias="DifferentDeliveryPoint"
    )
    loading_unit_items: Optional[List[ConsignmentLoadingUnitItem]] = Field(
        None, serialization_alias="LoadingUnitItems"
    )
    consignment_items: Optional[List[ConsignmentItem]] = Field(
        None, serialization_alias="ConsignmentItems"
    )
    times: Optional[ConsignmentTimes] = Field(None, serialization_alias="Times")
    flat_rate_customer: Optional[AmountData] = Field(
        None, serialization_alias="FlatRateCustomer"
    )
    flat_rate_receiver: Optional[AmountData] = Field(
        None, serialization_alias="FlatRateReceiver"
    )
    incoterms: Optional[Incoterms] = Field(None, serialization_alias="Incoterms")
    delivery_terms: Optional[DeliveryTerms] = Field(
        None, serialization_alias="DeliveryTerms"
    )
    sale_type: Optional[SaleType] = Field(None, serialization_alias="SaleType")
    traffic_type: Optional[TrafficType] = Field(None, serialization_alias="TrafficType")
    transport_type: Optional[TransportType] = Field(
        None, serialization_alias="TransportType"
    )
    execution_date: Optional[date] = Field(None, serialization_alias="ExecutionDate")
    pickup: Optional[bool] = Field(None, serialization_alias="Pickup")
    pickup_splitting_business_partner: Optional[BusinessPartner] = Field(
        None, serialization_alias="PickupSplittingBusinessPartner"
    )
    default_carrier: Optional[BusinessPartner] = Field(
        None, serialization_alias="DefaultCarrier"
    )
    sender_terminal: Optional[BusinessPartner] = Field(
        None, serialization_alias="SenderTerminal"
    )
    receiver_terminal: Optional[BusinessPartner] = Field(
        None, serialization_alias="ReceiverTerminal"
    )
    matchcode: Optional[str] = Field(
        None, max_length=10, serialization_alias="Matchcode"
    )
    container_number: Optional[str] = Field(
        None, max_length=40, serialization_alias="ContainerNumber"
    )
    loading_date_type: Optional[TransportDateType] = Field(
        None, serialization_alias="LoadingDateType"
    )
    delivery_date_type: Optional[TransportDateType] = Field(
        None, serialization_alias="DeliveryDateType"
    )
    initial_costs_tax_free: Optional[Money] = Field(
        None, serialization_alias="InitialCostsTaxFree"
    )
    initial_costs_taxable: Optional[Money] = Field(
        None, serialization_alias="InitialCostsTaxable"
    )
    cash_on_delivery_gross_amount: Optional[Money] = Field(
        None, serialization_alias="CashOnDeliveryGrossAmount"
    )
    cash_on_delivery_tax_free: Optional[Money] = Field(
        None, serialization_alias="CashOnDeliveryTaxFree"
    )
    cash_on_delivery_taxable: Optional[Money] = Field(
        None, serialization_alias="CashOnDeliveryTaxable"
    )
    cash_on_delivery_value_added_tax: Optional[Money] = Field(
        None, serialization_alias="CashOnDeliveryValueAddedTax"
    )
    cash_on_delivery_value_added_tax_rate_in_percent: Optional[Decimal] = Field(
        None, serialization_alias="CashOnDeliveryValueAddedTaxRateInPercent"
    )
    cash_on_delivery_currency: Optional[Currency] = Field(
        None, serialization_alias="CashOnDeliveryCurrency"
    )
    value_of_goods: Optional[Money] = Field(None, serialization_alias="ValueOfGoods")
    value_of_goods_currency: Optional[Currency] = Field(
        None, serialization_alias="ValueOfGoodsCurrency"
    )
    payment_type: Optional[ConsignmentPaymentType] = Field(
        None, serialization_alias="PaymentType"
    )
    payment_status: Optional[PaymentStatus] = Field(
        None, serialization_alias="PaymentStatus"
    )
    fin_acc_cost_center1: Optional[str] = Field(
        None, max_length=20, serialization_alias="FinAccCostCenter1"
    )
    fin_acc_cost_center2: Optional[str] = Field(
        None, max_length=20, serialization_alias="FinAccCostCenter2"
    )
    fin_acc_debtor_contra_account_group: Optional[ContraAccountGroup] = Field(
        None, serialization_alias="FinAccDebtorContraAccountGroup"
    )
    fin_acc_creditor_contra_account_group: Optional[ContraAccountGroup] = Field(
        None, serialization_alias="FinAccCreditorContraAccountGroup"
    )
    named_location: Optional[Address] = Field(None, serialization_alias="NamedLocation")
    kilometers: Optional[Decimal] = Field(None, serialization_alias="Kilometers")
    quantity: Optional[Decimal] = Field(None, serialization_alias="Quantity")
    weights: Optional[Weights] = Field(None, serialization_alias="Weights")
    dimensions: Optional[Dimensions] = Field(None, serialization_alias="Dimensions")
    required_storage_places: Optional[Decimal] = Field(
        None, serialization_alias="RequiredStoragePlaces"
    )
    timeframe: Optional[time] = Field(None, serialization_alias="Timeframe")
    named_place: Optional[str] = Field(
        None, max_length=40, serialization_alias="NamedPlace"
    )
    additional_agreement: Optional[str] = Field(
        None, max_length=40, serialization_alias="AdditionalAgreement"
    )
    calculation_default: Optional[str] = Field(
        None, max_length=10, serialization_alias="CalculationDefault"
    )
    flat_rate_carrier: Optional[AmountData] = Field(
        None, serialization_alias="FlatRateCarrier"
    )
    vehicle_type: Optional[VehicleType] = Field(None, serialization_alias="VehicleType")
    sender_relation: Optional[AreaRelation] = Field(
        None, serialization_alias="SenderRelation"
    )
    receiver_relation: Optional[AreaRelation] = Field(
        None, serialization_alias="ReceiverRelation"
    )
    abs_emp_relation: Optional[AreaRelation] = Field(
        None, serialization_alias="AbsEmpRelation"
    )
    maximum_size: Optional[Size] = Field(None, serialization_alias="MaximumSize")
    maximum_weight_in_kilogram: Optional[Decimal] = Field(
        None, serialization_alias="MaximumWeightInKilogram"
    )
    loading_duration_in_minutes: Optional[int] = Field(
        None, serialization_alias="LoadingDurationInMinutes"
    )
    unloading_duration_in_minutes: Optional[int] = Field(
        None, serialization_alias="UnloadingDurationInMinutes"
    )
    contains_dangerous_goods: Optional[bool] = Field(
        None, serialization_alias="ContainsDangerousGoods"
    )
    custom_fields: Optional[ConsignmentCustomFields] = Field(
        None, serialization_alias="CustomFields"
    )
    is_heavy_duty_transport: Optional[bool] = Field(
        None, serialization_alias="IsHeavyDutyTransport"
    )
    air_and_sea: Optional[ConsignmentAirAndSea] = Field(
        None, serialization_alias="AirAndSea"
    )
    container_type: Optional[ContainerType] = Field(
        None, serialization_alias="ContainerType"
    )
    load_type: Optional[ContainerLoadType] = Field(None, serialization_alias="LoadType")
    action: Optional[ImportExportAction] = Field(None, serialization_alias="Action")
