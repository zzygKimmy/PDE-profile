
import pandas as pd
import numpy as np
# import cmath

low = pd.read_excel(r'C:\path...\data.xlsx', index_col=0,usecols="A:H")
high = pd.read_excel(r'C:\path...\data.xlsx', index_col=0,usecols="A,I:O")

print(high)

# Problem (b)

# R=8.314J/K mol when the pressure is in kPa
R = 8.314
# low temperature 25 celsius = 298.15 K
T1 = 298.15
# high temperature 1000 celsius = 1273.15 K
T2 = 1273.15
# get the enthalpy with temperature and specific the name of the content
def get_enthalpy( name, df, T ):
    h0 = 0.0
    for i in range(0,5):
        h0 += (1/(i+1)) * df.loc[name][i]*T**(i+1)
        # print(name + ": " + str(df.loc[name][i]))
    h0 += df.loc[name][5]
    # print(name + ": " + str(df.loc[name][5]))
    return h0*R

# h_rp = [ np*hp (product) - nr*hr (reactant) ] * 10**(-3) KJ/mole
h_rp_low = (-1/3*get_enthalpy('ch4',low,T1) - 2/3*get_enthalpy('O2',low,T1) + 1/3*get_enthalpy('CO2',low,T1) + 2/3*get_enthalpy('H2O',low,T1))*10**(-3)
h_rp_high = (-1/3*get_enthalpy('ch4',high,T2) - 2/3*get_enthalpy('O2',high,T2) + 1/3*get_enthalpy('CO2',high,T2) + 2/3*get_enthalpy('H2O',high,T2))*10**(-3)

print( 'the heat of combustion for low temperature is ' + str(h_rp_low) + ' KJ/mol')
print( 'the heat of combustion for high temperature is ' + str(h_rp_high) + ' KJ/mol')

# Problem (c)
# initial temperature is 25 degree celsius
Ti = T1
# calculate in J/mole
h_rp_react = (1/3*get_enthalpy('ch4',low,Ti) + 2/3*get_enthalpy('O2',low,Ti))

# h_rp (reactant) = h_rp (product) in adiabatic reaction
coeff = []
coeff.append( R*(1/3 * high.loc['CO2'][5] + 2/3 * high.loc['H2O'][5]) - h_rp_react )
for i in range(0,5):
    coeff.append( (1/(i+1) * (1/3 * high.loc['CO2'][i] + 2/3 * high.loc['H2O'][i]))*R )
roots = np.roots(coeff[::-1])
print( roots )


# Problem (d)
Ti = T1
h_rp_react = (1/10.52*get_enthalpy('ch4',low,Ti) + 2/10.52*get_enthalpy('O2',low,Ti) + 7.52/10.52*get_enthalpy('N2',low, Ti))
coeff = []
coeff.append(R*(1/10.52*high.loc['CO2'][5] + 2/10.52 * high.loc['H2O'][5] +7.52/10.52* high.loc['N2'][5]) - h_rp_react)
for i in range(0,5):
    coeff.append((1/(i+1) * (1/10.52 * high.loc['CO2'][i] + 2/10.52 * high.loc['H2O'][i] + 7.52/10.52 * high.loc['N2'][i]))*R)
roots = np.roots(coeff[::-1])
print( roots )

