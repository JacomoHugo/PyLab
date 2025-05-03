import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = 'C:/Users/nakov/OneDrive/Рабочий стол/UNO/lab_1/3.csv'
df = pd.read_csv(file_path, sep=';', header=None, names=['Student', 'Group', 'Grade'])


pivot_df = df.groupby(['Group', 'Grade']).size().unstack(fill_value=0)


pivot_df.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='viridis')

plt.title('Распределение оценок по группам')
plt.xlabel('Группа')
plt.ylabel('Количество студентов')
plt.legend(title='Оценка', bbox_to_anchor=(1, 1))
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)


plt.savefig('plot.png', bbox_inches='tight')
plt.show()
