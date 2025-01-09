import pandas as pd

# Создание примера набора данных
data = {
    "feature1": [5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9],
    "feature2": [3.5, 3.0, 3.2, 3.1, 3.6, 3.9, 3.4, 3.4, 2.9, 3.1],
    "feature3": [1.4, 1.4, 1.3, 1.5, 1.4, 1.7, 1.4, 1.5, 1.4, 1.5],
    "feature4": [0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0.3, 0.2, 0.2, 0.1],
    "target": ["Class1", "Class1", "Class1", "Class1", "Class1", "Class2", "Class2", "Class2", "Class2", "Class2"]
}

# Создание DataFrame
example_df = pd.DataFrame(data)

# Сохранение в CSV файл
file_path = "data/your_dataset.csv"
example_df.to_csv(file_path, index=False)

file_path
