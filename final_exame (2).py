class Family:
    """Represents a registered family with an ID, name, and member count."""
    def __init__(self, family_id, name, members):
        self.family_id = family_id
        self.name = name
        self.members = members

    def __str__(self):
        return f"{self.family_id} - {self.name} - {self.members} members"


class FoodBank:
    """Manages food stock, family registrations, and distribution history."""
    def __init__(self):
        self.available_packs = 0
        self.total_distributed = 0
        
        # Data structures utilization:
        self.families_dict = {}       # dict: family_id -> Family object (for fast lookup)
        self.family_ids_set = set()   # set: unique family IDs (for quick duplicate checking)
        self.distribution_history = []# list: stores distribution events
        # Note: tuples will be used dynamically to record each distribution record.

    def register_family(self):
        print("\n--- Register Family ---")
        family_id = input("Family ID: ").strip()
        if not family_id:
            print("Error: Family ID cannot be empty.")
            return

        # Check for duplicate using set
        if family_id in self.family_ids_set:
            print(f"Error: Family ID '{family_id}' is already registered.")
            return

        name = input("Family Name: ").strip()
        if not name:
            print("Error: Family Name cannot be empty.")
            return

        try:
            members = int(input("Number of Members: "))
            if members <= 0:
                print("Error: Number of members must be greater than 0.")
                return
        except ValueError:
            print("Error: Please enter a valid numeric value for members.")
            return

        # Create Family instance and store in data structures
        new_family = Family(family_id, name, members)
        self.families_dict[family_id] = new_family
        self.family_ids_set.add(family_id)
        print("✓ Family registered!")

    def add_food_packs(self):
        print("\n--- Add Food Packs ---")
        try:
            packs = int(input("Packs to add: "))
            if packs <= 0:
                print("Error: Must add a positive number of food packs.")
                return
            self.available_packs += packs
            print(f"Current stock: {self.available_packs}")
        except ValueError:
            print("Error: Please enter a valid numeric value for packs.")

    def distribute_food_packs(self):
        print("\n--- Distribute Food Packs ---")
        family_id = input("Family ID: ").strip()

        # Check if family exists using set/dict
        if family_id not in self.family_ids_set:
            print("Error: Unknown family ID. Please register first.")
            return

        try:
            requested = int(input("Packs requested: "))
            if requested <= 0:
                print("Error: Request quantity must be positive.")
                return
            
            # Check stock availability
            if requested > self.available_packs:
                print(f"Not enough food! Remaining stock: {self.available_packs}")
                return

            # Update stock and distribution totals
            self.available_packs -= requested
            self.total_distributed += requested

            # Store distribution record as a tuple inside the list
            record = (family_id, requested)
            self.distribution_history.append(record)

            print(f"Success! Remaining stock: {self.available_packs}")
        except ValueError:
            print("Error: Please enter a valid numeric value for requested packs.")

    def show_report(self):
        print("\n===== FOOD BANK REPORT =====")
        print(f"Available Packs: {self.available_packs}")
        
        print("\nRegistered Families:")
        if not self.families_dict:
            print("No families registered yet.")
        else:
            for fam in self.families_dict.values():
                print(fam)

       