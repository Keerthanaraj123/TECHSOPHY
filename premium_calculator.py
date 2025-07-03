
##TECHSOPHY CODING TEST

"""

import random
import numpy as np
from sklearn.linear_model import LinearRegression

class SmartPremiumEstimator:
    """
    Estimates an insurance premium based on user information
    and simulated economic fluctuation using a trained model.
    """

    def __init__(self):
        self.model = self._build_model()
        self.base_rate = 500.0  # starting rate before adjustments

    def _build_model(self):
        """
        Trains a simple linear model to evaluate user risk.
        Input features include age and previous claims.
        Output is a normalized risk factor (0 to 1).
        """
        features = np.array([
            [22, 0],
            [35, 1],
            [47, 2],
            [55, 3],
            [65, 0]
        ])
        risk_labels = np.array([0.1, 0.3, 0.6, 0.85, 0.5])

        reg = LinearRegression()
        reg.fit(features, risk_labels)
        return reg

    def _predict_risk_factor(self, client_age, claim_count):
        """
        Uses trained model to return a bounded risk factor.
        """
        user_data = np.array([[client_age, claim_count]])
        estimated_risk = self.model.predict(user_data)[0]
        return max(0.0, min(1.0, estimated_risk))  # Ensure between 0–1

    def _market_variation(self):
        """
        Introduces real-world fluctuation by randomly adjusting costs.
        """
        return random.uniform(0.92, 1.08)  # narrower range for realism

    def estimate_final_premium(self, client_age, claim_count):
        """
        Computes insurance cost using:
        base rate × (1 + predicted risk) × market variation
        """
        risk = self._predict_risk_factor(client_age, claim_count)
        market_shift = self._market_variation()
        cost = self.base_rate * (1 + risk) * market_shift
        cost = round(cost, 2)

        summary = (
            f"\n--- Premium Breakdown ---\n"
            f"Base Rate       : ${self.base_rate:.2f}\n"
            f"Risk Multiplier : {risk:.2f}\n"
            f"Market Factor   : {market_shift:.2f}\n"
            f"-----------------------------\n"
            f"Estimated Cost  : ${cost:.2f}"
        )
        return cost, summary

# Main logic
calculator = SmartPremiumEstimator()
print("Welcome to the AI-Driven Insurance Estimator")

try:
    age_input = input("Please enter your age: ").strip()
    if not age_input.isdigit():
        raise ValueError("Age must be a positive number.")
    age = int(age_input)

    if age < 18:
        print("Sorry, you must be at least 18 to apply for coverage.")
    else:
        claims_input = input("Number of claims filed in past 5 years: ").strip()
        if not claims_input.isdigit():
            raise ValueError("Claims must be a non-negative number.")
        claims = int(claims_input)

        if claims < 0:
            print("Claims count can't be negative.")
        else:
            premium, details = calculator.estimate_final_premium(age, claims)
            print(details)

except ValueError as ve:
    print(f"[Input Error] {ve}")
except Exception as ex:
    print(f"[Unexpected Error] {ex}")

# Main logic
calculator = SmartPremiumEstimator()
print("Welcome to the AI-Driven Insurance Estimator")

try:
    age_input = input("Please enter your age: ").strip()
    if not age_input.isdigit():
        raise ValueError("Age must be a positive number.")
    age = int(age_input)

    if age < 18:
        print("Sorry, you must be at least 18 to apply for coverage.")
    else:
        claims_input = input("Number of claims filed in past 5 years: ").strip()
        if not claims_input.isdigit():
            raise ValueError("Claims must be a non-negative number.")
        claims = int(claims_input)

        if claims < 0:
            print("Claims count can't be negative.")
        else:
            premium, details = calculator.estimate_final_premium(age, claims)
            print(details)

except ValueError as ve:
    print(f"[Input Error] {ve}")
except Exception as ex:
    print(f"[Unexpected Error] {ex}")

