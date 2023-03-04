## IFS-API

Esta é uma api que disponibiliza os dados(cartões vermelhos e amarelos, partidas jogadas e golos marcados em cada época desportiva) de determinadas equipes de futibol.

Os dados da mesma são pegues do site https://pt.besoccer.com/ , por meio de webscraping.

### EndPoints

*Estes são os endpoints desta api.*

- **/equipes** -> Tráz uma lista com as equipes de destaque de cada continente.
- **/info-clube/yellow-card/\<nome_da_equipe>/** -> Tráz uma lista com os cartões amarelos de cada temporada.
- **/info-clube/red-card/\<nome_da_equipe>/** -> Tráz uma lista com os cartões vermelhos de cada temporada.
- **/info-clube/gols/\<nome_da_equipe>/** -> Tráz uma lista com os gols marcados em cada temporada.
- **/info-clube/partidas/\<nome_da_equipe>/** -> Tráz uma lista com o nº de partidas jogadas em cada temporada.

> No caso de falha no scraping será retornada uma mensagem 'json' informando.


Copyright - Eliseu Gaspar - .