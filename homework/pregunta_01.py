"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

# pylint: disable=import-outside-toplevel

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import os
    import pandas as pd
    import matplotlib.pyplot as plt

    os.makedirs("files/plots", exist_ok=True)

    df = pd.read_csv("files/input/news.csv")
    years = df.iloc[:, 0].tolist()
    tv = df["Television"].tolist()
    news = df["Newspaper"].tolist()
    radio = df["Radio"].tolist()
    internet = df["Internet"].tolist()

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(years, tv, color='#666666', linewidth=2)
    ax.plot(years, news, color='#888888', linewidth=2)
    ax.plot(years, radio, color='#bbbbbb', linewidth=2)
    ax.plot(years, internet, color='#1f77b4', linewidth=2)

    # etiquetas iniciales con nombre y porcentaje
    ax.text(years[0], tv[0], f"Television {tv[0]}%", color='#666666', va='center', ha='right')
    ax.text(years[0], news[0], f"Newspaper {news[0]}%", color='#888888', va='center', ha='right')
    ax.text(years[0], radio[0], f"Radio {radio[0]}%", color='#bbbbbb', va='center', ha='right')
    ax.text(years[0], internet[0], f"Internet {internet[0]}%", color='#1f77b4', va='center', ha='right')

    # etiquetas finales con porcentaje
    ax.text(years[-1], tv[-1], f"{tv[-1]}%", color='#666666', va='center', ha='left')
    ax.text(years[-1], news[-1], f"{news[-1]}%", color='#888888', va='center', ha='left')
    ax.text(years[-1], radio[-1], f"{radio[-1]}%", color='#bbbbbb', va='center', ha='left')
    ax.text(years[-1], internet[-1], f"{internet[-1]}%", color='#1f77b4', va='center', ha='left')

    ax.set_title('How people get their news', fontsize=16, weight='bold', pad=20)
    ax.text(
        0.5,
        1.02,
        'An increasing proportion cite the internet as their primary news source',
        transform=ax.transAxes,
        ha='center',
        va='bottom'
    )

    ax.set_xticks(years)
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    plt.tight_layout()
    plt.savefig("files/plots/news.png")
    plt.close()
