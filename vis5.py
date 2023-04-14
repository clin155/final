import numpy as np
import matplotlib.pyplot as plt
import config

def weight_vs_energy():
    conn = config.getdb()
    cur = conn.cursor()

    cur.execute("SELECT energy, weight FROM dogs")
    data = cur.fetchall()
    energy_levels = sorted(set(entry[0] for entry in data))

    weights_by_energy = [[] for _ in range(len(energy_levels))]
    for energy, weight in data:
        index = energy_levels.index(energy)
        weights_by_energy[index].append(weight)

    plt.boxplot(weights_by_energy, labels = energy_levels)
    plt.xlabel('Energy Level')
    plt.ylabel('Weight')
    plt.title('Box Plot of Dog Weights by Energy Level')
    plt.show()
    
    config.closedb(conn)

weight_vs_energy()