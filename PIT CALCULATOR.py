class IncomeSource:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class Deduction:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class Employee:
    def __init__(self, name, position, organization, income_sources=None, deductions=None):
        self.name = name
        self.position = position
        self.organization = organization
        self.income_sources = income_sources if income_sources else []
        self.deductions = deductions if deductions else []

    def calculate_taxable_income(self):
        taxable_income = sum(source.amount for source in self.income_sources)
        for deduction in self.deductions:
            taxable_income -= deduction.amount
        return max(0, taxable_income)


class TaxCalculator:
    TAX_SLABS = [
        (300000, 0.0),
        (400000, 0.10),
        (650000, 0.15),
        (1000000, 0.20),
        (1500000, 0.25),
        (float('inf'), 0.30)
    ]
    SURCHARGE_THRESHOLD = 1000000
    SURCHARGE_RATE = 0.10

    @staticmethod
    def calculate_tax_amount(taxable_income):
        tax_amount = 0
        for slab, rate in TaxCalculator.TAX_SLABS:
            if taxable_income <= 0:
                break
            if taxable_income > slab:
                tax_amount += slab * rate
                taxable_income -= slab
            else:
                tax_amount += taxable_income * rate
                break

        if tax_amount >= TaxCalculator.SURCHARGE_THRESHOLD:
            tax_amount += TaxCalculator.SURCHARGE_RATE * tax_amount

        return tax_amount


# Example usage
try:
    sonam_income_sources = [IncomeSource("Basic Salary", 800000), IncomeSource("Bonus", 20000)]
    sonam_deductions = [Deduction("PF Contribution", 0.10 * 800000)]
    sonam = Employee("Sonam", "Regular", "Private", sonam_income_sources, sonam_deductions)

    taxable_income = sonam.calculate_taxable_income()
    tax_amount = TaxCalculator.calculate_tax_amount(taxable_income)
    print(f"Tax amount for {sonam.name}: Nu. {tax_amount:.2f}")
except Exception as e:
    print("An error occurred:", str(e))
