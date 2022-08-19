# Домашнее задание Урок№ 11
# y = x*2 - 6abs(x) + 8

# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0

import sympy as sym
from sympy import symbols, latex, diff, S
from sympy.solvers import solve
from sympy.plotting import plot

sym.init_printing(use_latex='mathjax')


x = symbols('x',real=True) # ,real=True
f = x**2 - 6*abs(x) + 8
f


# 1. Находим корни функции (ищем значения x, при которых f(x)=0)
solve(f,x)

# 2,3. Интервалы, на которых функция возрастает и убывает:

f1 = diff(f)
f1 

extremum_x = solve(f1,x)
extremum_x[0].n()

print(f.subs(x,-extremum_x[0]).n())
print(f.subs(x,0).n())
print(f.subs(x,extremum_x[0]).n())

print(f1.subs(x,-2))
print(f1.subs(x,-0.2))
print(f1.subs(x,0.2))
print(f1.subs(x,2))


# 4. Построить график

str= latex(S(f,evaluate = False))
p = plot(f,(x,-8,8),title='$'+'f(x)='+str+'$', show=  False)
p.show()

# 5. Вычислить вершину

str= latex(S(f1,evaluate = False))
p = plot(f1,(x,-5,5), title = '$'+'f1(x)='+str+'$', show = False) # график производной
p.show()

# 6, 7. Определить промежутки, на котором f > 0 и f < 0

print(f.subs(x,-6))
print(f.subs(x,-3))
print(f.subs(x,0))
print(f.subs(x,3))
print(f.subs(x,6))


