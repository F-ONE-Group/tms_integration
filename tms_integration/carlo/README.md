# Carlo TMS Integration

Pydantic models for Carlo (Soloplan) TMS integration based on the FOneOrderImport-v3.xsd schema.

## Overview

This module provides Pydantic models for creating and validating order data for import into the Carlo TMS system. The models are based on the official XSD schema and provide:

- Full type validation with Pydantic
- XML generation for order import
- Similar pattern to `LisInAuftrag` used in lis_winsped module

## Usage

### Basic Order Creation

```python
from tms_integration.carlo.models import (
    NormalOrderData, Order, Consignment,
    ConsignmentBusinessPartner, BusinessPartner,
    ConsignmentItem, ConsignmentTimes, Weights,
    ConsignmentCustomFields, CustomTypeValue,
    ConsignmentLoadingUnitItem, LoadingUnit
)
from datetime import date, datetime
from decimal import Decimal

# Create an order
order = Order(
    date=date(2024, 1, 26),
    order_date=date(2024, 1, 26),
    customer=BusinessPartner(number=2010288),
    consignments=[
        Consignment(
            item_number=1,
            external_number='ORDER-001',
            sender=ConsignmentBusinessPartner(
                name1='Sender Company GmbH',
                street='Sender Street',
                house_number='1',
                country='DE',
                zip_code='12345',
                city1='Berlin'
            ),
            receiver=ConsignmentBusinessPartner(
                name1='Receiver Company GmbH',
                street='Receiver Street',
                house_number='2',
                country='DE',
                zip_code='54321',
                city1='Munich'
            ),
            loading_unit_items=[
                ConsignmentLoadingUnitItem(
                    item_number=1,
                    generate_loading_unit_postings=1,  # Yes
                    quantity=100,
                    loading_unit=LoadingUnit(matchcode='EUP')
                )
            ],
            consignment_items=[
                ConsignmentItem(
                    item_number=1,
                    quantity=Decimal('100'),
                    weights=Weights(
                        effective_weight_in_kilogram=Decimal('1000'),
                        freight_weight_in_kilogram=Decimal('1000'),
                        carrier_weight_in_kilogram=Decimal('1000')
                    ),
                    storage_places=Decimal('5'),
                    packaging='Europalett'
                )
            ],
            times=ConsignmentTimes(
                loading_date_start=datetime(2024, 1, 26, 8, 0, 0),
                loading_date_end=datetime(2024, 1, 26, 10, 0, 0),
                delivery_date_start=datetime(2024, 1, 26, 14, 0, 0),
                delivery_date_end=datetime(2024, 1, 26, 16, 0, 0)
            )
        )
    ],
    is_empty_trip=False
)

# Create order data and generate XML
order_data = NormalOrderData(orders=[order])
xml_string = order_data.generate_xml()
print(xml_string)
```

### Using with SoloplanCarlo SFTP Client

```python
from tms_integration.carlo import SoloplanCarlo
from tms_integration.carlo.models import NormalOrderData, Order, ...

# Create order data
order_data = NormalOrderData(orders=[...])

# Initialize SFTP client and import
carlo = SoloplanCarlo(
    hostname='sftp.example.com',
    username='user',
    password='password',
    import_dest_folder='/import/'
)
carlo.import_auftrag(order_data, import_prefix='ORDER_')
```

## Available Models

### Main Classes

- `NormalOrderData` - Main class for order data (similar to `LisInAuftrag`)
- `Order` - Individual order
- `OrderData` - Collection of orders

### Enums

- `ImportExportAction` - Create, Update, Delete, UpdateOrCreate
- `OrderContext` - Normal, Storage, RemoveFromStorage, etc.
- `Incoterms` - EXW, FCA, CPT, CIP, DAP, DPU, DDP, etc.
- `DeliveryTerms` - FreiHaus, AbWerk, Unfrei
- `TransportDateType` - On, By, From, Between, etc.
- `ConsignmentPaymentType` - Undefined, AdvanceDebit, Invoice
- `PaymentStatus` - Unknown, Unpaid, Paid, Installment
- `ContainerLoadType` - FCL, LCL, BCL, FTL, LTL, AirFreight
- `HazardousMaterial` - None, Yes, LimitedQuantities, etc.
- `WaterHazardClass` - WGK1, WGK2, WGK3
- `FreightType` - RoadFreight, AirFreight, SeaFreight
- And more...

### Business Partner Types

- `BusinessPartner` - Master data business partner
- `ConsignmentBusinessPartner` - Free consignment sender/receiver
- `ContactPerson` - Contact person from master data
- `ConsignmentContactPerson` - Free contact person

### Consignment Types

- `Consignment` - Transport order
- `ConsignmentItem` - Position/item within a consignment
- `ConsignmentTimes` - Loading and delivery dates/times
- `ConsignmentCustomFields` - Custom boolean, string, float, datetime fields
- `ConsignmentAirAndSea` - Air/sea freight specific fields

### Common Types

- `Address` - Address information
- `Country` - Country with ISO codes
- `Weights` - Effective, freight, and carrier weights
- `Size` / `Dimensions` - Length, width, height
- `Money` - Amount with currency
- `LoadingUnit` - Loading unit (e.g., pallet)
- `ConsignmentLoadingUnitItem` - Loading unit item for consignment
- `CustomTypeValue` - Custom type with number, matchcode, designation
- And more...

## Validation

The `NormalOrderData` class provides two levels of validation:

### Basic Validation

```python
order_data = NormalOrderData(orders=[order])

# Validate explicitly
order_data.validate_orders()  # Raises ValueError if validation fails

# Or generate XML with validation (default)
xml = order_data.generate_xml(validate=True)

# Skip validation if needed
xml = order_data.generate_xml(validate=False)
```

### XSD Schema Validation

Validate the generated XML against the official XSD schema (requires `lxml`):

```python
order_data = NormalOrderData(orders=[order])

# Validate and get detailed errors
is_valid, errors = order_data.validate_against_xsd()
if not is_valid:
    for error in errors:
        print(f"Validation error: {error}")

# Or generate and validate in one step (raises ValueError on failure)
xml = order_data.generate_and_validate_xml()
```

## Schema Reference

The models are based on the XSD schema located at:
`tms_integration/carlo/models/xsd/FOneOrderImport-v3.xsd`
