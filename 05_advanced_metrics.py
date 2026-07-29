# 1. Твой ИТ-список сделок ( Array / List )
trades = [615, -10, 150, -10, -10, 300, -10, 450, -10, -10]

# 2. Фильтруем отдельно плюсы и отдельно минусы
wins = [t for t in trades if t > 0]
losses = [t for t in trades if t < 0]

# 3. ИТ-магия: считаем среднее значение ( Сумма деленная на Количество )
avg_win = round(sum(wins) / len(wins), 2) if len(wins) > 0 else 0
avg_loss = round(sum(losses) / len(losses), 2) if len(losses) > 0 else 0

# 4. Высчитываем реальное соотношение риск/прибыль твоей системы
risk_reward_ratio = round(avg_win / abs(avg_loss), 2) if avg_loss != 0 else 0

# 5. Выводим официальный FinTech-отчет на экран
print("📊 [ADVANCED PERFORMANCE METRICS]:")
print("-" * 50)
print(f"💰 Средний профит с успешной сделки: ${avg_win}")
print(f"📉 Средний убыток со сделки: ${avg_loss}")
print(f"⚖️ Реальное соотношение Риск/Прибыль: 1 к {risk_reward_ratio}")
print("-" * 50)
 
