from tuomari import Tuomari


class KiviPaperiSakset:
    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = self._tokan_siirto(ekan_siirto)

        print(f"Tietokone valitsi: {tokan_siirto}")

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = self._tokan_siirto(ekan_siirto)

            print(f"Tietokone valitsi: {tokan_siirto}")

        print("Kiitos!")
        print(tuomari)

    def _tokan_siirto(self, ekan_siirto):
        raise Exception("Korvattava metodi")

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"