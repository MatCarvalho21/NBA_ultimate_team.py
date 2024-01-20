# NBA ULTIMATE TEAM
## Apresentação e Objetivo

Meu nome é Matheus Carvalho, estudante do terceiro período do curso de Ciência de Dados e Inteligência Artificial na Fundação Getúlio Vargas (FGV/RJ).

A ideia inicial deste projeto foi inspirada em um modo do jogo EAFC 24, antigo FIFA, chamado "Ultimate Team". Nele, o usuário tem que montar sua equipe com cartas de jogadores reais, levando em consideração, além da habilidade de cada jogador, pontos como a liga, o time em que ele joga ou a sua nacionalidade para alcançar o maior nível de entrosamento possível.

O projeto utiliza o design das cartas do "Ultimate Team" e dados que foram extraídos de diferentes fontes, desde o NBA2K até o site oficial da liga, para criar as cartas dos jogadores.

No entanto, o objetivo não é puramente estético. Pretendo criar uma página online onde será permitido ao usuário montar escalações, analisar os dados dos jogadores, compará-los e muito mais. Vale ressaltar que esse tipo de site é bastante popular para a comunidade de FIFA, da qual eu faço parte, mas não tanto quando o assunto é NBA2K.

O design das cartas foi totalmente elaborado utilizando a linguagem Python, que foi aquela com a qual tive maior contato no meu primeiro ano de faculdade. O restante do projeto será desenvolvido com ferramentas web, como HTML, CSS e JavaScript.

## Repositório
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
