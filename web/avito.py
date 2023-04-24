import pandas as pd
import joblib
import json
import sys
from sklearn.metrics import accuracy_score, log_loss, confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split, cross_validate, cross_val_score, cross_val_predict
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier

params_json = sys.argv[1]
params = json.loads(params_json)

clf = joblib.load('avito-'+params['model'][0]+'.pkl')

new_data = pd.DataFrame({'score': [params['score'][0]],
                         'category_id': [params['category_id'][0]],
                         'has_diff_location': [params['has_diff_location'][0]],
                         'uncounted': [params['uncounted'][0]],
                         'count_procent': [params['count_procent'][0]],
                         'bad_item': [params['bad_item'][0]]})

prediction = clf.predict(new_data)
model_name = clf.__class__.__name__

if prediction == 1:
    print(model_name,": Подозрительный профиль")
else:
    print(model_name,": Профиль не вызывает подозрений")