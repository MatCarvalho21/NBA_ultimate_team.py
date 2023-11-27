

/* dicionário com o nome dos time como chaves e os valores como as cores associadas a cada uma das franquias */
var dicionario_de_cores = {
    "padrao": "rgb(255, 255, 255)",
    "atlanta_hawks": "rgb(225, 58, 62)",
    "boston_celtics": "rgb(0, 122, 51)",
    "brooklyn_nets": "rgb(30, 30, 30)",
    "charlotte_hornets": "rgb(29, 17, 96)",
    "chicago_bulls": "rgb(206, 17, 38)",
    "cleveland_cavaliers": "rgb(111, 38, 61)",
    "dallas_mavericks": "rgb(0, 83, 188)",
    "denver_nuggets": "rgb(13, 34, 64)",
    "detroit_pistons": "rgb(13, 33, 79)",
    "golden_state_warriors": "rgb(0, 107, 182)",
    "houston_rockets": "rgb(206, 17, 38)",
    "indiana_pacers": "rgb(0, 45, 98)",
    "la_clippers": "rgb(200, 16, 46)",
    "los_angeles_lakers": "rgb(85, 37, 130)",
    "memphis_grizzlies": "rgb(93, 118, 169)",
    "miami_heat": "rgb(152, 0, 46)",
    "milwaukee_bucks": "rgb(0, 71, 27)",
    "minnesota_timberwolves": "rgb(12, 35, 64)",
    "new_orleans_pelicans": "rgb(0, 22, 65)",
    "new_york_knicks": "rgb(0, 107, 182)",
    "oklahoma_city_thunder": "rgb(0, 125, 195)",
    "orlando_magic": "rgb(0, 125, 197)",
    "philadelphia_76ers": "rgb(0, 107, 182)",
    "phoenix_suns": "rgb(229, 96, 32)",
    "portland_trail_blazers": "rgb(224, 58, 62)",
    "sacramento_kings": "rgb(91, 43, 130)",
    "san_antonio_spurs": "rgb(6, 25, 34)",
    "toronto_raptors": "rgb(206, 17, 38)",
    "utah_jazz": "rgb(0, 43, 92)",
    "washington_wizards": "rgb(227, 24, 55)"
  };

function set_tema(){
    /* extraindo do select de quadra/tema qual time o usuário selecionou */
    var tema_selecionado = document.getElementById("selecao_quadra").value;

    /* mudando a imagem da quadra */
    document.getElementById("quadra_imagem").src = "assets/imagens_de_quadras/quadra_" + tema_selecionado + ".png";

    /* mudando o logo da página */
    document.getElementById("logo").src = "assets/logos/logo_" + tema_selecionado + ".png";

    /* mudando a cor de fundo da página */
    document.body.style.backgroundColor = dicionario_de_cores[tema_selecionado];

    /* FALTA COLOCAR O BOTÃO DE DOWNLOAD E EVENTUALMENTE MUDAR A COR DELE */ 
}

