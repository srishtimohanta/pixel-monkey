"""Financial calculations and advice"""

class FinancialAdvisor:
    @staticmethod
    def calculate_savings_rate(income: float, expenses: float) -> float:
        """Calculate savings rate as a percentage of income."""
        if income <= 0:
            return 0.0
        return ((income - expenses) / income) * 100
    
    @staticmethod
    def calculate_debt_ratio(debt: float, income: float) -> float:
        """Calculate debt-to-income ratio as a percentage."""
        if income <= 0:
            return 0.0
        return (debt / income) * 100
    
    @staticmethod
    def calculate_monthly_savings(income: float, expenses: float) -> float:
        """Calculate monthly savings amount."""
        return max(0, income - expenses)
    
    @staticmethod
    def get_budget_advice(income: float, expenses: float) -> str:
        """Provide personalized budget advice based on savings rate."""
        savings_rate = FinancialAdvisor.calculate_savings_rate(income, expenses)
        
        if savings_rate >= 20:
            return "Excellent! You're saving above the recommended 20%."
        elif savings_rate >= 10:
            return "Good job! Try to increase savings to 20% if possible."
        else:
            return "Consider reducing expenses to save at least 10% of income."
