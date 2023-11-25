
function mudar_imagem_quadra() {
    /* Função que vai, com base em um drop-options, atualizar a escolha do 
    usuário a imagem de fundo da quardra. A função será chamada quando o o botão, logo
    abaixo do select, for pressionado. */

    // Obtém o valor selecionado no dropdown
    var selecionado = document.getElementById("escolha_times").value;
  
    // Atualiza a src da imagem com base na seleção
    document.getElementById("imagem_quadra").src = "imagens_de_quadras/quadra_" + selecionado + ".png";
  }

function mudar_time(numero_escalacao){
  var selecionado = document.getElementById("escolha_escalacao_" + numero_escalacao).value;

  document.getElementById("PG" + numero_escalacao).src = "imagens_de_times/" + selecionado + "/PG_" + selecionado + ".png";
  document.getElementById("SG" + numero_escalacao).src = "imagens_de_times/" + selecionado + "/SG_" + selecionado + ".png";
  document.getElementById("SF" + numero_escalacao).src = "imagens_de_times/" + selecionado + "/SF_" + selecionado + ".png";
  document.getElementById("PF" + numero_escalacao).src = "imagens_de_times/" + selecionado + "/PF_" + selecionado + ".png";
  document.getElementById("CE" + numero_escalacao).src = "imagens_de_times/" + selecionado + "/CE_" + selecionado + ".png";
}