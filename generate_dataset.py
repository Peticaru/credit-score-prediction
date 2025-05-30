import pandas as pd
import numpy as np

#git repo git repo: https://github.com/Peticaru/credit-score-prediction


def generate_credit_score_dataset(num_samples=1000):
    # np.random.seed(42)  # For reproducibility
    age = np.random.randint(18, 71, num_samples)           
    dependents = np.random.randint(0, 6, num_samples)     
    period = np.random.choice([12, 24, 36, 48, 60], num_samples)

    
    income = np.random.normal(20000, 150000, num_samples)        
    loan_amount = np.random.normal(1000, 50000, num_samples)      
    current_balance = np.random.normal(0, 25000, num_samples)    
    previous_balance = np.random.normal(0, 30000, num_samples)  

    credit_history = np.random.choice(['Good', 'Bad', 'Average'], num_samples)
    marital_status = np.random.choice(['Single', 'Married', 'Divorced'], num_samples)

    credit_score = np.zeros(num_samples, dtype=int)
    score = 300
    score += (income / 150000) * 300
    score += (loan_amount/ 50000) * 100
    score -= (period / 60) * 70
    score += (4 - dependents) * 30
    score += np.where(credit_history == "Good", 40, np.where(credit_history == "Average", 30, -20))
    score += np.where(marital_status == "Married", 30, np.where(marital_status == "Single", 10, -10))
    score = np.clip(score, 300, 850)  # Ensure scores are within the range of 300 to 850
    credit_score = score.astype(int)

    df = pd.DataFrame({
        "Age": age,
        "Dependents": dependents,
        "Income": income,

        "LoanAmount": loan_amount,
        "CurrentBalance": current_balance,
        "PreviousBalance": previous_balance,
        "CreditHistory": credit_history,
        "MaritalStatus": marital_status,
        "Period": period,
        "CreditScore": credit_score
    })

    for col in df.columns:
        if col == "CreditScore":
            continue
        nan_indices = np.random.choice(num_samples, size=int(np.random.uniform(0.05, 0.2) * num_samples), replace=False)
        for idx in nan_indices:
            df[col][idx] = np.nan

    return df

# Generate and save the dataset
dataset = generate_credit_score_dataset()
dataset.to_csv("./date/credit_score_dataset.csv", index=False)
print("Dataset generated and saved as 'credit_score_dataset.csv'")