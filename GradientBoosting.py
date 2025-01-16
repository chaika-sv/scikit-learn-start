import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load data from file
df = pd.read_csv('data/go_for_a_walk.csv')

# Create objects to encode string dataq
leWeather = LabelEncoder()
leHumidity = LabelEncoder()
leWeekday = LabelEncoder()
leGoWalk = LabelEncoder()

# Encode data
df["Weather_Code"] = leWeather.fit_transform(df["Weather"])
df["Humidity_Code"] = leHumidity.fit_transform(df["Humidity"])
df["Weekday_Code"] = leWeekday.fit_transform(df["Weekday"])
df["GoWalk_Code"] = leGoWalk.fit_transform(df["GoWalk"])


# Splitting into features and target variable
X = df[["Weather_Code", "Temperature", "Humidity_Code", "Weekday_Code"]]
y = df["GoWalk_Code"]

# Splitting into training and test datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
#clf = RandomForestClassifier(random_state=42)
clf = GradientBoostingClassifier(random_state=42)

clf.fit(X_train, y_train)

# Model evaluation
print("Accuracy:", clf.score(X_test, y_test))

# Prediction
y_pred = clf.predict(X_test)

# Convert to DataFrame
y_pred_df = pd.DataFrame(y_pred, columns=['GoWalk_Code'])

# Decode all columns
X_test_decode = pd.DataFrame({
    "Weather" : leWeather.inverse_transform(X_test["Weather_Code"]),
    "Temperature" : X_test["Temperature"],
    "Humidity" : leHumidity.inverse_transform(X_test["Humidity_Code"]),
    "Weekday" : leWeekday.inverse_transform(X_test["Weekday_Code"]),
    "GoWalk" : leGoWalk.inverse_transform(y_pred_df["GoWalk_Code"])
})

print(X_test_decode)
print("")


# Try to predict using new data
single_question = pd.DataFrame({
    "Weather_Code": [ leWeather.transform(["Дождь"])[0] ],
    "Temperature": [10],
    "Humidity_Code": [ leHumidity.transform(["Высокая"])[0] ],
    "Weekday_Code": [ leWeekday.transform(["Среда"])[0] ]
})

print("Single question:")
print(single_question)

single_prediction = clf.predict(single_question)
print("Single prediction:", leGoWalk.inverse_transform(single_prediction))







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