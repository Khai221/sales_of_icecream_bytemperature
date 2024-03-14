import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('IceCreamData.csv')

# tirando as casas decimais pra ficar mais bonito o gráfico
df = df.round(0).astype(int)

# convertendo temperatura (fahrenheit) pra celsius
celsius = (df['Temperature'] - 32) * 5/9
df['Temperature'] = celsius


result = df.sort_values('Temperature', ascending = False)


# graph

plt.figure(figsize=(10,6))

plt.plot(result['Temperature'], result['Revenue'], 'r.--',label = 'US$')

plt.title('Ice Cream Truck')
plt.ylabel('Sales (US$)')
plt.xlabel('Temperatura (Celsius)')

plt.legend()
plt.show()