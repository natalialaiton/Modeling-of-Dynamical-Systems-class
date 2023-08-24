
import plotly.express as px
import plotly.io as pio
import math
import pandas as pd


def initial_cond(state_var,alpha,beta,gamma,delta,total_time):
 x=state_var[0]
 y=state_var[1]
 z=state_var[2]
 a=alpha
 b=beta
 c=gamma
 d=delta
 t=total_time
 resaults=[]
 return [x,y,z],a,b,c,d,t,resaults

def observe(resaults,state_var):
 return resaults.append(state_var)

def update(num_oficers, Sz_budget,Sz_st_money, alpha, beta, gamma, delta):
 return [alpha*num_oficers+(beta/Sz_budget),Sz_budget+(gamma*num_oficers),(Sz_budget*delta)*num_oficers]

state_var,Coeff_1,Coeff_2,Coeff_3,coeff_4,Time,Resaults=initial_cond([1,1,1],0.1,0.5,0.2,0.5,100)

for time in range(Time):
 observe(Resaults,state_var)
 state_var=update(state_var[0],state_var[1],state_var[2],Coeff_1,Coeff_2,Coeff_3,coeff_4)

#print(Resaults)
df = pd.DataFrame(Resaults,columns = ['x', 'y','z'])
fig= px.line_3d(df, x="x", y="y",z="z",title='corruption in Colombia')

#fig.update_layout(xaxis_title='x',yaxis_title='y',zaxis_title='z')
legend_names={'0':'x'}

#fig.for_each_trace(lambda t: t.update(name=legend_names[t.name]))
fig.show()
