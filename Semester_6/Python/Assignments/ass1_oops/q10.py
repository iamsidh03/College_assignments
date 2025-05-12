class CommissionEmployee:
    def __init__(self, name, emp_id, sales, commission_rate):
        self.name = name
        self.emp_id = emp_id
        self.sales = sales              # triggers setter
        self.commission_rate = commission_rate  # triggers setter

    # Property for sales with validation
    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, value):
        if value < 0:
            raise ValueError("Sales amount cannot be negative.")
        self._sales = value

    # Property for commission_rate with validation
    @property
    def commission_rate(self):
        return self._commission_rate

    @commission_rate.setter
    def commission_rate(self, value):
        if value < 0:
            raise ValueError("Commission rate cannot be negative.")
        self._commission_rate = value

    # Method to calculate earnings
    def earnings(self):
        return self.sales * self.commission_rate

    # String representation of the object
    def __repr__(self):
        return f"CommissionEmployee(name='{self.name}', emp_id={self.emp_id}, sales={self.sales}, rate={self.commission_rate})"

# Test the CommissionEmployee class
try:
    emp = CommissionEmployee("Alice", 101, 5000, 0.1)
    print(emp)                          # Show object details
    print("Earnings:", emp.earnings())  # Calculate earnings

    emp.sales = 7000                    # Modify sales
    print("Updated earnings:", emp.earnings())

    emp.sales = -2000                   # Try setting negative sales
except ValueError as e:
    print("Error:", e)
