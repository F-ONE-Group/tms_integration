"""Enum types for Carlo TMS integration based on FOneOrderImport-v3.xsd."""

from enum import IntEnum


class ImportExportAction(IntEnum):
    """Import action tag for specifying create, update, updateorcreate or delete."""

    NONE = 0
    CREATE = 1
    UPDATE = 2
    DELETE = 3
    UPDATE_OR_CREATE = 4


class OrderContext(IntEnum):
    """Order context enumeration."""

    NORMAL = 0
    STORAGE = 10
    REMOVE_FROM_STORAGE = 20
    STORAGE_RELOCATION = 30
    NORMAL_STORAGE_MOVEMENT = 100
    GENERAL_ORDER_WITH_LOADING_UNIT = 200


class Incoterms(IntEnum):
    """Incoterms enumeration."""

    NONE = 0
    EXW = 1  # Ex Works
    FCA = 2  # Free Carrier
    CPT = 3  # Carriage Paid To
    CIP = 4  # Carriage and Insurance Paid To
    DAP = 5  # Delivered at Place
    DPU = 6  # Delivered at Place Unloaded
    DDP = 7  # Delivered Duty Paid
    FAS = 8  # Free Alongside Ship
    FOB = 9  # Free On Board
    CFR = 10  # Cost and Freight
    CIF = 11  # Cost, Insurance and Freight


class DeliveryTerms(IntEnum):
    """Delivery terms enumeration."""

    NONE = 0
    FREI_HAUS = 1  # Free House
    AB_WERK = 2  # Ex Works
    UNFREI = 3  # Freight Collect


class TransportDateType(IntEnum):
    """Transport date type enumeration."""

    NOT_SET = 0
    ON = 1  # Datum genau
    BY = 2  # Datum bis
    FROM = 3  # Datum ab
    BETWEEN = 4  # Datum zwischen
    NOT_BEFORE = 5  # nicht vor
    NOT_AFTER = 6  # nicht nach
    AS_SOON_AS_POSSIBLE = 7  # So bald wie möglich
    AT_THE_EARLIEST = 8  # Datum ab
    AT_THE_LATEST = 9  # Datum bis


class ConsignmentPaymentType(IntEnum):
    """Consignment payment type enumeration."""

    UNDEFINED = 0
    ADVANCE_DEBIT = 1  # Vorkasse
    INVOICE = 2  # Rechnung


class PaymentStatus(IntEnum):
    """Payment status enumeration."""

    UNKNOWN = 0
    UNPAID = 1
    PAID = 2
    INSTALLMENT = 3  # Teilzahlung


class ContainerLoadType(IntEnum):
    """Container load type enumeration."""

    NONE = 0
    FULL_CONTAINER_LOAD = 1  # FCL
    LESS_THAN_CONTAINER_LOAD = 2  # LCL
    BUYERS_CONSOLIDATION = 3  # BCL
    FULL_TRUCK_LOAD = 4  # FTL
    LESS_THAN_TRUCK_LOAD = 5  # LTL
    AIR_FREIGHT = 6


class InttraReferenceType(IntEnum):
    """Inttra reference type enumeration."""

    INTTRA_COMPANY_ID = 0  # Firmen-ID
    INTTRA_PARTNER_ALIAS = 1  # Partner-Alias
    DUNS_CODE = 2  # DUNS-Code


class HazardousMaterial(IntEnum):
    """Hazardous material enumeration."""

    NONE = 0  # Nein
    YES = 1  # Ja
    LIMITED_QUANTITIES = 2  # Begrenzte Menge
    EXCEPTED_QUANTITIES = 3  # Freigestellte Menge
    EXCEPTED_AND_LIMITED_QUANTITIES = 4  # Freigestellte + begrenzte Menge


class WaterHazardClass(IntEnum):
    """Water hazard class enumeration."""

    NONE = -1  # Nicht wassergefährdend
    NOT_SPECIFIED = 0  # (Nicht gesetzt)
    WGK_1 = 1  # schwach wassergefährdend
    WGK_2 = 2  # deutlich wassergefährdend
    WGK_3 = 3  # stark wassergefährdend


class MovementType(IntEnum):
    """Movement type enumeration for air/sea freight."""

    UNDEFINED = 0
    DOOR_TO_DOOR = 1  # D/D
    PORT_TO_DOOR = 2  # P/D
    DOOR_TO_PORT = 3  # D/P
    PORT_TO_PORT = 4  # P/P


class FreightType(IntEnum):
    """Freight type enumeration."""

    NONE = -1  # Nicht definiert
    ROAD_FREIGHT = 0  # Straße
    AIR_FREIGHT = 1  # Luftfracht
    SEA_FREIGHT = 2  # Seefracht


class RegulatedEntityCategory(IntEnum):
    """Regulated entity category for air freight security."""

    UNDEFINED = 0
    KNOWN_CONSIGNOR = 1
    AIRCRAFT_OPERATOR = 2
    REGULATED_AGENT = 3


class LoadingUnitPostingsGeneration(IntEnum):
    """Loading unit postings generation enumeration."""

    YES = 0  # Ja (Note: 0 = Yes in the XSD)
    NO = 1  # Nein
    DECIDE_LATER = 2  # Nicht definiert
