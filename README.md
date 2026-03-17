# Ritchter-s_Predictor
Algoritmo di intelligenza artificiale volto alla predizione dei danni di un terremoto
DrivenData. (2019). Richter's Predictor: Modeling Earthquake Damage. Retrieved [Month Day Year] from https://www.drivendata.org/competitions/57/nepal-earthquake.
# Earthquake Damage Prediction - Dataset Guide

## 📝 Problem Description
The goal is to predict the **damage_grade**, an ordinal variable representing the level of damage to a building hit by the Gorkha earthquake.

| Damage Grade | Description |
| :--- | :--- |
| **1** | Low damage |
| **2** | Medium amount of damage |
| **3** | Almost complete destruction |

---

## 📊 Features Dictionary

The dataset contains 39 columns: `building_id` (unique identifier) and 38 predictive features. 

> [!NOTE]
> **Categorical Obfuscation:** Values for categorical variables are represented by random lowercase ASCII characters. The same character in different columns does **not** imply the same original value.

| Feature Name | Type | Description | Possible Values / Range |
| :--- | :--- | :--- | :--- |
| **geo_level_1_id** | Int | Largest geographic region | 0 - 30 |
| **geo_level_2_id** | Int | Intermediate sub-region | 0 - 1427 |
| **geo_level_3_id** | Int | Most specific sub-region | 0 - 12567 |
| **count_floors_pre_eq** | Int | Number of floors before the earthquake | Integer |
| **age** | Int | Age of the building in years | Integer |
| **area_percentage** | Int | Normalized area of the building footprint | Integer |
| **height_percentage** | Int | Normalized height of the building footprint | Integer |
| **land_surface_condition** | Cat | Surface condition of the land | **n, o, t** |
| **foundation_type** | Cat | Type of foundation used | **h, i, r, u, w** |
| **roof_type** | Cat | Type of roof used | **n, q, x** |
| **ground_floor_type** | Cat | Type of the ground floor | **f, m, v, x, z** |
| **other_floor_type** | Cat | Construction used in higher floors | **j, q, s, x** |
| **position** | Cat | Position of the building | **j, o, s, t** |
| **plan_configuration** | Cat | Building plan configuration | **a, c, d, f, m, n, o, q, s, u** |
| **has_superstructure_adobe_mud** | Binary | Built with Adobe/Mud | 0: No, 1: Yes |
| **has_superstructure_mud_mortar_stone** | Binary | Built with Mud Mortar - Stone | 0: No, 1: Yes |
| **has_superstructure_stone_flag** | Binary | Built with Stone | 0: No, 1: Yes |
| **has_superstructure_cement_mortar_stone** | Binary | Built with Cement Mortar - Stone | 0: No, 1: Yes |
| **has_superstructure_mud_mortar_brick** | Binary | Built with Mud Mortar - Brick | 0: No, 1: Yes |
| **has_superstructure_cement_mortar_brick** | Binary | Built with Cement Mortar - Brick | 0: No, 1: Yes |
| **has_superstructure_timber** | Binary | Built with Timber | 0: No, 1: Yes |
| **has_superstructure_bamboo** | Binary | Built with Bamboo | 0: No, 1: Yes |
| **has_superstructure_rc_non_engineered** | Binary | Built with non-engineered reinforced concrete | 0: No, 1: Yes |
| **has_superstructure_rc_engineered** | Binary | Built with engineered reinforced concrete | 0: No, 1: Yes |
| **has_superstructure_other** | Binary | Built with other materials | 0: No, 1: Yes |
| **legal_ownership_status** | Cat | Legal ownership status of the land | **a, r, v, w** |
| **count_families** | Int | Number of families living in the building | Integer |
| **has_secondary_use** | Binary | Building has any secondary purpose | 0: No, 1: Yes |
| **has_secondary_use_agriculture** | Binary | Used for agricultural purposes | 0: No, 1: Yes |
| **has_secondary_use_hotel** | Binary | Used as a hotel | 0: No, 1: Yes |
| **has_secondary_use_rental** | Binary | Used for rental purposes | 0: No, 1: Yes |
| **has_secondary_use_institution** | Binary | Used as an institution | 0: No, 1: Yes |
| **has_secondary_use_school** | Binary | Used as a school | 0: No, 1: Yes |
| **has_secondary_use_industry** | Binary | Used for industrial purposes | 0: No, 1: Yes |
| **has_secondary_use_health_post** | Binary | Used as a health post | 0: No, 1: Yes |
| **has_secondary_use_gov_office** | Binary | Used as a government office | 0: No, 1: Yes |
| **has_secondary_use_use_police** | Binary | Used as a police station | 0: No, 1: Yes |
| **has_secondary_use_other** | Binary | Used for other secondary purposes | 0: No, 1: Yes |

---

## 📐 Submission Format
The submission should be a CSV file with a header and two columns:

| Column | Type | Description |
| :--- | :--- | :--- |
| **building_id** | Int/Unique | Identifier from the test set |
| **damage_grade** | Int (1-3) | Your predicted damage level |

**Example:**
```csv
building_id,damage_grade
1148,1
5842,3
2593,2