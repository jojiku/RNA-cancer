import pandas as pd
import numpy as np

credit = pd.read_csv('C:\\Users\\Tseh\\Desktop\\Диплом\\Данные по долгам\\Соревнование по кредитным историям\\data_for_competition\\train_target_balanced.csv') 
target_variable = credit['flag']
id_variable = credit['id']
credit.drop(['flag', 'id'], axis=1, inplace=True)
credit = pd.get_dummies(credit, columns=credit.columns, sparse=True)
credit = credit.sparse.to_dense()
credit.replace({True: 1, False: 0}, inplace=True) # add this line to replace True with 1 and False with 0
credit['flag'] = target_variable
credit.insert(loc=0, column='id', value=id_variable)
credit.to_csv('C:\\Users\\Tseh\\Desktop\\Диплом\\Данные по долгам\\Соревнование по кредитным историям\\data_for_competition\\dumb.csv', index=False)