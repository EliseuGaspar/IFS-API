import json as j

import requests as web
from bs4 import BeautifulSoup


class yellowcard():
    
    def __init__(self) -> None:
        self.yellow_cards = self.list_name = self.list_name2 = self.yellowcards = []
    
    def __limpo__(self, name : str) -> str:   
            name = name.lstrip()
            name = name.rstrip()
            name = name.replace(' ','-')
            return name
    
    def __Soup__(self, time : str, epoca : str) -> list:

        yellowcards = list_temporadas = list_yellowcards = list_ = []

        time = self.__limpo__(time)
        
        content = web.get(f'https://pt.besoccer.com/time/historico/{time}').content
            
        soup = BeautifulSoup(content,'html.parser')

        list_temporadas = soup.select(" .trajectory .table_parents tbody tr.parent_row .season-td a")

        list_yellowcards = soup.select(" .trajectory .table_parents tbody tr.parent_row td:nth-of-type(4) b")

        for i in range(len(list_temporadas)):
            list_.append(
                {
                    f"Temporada {list_temporadas[i].get_text()}" : f"Cartões Amarelos {list_yellowcards[i].get_text()}"
                }
            )

        if list_ != []:
            return list_
        else:
            return "Não foi possível achar resultados para a sua pesquisa"

    def Scraping(self, time : str, epoca : str) -> dict:
        self.__init__()
        return self.__Soup__(time,epoca)




