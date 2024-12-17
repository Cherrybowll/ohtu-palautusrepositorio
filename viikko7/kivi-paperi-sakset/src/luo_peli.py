from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

def luo_peli(tyyppi):
    if tyyppi == "a":
        return KPSPelaajaVsPelaaja()
    if tyyppi == "b":
        return KPSTekoaly(Tekoaly())
    if tyyppi == "c":
        return KPSTekoaly(TekoalyParannettu(10))
    
    return None