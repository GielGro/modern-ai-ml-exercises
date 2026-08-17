# HomeValue data dictionary

Each row represents one residential property sale. `sale_price` is present only in training data and is an inflation-normalized course target in US dollars.

| Field | Type | Meaning |
|---|---|---|
| `property_id` | identifier | Random course identifier; not predictive |
| `dwelling_type` | category | Assessor dwelling classification |
| `zoning` | category | Zoning classification |
| `lot_frontage_ft` | numeric | Street-connected frontage in feet |
| `lot_area_sqft` | numeric | Lot area in square feet |
| `lot_shape` | category | Regularity of lot shape |
| `neighborhood` | category | Ames neighborhood code |
| `building_type` | category | Detached, duplex, or townhouse form |
| `house_style` | category | Stories and finished-level configuration |
| `overall_quality` | ordinal 1–10 | Overall material and finish quality |
| `overall_condition` | ordinal 1–10 | Overall condition |
| `year_built` | integer | Original construction year |
| `year_remodeled` | integer | Remodel year; equals build year when not remodeled |
| `exterior_quality` | ordinal category | Exterior material quality |
| `foundation` | category | Foundation type |
| `basement_quality` | ordinal category | Basement quality; missing can indicate no basement |
| `basement_sqft` | numeric | Total basement area |
| `central_air` | binary category | Central air conditioning indicator |
| `living_area_sqft` | numeric | Above-ground living area |
| `full_bathrooms` | integer | Full bathrooms above grade |
| `bedrooms` | integer | Bedrooms above grade |
| `kitchen_quality` | ordinal category | Kitchen quality |
| `fireplaces` | integer | Number of fireplaces |
| `garage_type` | category | Garage configuration; missing can indicate no garage |
| `garage_capacity` | numeric | Vehicle capacity |
| `deck_sqft` | numeric | Wood deck area |
| `sale_month` | integer 1–12 | Month of sale |
| `sale_year` | integer | Year of sale |
| `sale_price` | positive numeric | Target available only in training data |

Category codes retain the original Ames meaning. Full source documentation: https://jse.amstat.org/v19n3/decock/DataDocumentation.txt
