def find_min_max(arr, low, high):
    # Базовий випадок: якщо масив містить лише один елемент
    if low == high:
        return arr[low], arr[low]
    
    # Якщо масив містить два елементи
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    
    # Розділяємо масив на дві частини
    mid = (low + high) // 2
    
    # Рекурсивно знаходимо мінімум і максимум для лівої і правої частини
    left_min, left_max = find_min_max(arr, low, mid)
    right_min, right_max = find_min_max(arr, mid + 1, high)
    
    # Повертаємо мінімум і максимум з двох частин
    return min(left_min, right_min), max(left_max, right_max)

# Основна функція для знаходження мінімуму і максимуму в масиві
def find_min_max_in_array(arr):
    # Перевірка, чи не порожній масив
    if not arr:
        raise ValueError("Масив не може бути порожнім")
    
    # Викликаємо рекурсивну функцію для знаходження мінімуму і максимуму
    return find_min_max(arr, 0, len(arr) - 1)

# Приклад використання:
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_element, max_element = find_min_max_in_array(arr)

print(f"Мінімальний елемент: {min_element}")
print(f"Максимальний елемент: {max_element}")
