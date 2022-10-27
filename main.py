#Работа Дорофеева Сергея 20-кис-1

print("Введите число Фибоначи")

n = int(input())

def formulaFib(n):
	root_5 = 5**0.5
	phi = ((1 + root_5)/2)

	a = ((phi**n)-((-phi)** -n))/ root_5

	return round(a)

print(formulaFib(n))