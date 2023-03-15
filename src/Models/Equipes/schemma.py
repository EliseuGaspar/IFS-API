import json as j

import requests as r
from bs4 import BeautifulSoup


def equipes():
	sufix_times = ['eu','am','ao','af']
	total_equipes = []
	DIC = {}

	for x in range(len(sufix_times)):
		content = r.get(f'https://pt.besoccer.com/times/{sufix_times[x]}').content

		soup = BeautifulSoup(content,'html.parser')

		list_top_15 = soup.select('#popular .panel-body .item-list li .item-box .left-content .desc-boxes .main-text')

		list_projecoes_15 = soup.select('#mod_popular_team .panel-body .item-list li .item-box .left-content .desc-boxes .main-text')

		for equipes in list_top_15:
			total_equipes.append(equipes.get_text())

		for equipes in list_projecoes_15:
			total_equipes.append(equipes.get_text())

	for x in range(len(total_equipes)):
		if x < 31:
			DIC[x] = {
				'name': total_equipes[x],
				'continent': 'Europa'
			}
		elif x < 61:
			DIC[x] = {
				'name': total_equipes[x],
				'continent': 'Americas'
			}
		elif x < 91:
			DIC[x] = {
				'name': total_equipes[x],
				'continent': 'Asia/Oceania'
			}
		else:
			DIC[x] = {
				'name': total_equipes[x],
				'continent': 'Africa'
			}

	return DIC