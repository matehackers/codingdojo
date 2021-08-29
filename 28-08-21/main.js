/*
# Jokenpo
Jokenpo é uma brincadeira japonesa, onde dois jogadores escolhem um dentre três possíveis itens: Pedra, Papel ou Tesoura.

O objetivo é fazer um juiz de Jokenpo que dada a jogada dos dois jogadores informa o resultado da partida.

As regras são as seguintes:
Pedra empata com Pedra e ganha de Tesoura
Tesoura empata com Tesoura e ganha de Papel
Papel empata com Papel e ganha de Pedra

Fonte: https://dojopuzzles.com/problems/jokenpo/
*/

function main(dados) {
    if(dados.includes("pedra") && dados.includes("tesoura")){
      return "ganha pedra";
    }
    else if(dados.includes("pedra") && dados.includes("papel")){
      return "ganha papel";
    }
    else if (dados.includes("tesoura") && dados.includes("papel")){
      return "ganha tesoura";
    }
  
    return "empate"
  
  }
  
  module.exports = main;