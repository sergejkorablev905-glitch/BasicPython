import pandas as pd

# 1. Загружаем датасет
df = pd.read_csv('txt.csv/ecommerce_sales_data.csv')

# 2. Сравниваем поведение подписчиков и обычных пользователей
subscription_summary = df.groupby('subscription_status')['purchase_amount'].agg(
    count='count',
    median='median',
    iqr=lambda x: x.quantile(0.75) - x.quantile(0.25)
).round(2)

print(subscription_summary)

# Создаем возрастные категории
df['age_group'] = pd.cut(
    df['age'], bins=[18, 30, 45, 65],
    labels=['18-30', '31-45', '46-65']
)

# Строим сводную таблицу медианных чеков
subscription_by_age = df.groupby(['age_group', 'subscription_status'])['purchase_amount'].median().unstack().round(2)

print(subscription_by_age)