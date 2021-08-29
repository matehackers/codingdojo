/*
Arquivo que contem nossos testes unitarios
Para rodar no terminal os testes basta digitar:
jest

Doc da lib usada:
https://jestjs.io/pt-BR/docs/getting-started
*/

const main = require('./main');

test('testa pedra x pedra', () => {
  expect(main("pedra", "pedra")).toBe("empate");
});

test('testa pedra x tesoura', () => {
  expect(main(["pedra", "tesoura"])).toBe("ganha pedra");
});


test('testa pedra x papel', () => {
  expect(main(["pedra", "papel"])).toBe("ganha papel");
});

test('teste tesoura x papel', () => {
  expect(main(["tesoura", "papel"])).toBe("ganha tesoura");
});

test('teste tesoura x tesoura', () => {
  expect(main(["tesoura", "tesoura"])).toBe("empate");
})

test('teste papel x papel', () => {
  expect(main(["papel","papel"])).toBe("empate");
});

test('teste tesoura x pedra', () => {
  expect(main(["tesoura","pedra"])).toBe("ganha pedra");
});