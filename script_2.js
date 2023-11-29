

/* dicionário com o nome dos time como chaves e os valores como as cores associadas a cada uma das franquias */
var dicionario_de_cores = {
    "padrao": "rgb(21, 64, 52)",
    "atlanta_hawks": "rgb(191, 17, 49)",
    "boston_celtics": "rgb(3, 140, 62)",
    "brooklyn_nets": "rgb(30, 30, 30)",
    "charlotte_hornets": "rgb(3, 150, 166)",
    "chicago_bulls": "rgb(191, 6, 55)",
    "cleveland_cavaliers": "rgb(140, 22, 66)",
    "dallas_mavericks": "rgb(3, 74, 166)",
    "denver_nuggets": "rgb(5, 36, 64)",
    "detroit_pistons": "rgb(166, 13, 54)",
    "golden_state_warriors": "rgb(242, 187, 19)",
    "houston_rockets": "rgb(191, 17, 49)",
    "indiana_pacers": "rgb(8, 32, 64)",
    "la_clippers": "rgb(30, 30, 30)",
    "los_angeles_lakers": "rgb(242, 183, 5)",
    "memphis_grizzlies": "rgb(2, 48, 89)",
    "miami_heat": "rgb(166, 27, 52)",
    "milwaukee_bucks": "rgb(1, 64, 11)",
    "minnesota_timberwolves": "rgb(2, 48, 89)",
    "new_orleans_pelicans": "rgb(5, 36, 64)",
    "new_york_knicks": "rgb(3, 74, 166)",
    "oklahoma_city_thunder": "rgb(5, 131, 242)",
    "orlando_magic": "rgb(4, 96, 217)",
    "philadelphia_76ers": "rgb(27, 73, 166)",
    "phoenix_suns": "rgb(24, 18, 64)",
    "portland_trail_blazers": "rgb(191, 17, 49)",
    "sacramento_kings": "rgb(79, 44, 115)",
    "san_antonio_spurs": "rgb(30, 30, 30)",
    "toronto_raptors": "rgb(115, 2, 32)",
    "utah_jazz": "rgb(1, 22, 64)",
    "washington_wizards": "rgb(191, 17, 49)"
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

    /* mudando a linha de fora do input */
    document.getElementById("selecao_quadra").style.outline = "2px solid " + dicionario_de_cores[tema_selecionado];

    /* FALTA COLOCAR O BOTÃO DE DOWNLOAD E EVENTUALMENTE MUDAR A COR DELE */ 
}

