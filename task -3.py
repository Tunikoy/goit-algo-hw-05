import timeit

# Реалізація алгоритму Боєра-Мура
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    skip = {pattern[i]: m - i - 1 for i in range(m - 1)}
    skip = skip.get
    
    i = m - 1
    while i < n:
        j = m - 1
        while text[i] == pattern[j]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        i += m - min(j, 1 + skip(text[i], m))
    return -1

# Реалізація алгоритму Кнута-Морріса-Пратта (KMP)
def kmp_search(text, pattern):
    def kmp_table(pattern):
        table = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            if pattern[i] == pattern[j]:
                j += 1
                table[i] = j
            else:
                if j > 0:
                    j = table[j - 1]
                    i -= 1
        return table
    
    table = kmp_table(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == len(pattern):
                return i - j
        else:
            if j > 0:
                j = table[j - 1]
            else:
                i += 1
    return -1

# Реалізація алгоритму Рабіна-Карпа
def rabin_karp(text, pattern):
    m, n = len(pattern), len(text)
    p_hash = hash(pattern)
    for i in range(n - m + 1):
        if hash(text[i:i + m]) == p_hash and text[i:i + m] == pattern:
            return i
    return -1

# Вимірювання часу виконання з timeit
text_1 = "Текст статті 1 з файлу"
text_2 = "Текст статті 2 з файлу"
pattern_existing = "підрядок"
pattern_nonexistent = "вигаданий_підрядок"

# Використовуйте реальні дані з текстових файлів замість прикладів вище.
with open('path_to_file_1.txt', 'r', encoding='utf-8') as f:
    text_1 = f.read()

with open('path_to_file_2.txt', 'r', encoding='utf-8') as f:
    text_2 = f.read()

# Функція для вимірювання часу пошуку
def measure_time(algorithm, text, pattern):
    return timeit.timeit(lambda: algorithm(text, pattern), number=100)

# Вимірювання часу для статті 1 та статті 2
print("Boyer-Moore existing (Article 1):", measure_time(boyer_moore, text_1, pattern_existing))
print("KMP existing (Article 1):", measure_time(kmp_search, text_1, pattern_existing))
print("Rabin-Karp existing (Article 1):", measure_time(rabin_karp, text_1, pattern_existing))

print("Boyer-Moore nonexistent (Article 1):", measure_time(boyer_moore, text_1, pattern_nonexistent))
print("KMP nonexistent (Article 1):", measure_time(kmp_search, text_1, pattern_nonexistent))
print("Rabin-Karp nonexistent (Article 1):", measure_time(rabin_karp, text_1, pattern_nonexistent))

print("Boyer-Moore existing (Article 2):", measure_time(boyer_moore, text_2, pattern_existing))
print("KMP existing (Article 2):", measure_time(kmp_search, text_2, pattern_existing))
print("Rabin-Karp existing (Article 2):", measure_time(rabin_karp, text_2, pattern_existing))

print("Boyer-Moore nonexistent (Article 2):", measure_time(boyer_moore, text_2, pattern_nonexistent))
print("KMP nonexistent (Article 2):", measure_time(kmp_search, text_2, pattern_nonexistent))
print("Rabin-Karp nonexistent (Article 2):", measure_time(rabin_karp, text_2, pattern_nonexistent))
