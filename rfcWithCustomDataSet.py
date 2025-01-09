import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# 1. Загрузка пользовательского набора данных
# Замените 'your_dataset.csv' на путь к вашему файлу
data = pd.read_csv('data/your_dataset.csv')

# 2. Разделение данных на признаки (X) и целевую переменную (y)
# Предположим, что целевой столбец называется 'target'
X = data.drop(columns=['target'])  # Все столбцы, кроме целевого
y = data['target']  # Целевой столбец

# 3. Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Обучение модели RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# 5. Предсказания и оценка модели
y_pred = clf.predict(X_test)

# Вывод точности
print("Accuracy:", accuracy_score(y_test, y_pred))

# Подробный отчёт о классификации
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 6. Важность признаков
feature_importances = pd.DataFrame({
    'Feature': X.columns,
    'Importance': clf.feature_importances_
}).sort_values(by='Importance', ascending=False)

print("\nFeature Importances:\n", feature_importances)