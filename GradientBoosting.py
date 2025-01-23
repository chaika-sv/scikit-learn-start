import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, f1_score
import matplotlib.pyplot as plt

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
rf_clf = RandomForestClassifier(random_state=42)
gb_clf = GradientBoostingClassifier(random_state=42)

rf_clf.fit(X_train, y_train)
gb_clf.fit(X_train, y_train)


# Prediction
rf_prediction = rf_clf.predict(X_test)
gb_prediction = gb_clf.predict(X_test)


# Convert to DataFrame
rf_pred_df = pd.DataFrame(rf_prediction, columns=['GoWalk_Code_RF'])
gb_pred_df = pd.DataFrame(gb_prediction, columns=['GoWalk_Code_GB'])

# Decode all columns
X_test_decode = pd.DataFrame({
    "Weather" : leWeather.inverse_transform(X_test["Weather_Code"]),
    "Temperature" : X_test["Temperature"],
    "Humidity" : leHumidity.inverse_transform(X_test["Humidity_Code"]),
    "Weekday" : leWeekday.inverse_transform(X_test["Weekday_Code"]),
    "GoWalk RF" : leGoWalk.inverse_transform(rf_pred_df["GoWalk_Code_RF"]),
    "GoWalk GB" : leGoWalk.inverse_transform(gb_pred_df["GoWalk_Code_GB"])
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

single_prediction_gb = gb_clf.predict(single_question)
print("Single prediction GB:", leGoWalk.inverse_transform(single_prediction_gb))

single_prediction_rf = rf_clf.predict(single_question)
print("Single prediction RB:", leGoWalk.inverse_transform(single_prediction_rf))



print("------------------------------------")

print("Random Forest:")
print("Accuracy:", accuracy_score(y_test, rf_prediction))
print("F1 Score:", f1_score(y_test, rf_prediction, average='weighted'))

print("\nGradient Boosting:")
print("Accuracy:", accuracy_score(y_test, gb_prediction))
print("F1 Score:", f1_score(y_test, gb_prediction, average='weighted'))


rf_importances = rf_clf.feature_importances_
gb_importances = gb_clf.feature_importances_

print("Random Forest Feature Importances:", rf_importances)
print("Gradient Boosting Feature Importances:", gb_importances)

feature_names = [f"Feature {i}" for i in range(X.shape[1])]

plt.barh(feature_names, rf_importances)
plt.xlabel("Importances")
plt.ylabel("Features")
plt.title("Random Forest Feature Importances")
plt.show()

plt.barh(feature_names, gb_importances)
plt.xlabel("Importances")
plt.ylabel("Features")
plt.title("Gradient Boosting Feature Importances")
plt.show()




# # Вывод точности
# print("Accuracy:", accuracy_score(y_test, y_pred))

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