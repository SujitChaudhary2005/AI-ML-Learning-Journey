import pandas as pd

def preprocess_titanic(path):
    """
    Preprocess Titanic dataset:
    - Handles missing values
    - Removes duplicates
    - Creates new features
    - Filters unrealistic ages
    """

    # Load data
    df = pd.read_csv(path)

    # Handle missing values
    df['Cabin'] = df['Cabin'].fillna("Unknown")
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Convert Pclass to category
    df['Pclass'] = df['Pclass'].astype('category')

    # Create FamilySize feature
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

    # Extract Title from Name
    df['Title'] = df['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)

    # Create AgeGroup
    df['AgeGroup'] = pd.cut(df['Age'],
                            bins=[0, 12, 18, 35, 60, 100],
                            labels=['Child', 'Teen', 'Adult', 'MiddleAge', 'Senior'])

    # Remove unrealistic ages
    df = df[df['Age'] <= 80]

    return df