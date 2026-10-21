# Community Vaccination Tracker

PROG211 Object-Oriented Programming 1 – Individual Assignment (Health domain).

A small Python program that tracks vaccine doses for people in a community using anonymous IDs.

## How to run
```
python vaccination_tracker.py
```
Choose `1` for an automatic demo or `2` for an interactive menu. Requires Python 3.8+ (no extra libraries).

## OOP concepts used
| Requirement | Where |
|---|---|
| Two classes with attributes and methods | `Vaccine`, `VaccinationRecord` |
| Object creation and interaction | `record.add_dose(vaccine)` links a record to a vaccine |
| Data structure | A **dictionary** (`records`) stores objects with their ID as key; `add_record()` and `display_records()` |
| Tuples (bonus) | `Vaccine.schedule_months`, `VaccinationRecord.VALID_AGE_GROUPS` |
| Instance methods | `add_dose()`, `update_record()`, `display_info()`, `is_fully_vaccinated()` |
| Class methods (`@classmethod`) | `Vaccine.get_total_vaccines()`, `VaccinationRecord.get_record_count()` |
| Static method | `VaccinationRecord.is_valid_age_group()` |

## Digital Public Goods (DPG) alignment
- **Open-source:** the code is public on GitHub under an open licence (MIT recommended).
- **Inclusive and accessible:** plain-text, keyboard-only interface with simple prompts and clear messages; runs on any low-spec computer, offline.
- **Privacy-respecting:** no names, phone numbers or addresses are stored. People are identified only by an anonymous ID (`V-0001`), age group and community (district/village).
- **Modular and reusable:** each class has one job, so `Vaccine` and `VaccinationRecord` can be reused in other health tools; new vaccines are added without changing code logic.

## Example usage (sample output)
```
=== Adding records ===
  + Record V-0001 added.
  + Record V-0002 added.
  ! Could not add record: age_group must be one of ('child', 'adult', 'elderly')

=== Recording doses ===
  + V-0001: Measles dose 1/2 recorded.
  + V-0001: Measles dose 2/2 recorded.
  ! V-0001 already completed Measles.

=== All records ===
  V-0001 | child | Freetown East
      MEASLES: 2026-09-10, 2026-12-10
  V-0002 | adult | Bo Town
      POLIO: 2026-10-20
```