import heapq

def min_cost_to_connect_cables(cables):
    # створюємо мінімальну купу
    heapq.heapify(cables)
    
    total_cost = 0
    
    # цикл, доки в купі більше одного елемента
    while len(cables) > 1:
        # знаходимо 2 найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # витрати на з'єднання двох кабелів
        cost = first + second
        
        # рахуємо загальні витрати
        total_cost += cost
        
        # поміщаємо об'єднаний кабель назад у купу
        heapq.heappush(cables, cost)
    
    return total_cost

if __name__ == "__main__":
    # приклад
    cables = [15, 4, 4, 2, 1]
    print(f"Мінімальні витрати на з'єднання кабелів: {min_cost_to_connect_cables(cables)}")
