from urllib import request
import toml
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        toml_content = toml.loads(content)
        #Epäonnistuu varmasti, jos pyproject.toml ei sisällä jotain avaimista
        #Poikkeustapaukset huomioiva toteutus ei liene tehtävän kannalta olennaista?
        return Project(toml_content["tool"]["poetry"]["name"],
                       toml_content["tool"]["poetry"]["description"],
                       toml_content["tool"]["poetry"]["license"],
                       toml_content["tool"]["poetry"]["authors"],
                       toml_content["tool"]["poetry"]["dependencies"],
                       toml_content["tool"]["poetry"]["group"]["dev"]["dependencies"])
