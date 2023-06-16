import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import customException
from src.logger import logging
import os

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts',"preprcessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()


    def get_data_transformer_object(self):
        '''
        This function is for data trnasformation
        '''

        try:
            numerical_columns = ['writing_score','reading_score']
            categorical_columns = ['gender','lunch','race_ethnicity','parental_level_of_education','test_preparation_course']
                                                                                                    
            num_pipeline = Pipeline(steps=[
                ("imputer",SimpleImputer(strategy="mean")),
                ("scaler",StandardScaler())
            ])


            cat_pipeline = Pipeline(steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("onehotencoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
            ])


            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")


            preprocessor = ColumnTransformer([
                ("num_pipeline", num_pipeline, numerical_columns),
                ("cat_pipeline", cat_pipeline, categorical_columns)
            ])


            return preprocessor


        except Exception as e:
            raise customException(e,sys)


    def initiate_data_transformation(self,train_path,test_path):


        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)


            logging.info("Read train and test data completed")
            logging.info("Obtaining preprocessing object")


            preprocesser_obj = self.get_data_transformer_object()


            target_column = "math_score"
            numerical_columns = ["reading_score","writing_score"]


            input_feature_train_df = train_df.drop(target_column,axis=1)
            target_feature_train_df = train_df[target_column]


            input_feature_test_df = test_df.drop(target_column,axis=1)
            target_feature_test_df = test_df[target_column]


            logging.info(f"Applying preprocessing object on training dataframe and testing dataframe.")


            input_feature_train_arr = preprocesser_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocesser_obj.fit_transform(input_feature_test_df)


            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]


            logging.info(f"Saved preprocessing object.")


            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj= preprocesser_obj
            )


            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )


        except Exception as e:
            raise customException(e,sys)
        

