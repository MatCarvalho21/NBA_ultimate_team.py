

var dicionario_de_cores = {
  "padrao": "rgb(78, 78, 78)",
  "atlanta_hawks": "rgb(225, 58, 62)",
  "boston_celtics": "rgb(0, 122, 51)",
  "brooklyn_nets": "rgb(0, 0, 0)",
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


function mudar_imagem_quadra() {
    /* Função que vai, com base em um drop-options, atualizar a escolha do 
    usuário a imagem de fundo da quardra. A função será chamada quando o o botão, logo
    abaixo do select, for pressionado. */

    // Obtém o valor selecionado no dropdown
    var selecionado = document.getElementById("escolha_times").value;
  
    // Atualiza a src da imagem com base na seleção
    document.getElementById("imagem_quadra").src = "imagens_de_quadras/quadra_" + selecionado + ".png";
    document.getElementById("logo").src = "logos/logo_" + selecionado + ".png";
    document.body.style.backgroundColor = dicionario_de_cores[selecionado]
  }

function mudar_time(numero_escalacao){
  var selecionado = document.getElementById("escolha_escalacao_" + numero_escalacao).value;

  document.getElementById("PG" + numero_escalacao).src = "imagens_de_times/" + selecionado + "/PG_" + selecionado + ".png";
  document.getElementById("SG" + numero_escalacao).src = "imagens_de_times/" + selecionado + "/SG_" + selecionado + ".png";
  document.getElementById("SF" + numero_escalacao).src = "imagens_de_times/" + selecionado + "/SF_" + selecionado + ".png";
  document.getElementById("PF" + numero_escalacao).src = "imagens_de_times/" + selecionado + "/PF_" + selecionado + ".png";
  document.getElementById("CE" + numero_escalacao).src = "imagens_de_times/" + selecionado + "/CE_" + selecionado + ".png";
}

