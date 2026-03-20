import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
df = pd.read_csv('Titanic-Dataset.csv')
df = df.drop(['Name', 'Ticket', 'Cabin'], axis=1)
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Fare'] = df['Fare'].fillna(df['Fare'].median())  
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df = df.drop(['SibSp', 'Parch'], axis=1)
X = df.drop('Survived', axis=1)
y = df['Survived']
num_features = ['Age', 'Fare', 'FamilySize']  
cat_features = ['Sex', 'Embarked', 'Pclass']
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), num_features),
    ('cat', OneHotEncoder(drop='first', sparse_output=False), cat_features)  
])
X_processed = preprocessor.fit_transform(X)
feature_names = (num_features + 
                 list(preprocessor.named_transformers_['cat'].get_feature_names_out(cat_features)))
X_df = pd.DataFrame(X_processed, columns=feature_names)
X_df['Survived'] = y.values
X_df.to_csv('titanic_clean.csv', index=False)