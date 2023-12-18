import pandas as pd
import matplotlib.pyplot as plt

file_path = "data.csv" 
df = pd.read_csv(file_path)

# Creare figura
fig, axes = plt.subplots(nrows=3, figsize=(12, 8))

# Plotează toate valorile pe prima axă
df.plot(ax=axes[0])
axes[0].set_title('Toate valorile')

# Plotează primele X 
X = 5
df.head(X).plot(ax=axes[1])
axes[1].set_title(f'Primele {X} valori pentru toate coloanele')

# Plotează ultimele Y valori pentru coloanele Durata și Puls pe a treia axă
Y = 15
df.tail(Y)[['Durata', 'Puls']].plot(ax=axes[2])
axes[2].set_title(f'Ultimele {Y} valori pentru Durata și Puls')


plt.tight_layout()

plt.show()