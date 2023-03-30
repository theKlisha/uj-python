import time
from mtablica import MonitorowanaTablica
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def mesure(sortFunction, N, target):
    tablica = MonitorowanaTablica(0, 1000, N, target)
    algorytm = sortFunction.__name__ 
    t0 = time.perf_counter()
    sortFunction(tablica)
    delta_t = time.perf_counter() - t0
    return {
        "history": tablica,
        "time": delta_t, 
        "steps": len(tablica.pelne_kopie),
        "algorytm": algorytm
    }

def animate(tablica, algorytm=None, FPS=60):
    N = len(tablica)
    # konfiguracja wyświetlania histogramu
    plt.rcParams["font.size"] = 16
    fig, ax = plt.subplots(figsize=(16, 8))
    container = ax.bar(np.arange(0, len(tablica), 1), tablica.pelne_kopie[0], align="edge", width=0.8)
    fig.suptitle(f"Sortowanie: {algorytm}")
    ax.set(xlabel="Indeks", ylabel="Wartość")
    ax.set_xlim([0, N])
    txt = ax.text(0.01, 0.99, "", ha="left", va="top", transform=ax.transAxes)

    # funkcja aktualizująca stan poszczególnych klatek do wyświetlenia
    def update(frame):
        txt.set_text(f"Liczba operacji = {frame}")
        for rectangle, height in zip(container.patches, tablica.pelne_kopie[frame]):
            rectangle.set_height(height)
            rectangle.set_color("darkblue")

        idx, op = tablica.aktywnosc(frame)
        if op == "get":
            container.patches[idx].set_color("green")
        elif op == "set":
            container.patches[idx].set_color("red")

        return (txt, *container)

    # tu akumulowana jest animacja, wyświetlna komendą show
    ani = FuncAnimation(fig, update, frames=range(len(tablica.pelne_kopie)), blit=True, interval=1000./FPS, repeat=False)
    plt.show()
