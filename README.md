# NBA ULTIMATE TEAM
## Apresentação e Objetivo

Meu nome é Matheus Carvalho, estudante do terceiro período do curso de Ciência de Dados e Inteligência Artificial na Fundação Getúlio Vargas (FGV/RJ).

A ideia inicial deste projeto foi inspirada em um modo do jogo EAFC 24, antigo FIFA, chamado "Ultimate Team". Nele, o usuário tem que montar sua equipe com cartas de jogadores reais, levando em consideração, além da habilidade de cada jogador, pontos como a liga, o time em que ele joga ou a sua nacionalidade para alcançar o maior nível de entrosamento possível.

O projeto utiliza o design das cartas do "Ultimate Team" e dados que foram extraídos de diferentes fontes, desde o NBA2K até o site oficial da liga, para criar as cartas dos jogadores.

No entanto, o objetivo não é puramente estético. Pretendo criar uma página online onde será permitido ao usuário montar escalações, analisar os dados dos jogadores, compará-los e muito mais. Vale ressaltar que esse tipo de site é bastante popular para a comunidade de FIFA, da qual eu faço parte, mas não tanto quando o assunto é NBA2K.

O design das cartas foi totalmente elaborado utilizando a linguagem Python, que foi aquela com a qual tive maior contato no meu primeiro ano de faculdade. O restante do projeto será desenvolvido com ferramentas web, como HTML, CSS e JavaScript.

## Projetos
### Cartas
Segue abaixo um exemplo das diferentes versões de cartas, que foram a ideia inicial do projeto. As possibilidades de uso são diversas, desde jogos com dinâmica de cartas (que não foi completamente descartado por mim), até uma página web. É válido pontuar que elas são diferentes entre si, de acordo com o overall do jogador no NBA2K.

- **Inform (Preto com Dourado):** jogadores com overall maior ou igual a 90;
- **Ouro Raro (Dourado Brilhante):** jogadores com overall maior ou igual a 85;
- **Ouro Comum (Dourado Fosco):** jogadores com overall maior ou igual a 80;
- **Prata Raro (Prata Brilhante):** jogadores com overall maior ou igual a 75;
- **Prata Comum (Prata Fosco):** jogadores com overall maior ou igual a 70;
- **Bronze Raro (Bronze Brilhante):** jogadores com overall maior ou igual a 68;
- **Bronze Comum (Bronze Fosco):** com o restante dos jogadores de overall baixo.

<div style="text-align:center">
    <img src="https://raw.githubusercontent.com/MatCarvalho21/NBA_ultimate_team/main/main/assets/images/example_full_cards.png?token=GHSAT0AAAAAACM43EKOJTGTTTLBX4PEXMNQZNKRFXQ" alt="Exemplo de cartas" />
</div>

### Web Site
Além das cartas, também foi desenvolvido uma página web com algumas funcionalidades interessantes. A página foi desenvolvida inteiramente em `python`, utilizando a biblioteca `stremalit`. Segue abaixo, algumas das utilidades que foram disponibilizadas. 
##### Página Inicial
Ao acessar o site, o usuário encontra uma barra de pesquisa, onde ele pode pesquisar por qualquer jogador da liga e acessar suas estatísticas. Além disso, de forma fixa, é mostrado um ranking com os 15 melhores jogadores do jogo e, para finalizar, existe uma outra barra de pesquisa mais abaixo. Nela, o usuário pode selecionar um atributo, por exemplo "Three-Point Shot", e será gerado um ranking com os 15 melhores jogadores do jogo no quesito "Three-Point Shot".

<div style="text-align:center">
    <img src="https://raw.githubusercontent.com/MatCarvalho21/NBA_ultimate_team/main/main/assets/images/page/screenshots/home.png?token=GHSAT0AAAAAACM43EKOFSDXKE5PGNQYPF7EZNLFMBQ" alt="Página Inicial" />
</div>

<div style="text-align:center">
    <img src="https://raw.githubusercontent.com/MatCarvalho21/NBA_ultimate_team/main/main/assets/images/page/screenshots/ranking.png?token=GHSAT0AAAAAACM43EKPIAWCZ5N7JW3Z7NMIZNLFMDA" alt="Ranking Generator" />
</div>

##### Página dos Jogadores
Ao selecionar um jogador na página inicial, o usuário é direcionado para a página particular do respectivo atleta. Nessa página, são exibidas informações pessoais do jogador, assim como seus atributos dentro do jogo e um gráfico com uma visão geral da sua carta no jogo. 

<div style="text-align:center">
    <img src="https://raw.githubusercontent.com/MatCarvalho21/NBA_ultimate_team/main/main/assets/images/page/screenshots/player_page.png?token=GHSAT0AAAAAACM43EKOFMKL6UIJWJPMW5HSZNLFMEA" alt="Jogador" />
</div>


##### Página de Comparações
Acessando o menu, que fica no lado esquerdo da página, é possível navegar para outras seções do site, que possuem funcionalidades distintas. Uma delas é a página de comparações, onde o usuário pode selecionar até três jogadores e comparar seus atributos um a um para verificar os pontos fortes de cada um.

<div style="text-align:center">
    <img src="https://raw.githubusercontent.com/MatCarvalho21/NBA_ultimate_team/main/main/assets/images/page/screenshots/comparacao.png?token=GHSAT0AAAAAACM43EKOS4KVJ5T3RQVCVBEOZNLFMFQ" alt="Jogador" />
</div>


# NBA ULTIMATE TEAM (English)
## Introduction and Objective

My name is Matheus Carvalho, a third-semester student in the Data Science and Artificial Intelligence program at Fundação Getúlio Vargas (FGV/RJ).

The initial idea of this project was inspired by a mode in the EAFC 24 game, the old FIFA, called "Ultimate Team." In this mode, the user has to build their team with cards of real players, taking into consideration not only each player's skill but also factors like the league, the team they play for, or their nationality to achieve the highest level of chemistry.

The project utilizes the design of "Ultimate Team" cards and data extracted from various sources, from NBA2K to the league's official website, to create player cards.

However, the goal is not purely aesthetic. I intend to create an online page where users can build lineups, analyze player data, compare them, and much more. It's worth noting that this type of website is quite popular for the FIFA community, of which I am a part, but not as much when it comes to NBA2K.

The card designs were entirely created using the Python language, which I had the most exposure to in my first year of college. The rest of the project will be developed using web tools such as HTML, CSS, and JavaScript.

## Projects
### Cards
Below is an example of the different card versions, which were the initial idea of the project. The possibilities for use are diverse, ranging from games with card dynamics (which has not been completely ruled out by me) to a web page. It's worth noting that they differ from each other, according to the player's overall rating in NBA2K.

- **Inform (Black with Gold):** players with an overall rating of 90 or higher;
- **Rare Gold (Shiny Gold):** players with an overall rating of 85 or higher;
- **Common Gold (Matte Gold):** players with an overall rating of 80 or higher;
- **Rare Silver (Shiny Silver):** players with an overall rating of 75 or higher;
- **Common Silver (Matte Silver):** players with an overall rating of 70 or higher;
- **Rare Bronze (Shiny Bronze):** players with an overall rating of 68 or higher;
- **Common Bronze (Matte Bronze):** with the rest of the players with low overall ratings.

![Example cards](https://raw.githubusercontent.com/MatCarvalho21/NBA_ultimate_team/main/main/assets/images/example_full_cards.png?token=GHSAT0AAAAAACM43EKOJTGTTTLBX4PEXMNQZNKRFXQ)

### Web Site
In addition to the cards, a web page with some interesting features was also developed. The page was entirely developed in Python using the `streamlit` library. Below are some of the functionalities that were made available.

#### Home Page
Upon accessing the site, the user finds a search bar where they can search for any league player and access their statistics. In addition, a fixed ranking of the top 15 players.

![Home Page](https://raw.githubusercontent.com/MatCarvalho21/NBA_ultimate_team/main/main/assets/images/page/screenshots/home.png?token=GHSAT0AAAAAACM43EKOFSDXKE5PGNQYPF7EZNLFMBQ)

![Ranking Generator](https://raw.githubusercontent.com/MatCarvalho21/NBA_ultimate_team/main/main/assets/images/page/screenshots/ranking.png?token=GHSAT0AAAAAACM43EKPIAWCZ5N7JW3Z7NMIZNLFMDA)

#### Players Page
When selecting a player on the home page, the user is directed to the specific player's page. This page displays personal information about the player, as well as their in-game attributes and a chart with an overview of their in-game card.

![Players Page](https://raw.githubusercontent.com/MatCarvalho21/NBA_ultimate_team/main/main/assets/images/page/screenshots/player_page.png?token=GHSAT0AAAAAACM43EKOFMKL6UIJWJPMW5HSZNLFMEA)

#### Comparison Page
Accessing the menu on the left side of the page allows navigation to other sections of the site with distinct functionalities. One of them is the comparison page, where the user can select up to three players and compare their attributes one by one to evaluate each one's strengths.

![Comparison Page](https://raw.githubusercontent.com/MatCarvalho21/NBA_ultimate_team/main/main/assets/images/page/screenshots/comparacao.png?token=GHSAT0AAAAAACM43EKOS4KVJ5T3RQVCVBEOZNLFMFQ)
