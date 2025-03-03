import pandas as pd
# reading the data from the file
df= pd.read_csv("D:/File Pack/Courses/10Acadamey/Week 3/Technical Content/alpha-insurance-analysis/data/Insurance_data.csv", low_memory=False)

# Drop Columns (too many missing values), column has over 80-90% missing values, it's often best to remove it.
df.drop(columns=['CustomValueEstimate', 'WrittenOff', 'Rebuilt', 'Converted', 'CrossBorder', 'NumberOfVehiclesInFleet'], inplace=True)

# Handling Missing Data
df.fillna(df.mean(), inplace=True)

# Feature Engineering
df['PremiumToClaimRatio'] = df['TotalPremium'] / (df['TotalClaims'] + 1)

#Encoding Categorical Data
df = pd.get_dummies(df, columns=['Gender', 'Province'], drop_first=True)
# Splitting Data
from sklearn.model_selection import train_test_split
X = df.drop(['TotalClaims'], axis=1)
y = df['TotalClaims']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)