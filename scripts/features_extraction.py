import pandas as pd

# feature extraction function
def extract_features(name):
    # convert name to lowercase
    df_input = pd.DataFrame({'Name': [name]})
    
    # extract features
    df_input['first_letter'] = df_input['Name'].str[0].str.lower()
    df_input['last_letter'] = df_input['Name'].str[-1].str.lower()
    df_input['name_length'] = df_input['Name'].apply(len)
    
    # return features that will be used by the model
    return df_input[['first_letter', 'last_letter', 'name_length']]
