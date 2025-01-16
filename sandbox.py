import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Загрузка данных
df = pd.read_csv('data/go_for_a_walk.csv')

# Кодирование категориальных признаков
le1 = LabelEncoder()
le2 = LabelEncoder()

df["Погода_код"] = le1.fit_transform(df["Погода"])
df["Влажность_код"] = le2.fit_transform(df["Влажность"])

print(df["Погода_код"])
print(df["Влажность_код"])

a = le1.inverse_transform(df["Погода_код"])
b = le2.inverse_transform(df["Влажность_код"])

print(a)
print(b)

# # Разделение на признаки и целевую переменную
# X = df[["Погода_код", "Температура", "Влажность_код", "ДеньНедели_код"]]
# y = df["ИдтиГулять_код"]
#
# # Разделение на обучающую и тестовую выборки
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# # Обучение модели
# clf = RandomForestClassifier(random_state=42)
# clf.fit(X_train, y_train)
#
# # Оценка модели
# #print("Точность:", clf.score(X_test, y_test))
#
# print(df["Погода"])
# print(df["Погода_код"])

#a = le.inverse_transform(df["Погода_код"])


# predictions = clf.predict(X_test)
#
# X_test["Погода"] = le.inverse_transform(df["Погода_код"])
#
# print(X_test)
# print("Предсказания:", predictions)




# # Предсказание на новых данных
# new_data = pd.DataFrame({
#     "Погода": [0],
#     "Температура": [40],
#     "Влажность": [2],
#     "День недели": [1]
# })
#
# print(new_data)
# single_prediction = clf.predict(new_data)  # Пример одного наблюдения
# df["Погода"] = le.inverse_transform(df["Погода"])
# print("Предсказание:", single_prediction)







# 4. Обучение модели RandomForestClassifier
# clf = GradientBoostingClassifier(n_estimators=100, random_state=42)
# clf.fit(X_train, y_train)

# 5. Предсказания и оценка модели
# y_pred = clf.predict(X_test)
#
# # Вывод точности
# print("Accuracy:", accuracy_score(y_test, y_pred))
#
# # Подробный отчёт о классификации
# print("\nClassification Report:\n", classification_report(y_test, y_pred))
#
# # 6. Важность признаков
# feature_importances = pd.DataFrame({
#     'Feature': X.columns,
#     'Importance': clf.feature_importances_
# }).sort_values(by='Importance', ascending=False)
#
# print("\nFeature Importances:\n", feature_importances)