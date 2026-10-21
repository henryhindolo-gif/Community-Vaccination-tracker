

from datetime import date


# --------------------------------------------------------------------------
# TASK 1 - CLASS 1: Vaccine
# --------------------------------------------------------------------------
class Vaccine:
    """A vaccine type and its recommended dose schedule."""

    # Class attribute shared by all vaccines
    total_vaccines = 0

    def __init__(self, code, name, doses_required, schedule_months):
        self.code = code                          # e.g. "MEASLES"
        self.name = name                          # e.g. "Measles"
        self.doses_required = doses_required      # e.g. 2
        # TUPLE (bonus): the recommended schedule never changes
        self.schedule_months = tuple(schedule_months)   # e.g. (9, 15)
        Vaccine.total_vaccines += 1

    # Instance method
    def display_info(self):
        schedule = ", ".join(f"month {m}" for m in self.schedule_months)
        print(f"  [{self.code}] {self.name} | doses: {self.doses_required} | schedule: {schedule}")

    # Class method
    @classmethod
    def get_total_vaccines(cls):
        return cls.total_vaccines


# --------------------------------------------------------------------------
# TASK 1 - CLASS 2: VaccinationRecord
# --------------------------------------------------------------------------
class VaccinationRecord:
    """An anonymous vaccination record for one person."""

    # Class attributes
    record_count = 0
    VALID_AGE_GROUPS = ("child", "adult", "elderly")   # tuple (bonus)

    def __init__(self, age_group, community):
        if not VaccinationRecord.is_valid_age_group(age_group):
            raise ValueError(f"age_group must be one of {self.VALID_AGE_GROUPS}")
        VaccinationRecord.record_count += 1
        self.record_id = f"V-{VaccinationRecord.record_count:04d}"   # anonymous ID
        self.age_group = age_group
        self.community = community                 # district/village only, no address
        self.doses = {}                            # vaccine code -> list of dates

    # ---- Instance methods ----
    def add_dose(self, vaccine, dose_date=None):
        """Record a dose of a vaccine (object interaction: Record <-> Vaccine)."""
        taken = self.doses.setdefault(vaccine.code, [])
        if len(taken) >= vaccine.doses_required:
            print(f"  ! {self.record_id} already completed {vaccine.name}.")
            return False
        taken.append(dose_date or date.today())
        print(f"  + {self.record_id}: {vaccine.name} dose {len(taken)}/{vaccine.doses_required} recorded.")
        return True

    def is_fully_vaccinated(self, vaccine):
        return len(self.doses.get(vaccine.code, [])) >= vaccine.doses_required

    def update_record(self, age_group=None, community=None):
        if age_group:
            if not VaccinationRecord.is_valid_age_group(age_group):
                print("  ! Invalid age group.")
                return
            self.age_group = age_group
        if community:
            self.community = community
        print(f"  ~ {self.record_id} updated.")

    def display_info(self):
        print(f"  {self.record_id} | {self.age_group} | {self.community}")
        if not self.doses:
            print("      (no doses recorded)")
        for code, dates in self.doses.items():
            print(f"      {code}: " + ", ".join(d.isoformat() for d in dates))

    # ---- Class method ----
    @classmethod
    def get_record_count(cls):
        return cls.record_count

    # ---- Static method (needs no object or class data) ----
    @staticmethod
    def is_valid_age_group(age_group):
        return age_group in VaccinationRecord.VALID_AGE_GROUPS


# --------------------------------------------------------------------------
# TASK 2 - DATA STRUCTURE: dictionary (record_id -> VaccinationRecord)
# --------------------------------------------------------------------------
records = {}


def add_record(age_group, community):
    """Create a record and store it in the dictionary using its ID as key."""
    try:
        rec = VaccinationRecord(age_group, community)
    except ValueError as err:
        print(f"  ! Could not add record: {err}")
        return None
    records[rec.record_id] = rec
    print(f"  + Record {rec.record_id} added.")
    return rec


def display_records():
    """Loop through the dictionary and display every record."""
    if not records:
        print("  (no records yet)")
        return
    for rec in records.values():
        rec.display_info()


# --------------------------------------------------------------------------
# Demo + simple menu
# --------------------------------------------------------------------------
def run_demo():
    print("=== Vaccines ===")
    measles = Vaccine("MEASLES", "Measles", 2, (9, 15))
    polio = Vaccine("POLIO", "Polio (OPV)", 3, (2, 4, 6))
    for v in (measles, polio):
        v.display_info()
    print(f"  Total vaccines: {Vaccine.get_total_vaccines()}")

    print("\n=== Adding records ===")
    r1 = add_record("child", "Freetown East")
    r2 = add_record("adult", "Bo District")
    add_record("teenager", "Kenema")           # invalid -> handled

    print("\n=== Recording doses ===")
    r1.add_dose(measles, date(2026, 9, 10))
    r1.add_dose(measles, date(2026, 12, 10))
    r1.add_dose(measles)                        # already complete
    r2.add_dose(polio)

    print("\n=== Update a record ===")
    r2.update_record(community="Bo Town")

    print("\n=== All records ===")
    display_records()

    print("\n=== Status ===")
    print(f"  {r1.record_id} fully vaccinated for Measles? {r1.is_fully_vaccinated(measles)}")
    print(f"  {r2.record_id} fully vaccinated for Polio?   {r2.is_fully_vaccinated(polio)}")
    print(f"  Total records: {VaccinationRecord.get_record_count()}")


def run_menu():
    vaccines = {
        "MEASLES": Vaccine("MEASLES", "Measles", 2, (9, 15)),
        "POLIO": Vaccine("POLIO", "Polio (OPV)", 3, (2, 4, 6)),
    }
    while True:
        print("\n1) Add record  2) Add dose  3) Display records  4) Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_record(input("Age group (child/adult/elderly): ").strip().lower(),
                       input("Community: ").strip())
        elif choice == "2":
            rec = records.get(input("Record ID (e.g. V-0001): ").strip().upper())
            vac = vaccines.get(input("Vaccine (MEASLES/POLIO): ").strip().upper())
            if rec and vac:
                rec.add_dose(vac)
            else:
                print("  ! Record or vaccine not found.")
        elif choice == "3":
            display_records()
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("  ! Invalid choice.")


if __name__ == "__main__":
    mode = input("Run (1) demo or (2) interactive menu? ").strip()
    run_menu() if mode == "2" else run_demo()