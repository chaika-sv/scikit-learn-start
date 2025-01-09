from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
import graphviz

# Загрузка данных
data = load_iris()
X, y = data.data, data.target

# Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# Обучение Random Forest
clf = RandomForestClassifier(n_estimators=10, random_state=42)
clf.fit(X, y)

# Экспорт одного дерева из случайного леса
estimator = clf.estimators_[0]  # Берём первое дерево

# Визуализация дерева
dot_data = export_graphviz(
    estimator,
    out_file=None,
    feature_names=data.feature_names,
    class_names=data.target_names,
    filled=True,
    rounded=True,
    special_characters=True
)

# Отображение дерева
graph = graphviz.Source(dot_data)
#graph.view("decision_tree")  # Откроется в графическом просмотрщике

# Предсказание
y_pred = clf.predict(X_test)

# Оценка точности
print("Accuracy:", accuracy_score(y_test, y_pred))
