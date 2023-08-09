# Importing libraries required
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

import seaborn as sns # Data visualization
import matplotlib.pyplot as plt # Data visualization

# Data analysis and ML Library
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.linear_model import Lasso # Lasso regression
from sklearn.feature_selection import mutual_info_classif
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression # Logistic regression
from sklearn.svm import SVC # Support vector machine classifier
from sklearn.tree import DecisionTreeClassifier # Decision tree classifier
from sklearn.ensemble import RandomForestClassifier # Random forest classifier
from sklearn.naive_bayes import GaussianNB # Gaussian Naive Bayes
from sklearn.neighbors import KNeighborsClassifier# K Nearset Neighbors
from sklearn.model_selection import GridSearchCV,RandomizedSearchCV,RepeatedStratifiedKFold
from sklearn.metrics import accuracy_score,precision_score,recall_score,roc_auc_score,f1_score,log_loss,roc_curve,classification_report, confusion_matrix

# Handle Imbalanced dataset
from imblearn.over_sampling import SMOTE

# Print html elements
from IPython.display import Markdown

# Ignore warning messages
import warnings
warnings.filterwarnings('ignore')

#To make working with geospatial data in python easier
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame

plt.style.use('ggplot')
