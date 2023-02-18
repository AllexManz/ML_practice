import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder


# Creating DataFrame
bridge_types = ('Arch', 'Beam', 'Truss', 'Cantilever', 'Tied Arch', 'Suspension', 'Cable')
bridge_df = pd.DataFrame(bridge_types, columns=['Bridge_Types'])
bridge_data_frame = pd.DataFrame(bridge_types, columns=['Bridge_Types'])

# Converting type of columns to 'category'
bridge_df['Bridge_Types'] = bridge_df['Bridge_Types'].astype('category')

# ENCODING Values using Label Encoding
bridge_df['Bridge_Types_Cat'] = bridge_df['Bridge_Types'].cat.codes
print(bridge_df, end='\n\n')


# creating instance of label encoder and assigning numerical values
label_encoder = LabelEncoder()

# ENCODING Values using Label Encoding created by skit-learn
bridge_data_frame['Bridge_Types_Cat'] = label_encoder.fit_transform(bridge_data_frame['Bridge_Types'])
print(bridge_data_frame, end='\n\n')

# creating instance of OneHotEncoder
encoder = OneHotEncoder(handle_unknown='ignore')

# ENCODING values using
encoded_df = pd.DataFrame(encoder.fit_transform(bridge_df[['Bridge_Types']]).toarray())
all_df = bridge_df.join(encoded_df)
print(all_df)
