from typing import List, Tuple
from collections import Counter
import math


def suma(a: float, b: float) -> float:
	return a + b


def resta(a: float, b: float) -> float:
	return a - b


def multiplicacion(a: float, b: float) -> float:
	return a * b


def division(a: float, b: float) -> float:
	if b == 0:
		raise ValueError("No se puede dividir entre cero")
	return a / b


def potencia(a: float, b: float) -> float:
	return a ** b


def raiz(x: float) -> float:
	if x < 0:
		raise ValueError("No se puede sacar raíz de un número negativo")
	return math.sqrt(x)


def modulo(a: int, b: int) -> int:
	return a % b


def funcion_piso(a: int, b: int) -> int:
	return a // b


def incremento(x: float, step: float = 1.0) -> float:
	return x + step


def decremento(x: float, step: float = 1.0) -> float:
	return x - step


def es_par(n: int) -> bool:
	return n % 2 == 0


def es_impar(n: int) -> bool:
	return n % 2 != 0


def max_de_dos(a: float, b: float) -> float:
	return a if a >= b else b


def min_de_dos(a: float, b: float) -> float:
	return a if a <= b else b


def promedio_de_dos(a: float, b: float) -> float:
	return (a + b) / 2


def promedio_lista(values: List[float]) -> float:
	if not values:
		raise ValueError("La lista está vacía")
	return sum(values) / len(values)


def lista_suma(values: List[float]) -> float:
	return sum(values)


def lista_producto(values: List[float]) -> float:
	resultado = 1
	for v in values:
		resultado *= v
	return resultado


def factorial(n: int) -> int:
	if n < 0:
		raise ValueError("El factorial no está definido para negativos")
	resultado = 1
	for i in range(2, n + 1):
		resultado *= i
	return resultado


def porcentaje(part: float, whole: float) -> float:
	if whole == 0:
		raise ValueError("El total no puede ser cero")
	return part / whole * 100


def es_primo(n: int) -> bool:
	if n < 2:
		return False
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True


def fibonacci(n: int) -> int:
	a, b = 0, 1
	for _ in range(n):
		a, b = b, a + b
	return a


# ---------- Nuevas funciones de la tarea ----------

def moda(values: List[float]) -> List[float]:
	"""Regresa la moda de una lista de números.

	Se regresa siempre una lista ordenada, porque puede haber más de una
	moda (por ejemplo, [1, 1, 2, 2] tiene dos modas: 1 y 2).
	"""
	if not values:
		raise ValueError("La lista está vacía")
	conteo = Counter(values)
	maxima_frecuencia = max(conteo.values())
	return sorted(v for v, f in conteo.items() if f == maxima_frecuencia)


def volumen_paralelepipedo(largo: float, ancho: float, alto: float) -> float:
	"""Volumen de un paralelepípedo rectangular: largo x ancho x alto."""
	if largo <= 0 or ancho <= 0 or alto <= 0:
		raise ValueError("Las dimensiones deben ser mayores que cero")
	return largo * ancho * alto

