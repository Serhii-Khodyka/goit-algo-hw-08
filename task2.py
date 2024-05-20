import heapq

def merge_k_lists(lists):
    min_heap = []
    
    # поміщаємо перший елемент кожного списку у купу разом з індексом списку і індексом елемента
    for i, lst in enumerate(lists):
        if lst:  # якщо список не порожній
            heapq.heappush(min_heap, (lst[0], i, 0))
    
    result = []
    
    while min_heap:
        value, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(value)
        
        # якщо є наступний елемент в тому ж списку, додаємо його в купу
        if element_idx + 1 < len(lists[list_idx]):
            next_element = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_element, list_idx, element_idx + 1))
    
    return result

if __name__ == "__main__":
    # приклад
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)
