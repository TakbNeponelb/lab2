def f(x):
    return 5.9 * x**3 + 22 * x**2 - 8 * x - 1

def df(x):
    return 17.7 * x**2 + 44 * x - 8

def g(x, a):
    return x - a * f(x)  # функция для метода простой итерации с оптимальным параметром a

m = [df(-3.5), df(-1), df(0.1)]
M = [df(-4), df(-0.1), df(1)]
a = [2 / (M[i] + m[i]) for i in range(3)]  # Вычисляем оптимальные параметры a
def simple_iteration_method(guess, tolerance, a, M, m):
    q = abs(M-m)/abs(M+m) #в каждом случае вычисляем q(a_опт) для выхода из МПИ
    x = guess
    iteration = 1
    while True:
        x1 = g(x, a)
        print(f"Итерация {iteration}: x = {x1}, апостериорная оценка погрешности: {abs(x1-x)}")
        if abs(x1 - x) < (1-q)/q*tolerance:
            return x1, iteration  # Возвращаем найденный корень и количество итераций
        x = x1
        iteration += 1

# Запуск метода простой итерации для каждого интервала локализации
tolerance = 1e-13
guesses = [-3.75, -0.55, 0.55]
for i in range(3):
    root, iterations = simple_iteration_method(guesses[i], tolerance, a[i], M[i], m[i])
    print(f"Корень уравнения на интервале {i+1}: {root} (достигнут на итерации {iterations})")
