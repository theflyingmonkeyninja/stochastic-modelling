import numpy as np
import matplotlib.pyplot as plt

mu = 0.0
nsims = 500
dt = 1
T = 30
S0 = 100
sigma = 0.02

def stockprices(S0,mu,sigma,dt,nsims,T):
    sp_i=0.0;
    Tvect = list(range(int(T/dt)));
    S = np.zeros((nsims,len(Tvect)),"float");
    for i in range(nsims):
        for j in range(len(Tvect)):
            if j<1:
                sp_i = S0;
            else:
                sp_i = sp_i*np.exp((mu-(sigma**2/2))*dt+sigma*np.random.randn()*np.sqrt(dt));
                
            S[i,j] = sp_i
           
    return S
    


S = stockprices(S0,mu,sigma,dt,nsims,T)
T = np.linspace(0,T,30)
plt.plot(T,np.transpose(S))