import scipy, scipy.integrate
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
 
# Se define equação diferencial como sistema de duas equações de primeira ordem
def dydt(t,y,L):
    theta, dydt = y
    dvydt = -(g/L) * scipy.sin(theta)
    return [dydt,dvydt]
 
# Definimos umas constantes a título de exemplo
# g: aceleração da gravidade
# L: comprimento do pendulo 
# theta0: angulo inicial
# v0: velocidade inicial
  
g = 9.8
L = 2.2
theta0 = scipy.pi*5/12 # Ângulo inicial: 20 graus.
v0 = 0.0
  
sol = scipy.integrate.ode(dydt)
# 'dopri5' é para indicar ao solucionador que ele deve resolver a equação pelo método de Runge-Kutta
sol.set_integrator('dopri5') 
# .set_f_params é a funcão para passar os argumentos adicionais para a função diferencial. Neste caso, o comprimento do pendulo.
sol.set_f_params(L)
# Mostramos ao solucionador os valores iniciais
# theta0: angulo inicial
# v0: velocidade inicial
sol.set_initial_value([theta0,v0] , 0)
 
thetas = [] # Criar lista vazia de ordenadas
dt = 0.01 # Intervalo de variação de tempo
while sol.successful() and sol.t < 35:
    sol.integrate(sol.t+dt)
    thetas.append(sol.y[0]*180/scipy.pi) # Preencher a lista de ordenadas com os valores de theta
 
# Criar lista das abscissas de tempo
t=[]
for i in range(len(thetas)):
    t.append(i*dt)
 
fig = plt.figure() 
plt.plot(t,thetas) 
plt.xlabel('tempo (s)') 
plt.ylabel('Amplitude theta(t)') 
plt.show() 