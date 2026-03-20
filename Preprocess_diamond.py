import pandas as pd
from sklearn.preprocessing import StandardScaler
df = pd.read_csv('diamonds.csv')
df = df.dropna()
cut_order = {'Fair': 1, 'Good': 2, 'Very Good': 3, 'Premium': 4, 'Ideal': 5}
color_order = {'J': 1, 'I': 2, 'H': 3, 'G': 4, 'F': 5, 'E': 6, 'D': 7}
clarity_order = {'I1': 1, 'SI2': 2, 'SI1': 3, 'VS2': 4, 'VS1': 5, 'VVS2': 6, 'VVS1': 7, 'IF': 8}
df['cut'] = df['cut'].map(cut_order)
df['color'] = df['color'].map(color_order)
df['clarity'] = df['clarity'].map(clarity_order)
X = df.drop('price', axis=1)
y = df['price']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_df = pd.DataFrame(X_scaled)
X_df['price'] = y.values
X_df.to_csv('diamonds_clean.csv', index=False)