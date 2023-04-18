import numpy as np
import matplotlib.pyplot as plt
import config

import numpy as np
import matplotlib.pyplot as plt
import config

def pokemon_radar():
    conn = config.getdb()
    cur = conn.cursor()

    cur.execute('''
        SELECT t.type, AVG (p.attack) as avg_attack, AVG (p.defense) as avg_defense, AVG (p.speed) as avg_speed
        FROM pokemon p
        JOIN type t on p.type_id = t.id
        GROUP BY t.type
    ''')
    data = cur.fetchall()
    
    type_colors = {
        'Bug': '#A6B91A',
        'Dark': '#705746',
        'Dragon': '#6F35FC',
        'Electric': '#F7D02C',   
        'Fairy': '#D685AD',
        'Fighting': '#C22E28',
        'Fire': '#EE8130',
        'Flying': '#A98FF3',
        'Ghost': '#735797',
        'Grass': '#7AC74C',
        'Ground': '#E2BF65',
        'Ice': '#96D9D6',
        'Normal': 'beige',
        'Poison': '#A33EA1',
        'Psychic': '#F95587',
        'Rock': '#B6A136',
        'Steel': '#B7B7CE',
        'Water': '#6390F0'
    }

    angles = np.linspace(0, 2 * np.pi, 3, endpoint=False).tolist()
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    for row in data:
        _type, attack, defense, speed = row
        color = type_colors[_type]
        values = [attack, defense, speed, attack]
        ax.plot(angles + [angles[0]], values, label=_type, color=color)

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.degrees(angles), labels=['Attack', 'Defense', 'Speed'])

    ax.set_rlabel_position(180 / len(data))
    plt.ylim(0, max(max([d[1] for d in data]), max([d[2] for d in data]), max([d[3] for d in data])))

    ax.legend(loc='upper right', bbox_to_anchor=(1, 1))
    plt.title("Radar Plot of Pokemon Types' Average Attack, Defense, and Speed")
    plt.show()

    config.closedb(conn)

if __name__ == "__main__":
    pokemon_radar()
