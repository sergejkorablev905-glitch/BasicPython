import pandas as pd
import numpy as np


def generate_dataset(filename: str = 'Название файла.csv') -> None:
    """
    Генерирует датасет по описательной статистике
    и сохраняет его в CSV.
    """
    np.random.seed(42)  # Фиксируем seed для одинакового результата у всех
    n = 1000  # Размер датасета

    # 1. Генерация статуса подписки (30% с подпиской)
    subscription_status = np.random.choice([True, False], size=n, p=[0.3, 0.7])

    # 2. Генерация базовых сумм покупок
    base_amounts = np.random.lognormal(mean=7.5, sigma=0.8, size=n)

    # 3. Применяем коэффициент для подписчиков (они тратят в 1.5 раза больше)
    purchase_amount = np.where(subscription_status, base_amounts * 1.5, base_amounts)

    # 4. Внедряем 5 жестких выбросов для демонстрации искажения среднего значения
    outlier_indices = np.random.choice(n, 5, replace=False)
    purchase_amount[outlier_indices] = [150000.0, 200000.0, 250000.0, 300000.0, 500000.0]

    # 5. Собираем итоговый датафрейм
    df = pd.DataFrame({
        'user_id': range(1, n + 1),
        'group': np.random.choice(['A', 'B'], size=n),
        'age': np.random.randint(18, 65, size=n),
        'subscription_status': subscription_status,
        'purchase_amount': np.round(purchase_amount, 2)
    })

    # Перемешиваем строки, чтобы выбросы не были в самом конце
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    # Исправляем user_id после перемешивания, чтобы они шли по порядку
    df['user_id'] = range(1, n + 1)

    # Сохраняем в CSV
    df.to_csv(filename, index=False)


if __name__ == '__main__':
    generate_dataset()
