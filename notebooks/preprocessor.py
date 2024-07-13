import numpy as np
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

class Preprocessor:
    def __init__(self, data):
        self.df = pd.DataFrame(data)
        
    def encoder(self):
        self.df.replace(['Male', 'Female'], [0, 1], inplace=True)
    
    def drop_cols(self):
        self.df.drop('CustomerID', axis=1, inplace=True)  
        
    def scaler (self , x):
        scaler = MinMaxScaler()
        self.df[[x]] = scaler.fit_transform(self.df[[x]])
    
    def transform(self):
        self.encoder()
        self.drop_cols()
        scale_cols=['Age','Annual Income (k$)','Spending Score (1-100)','Gender']
        for col in scale_cols:
            self.scaler(col)
        return self.df

