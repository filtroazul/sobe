# aquarela 🖤

joguinho-presente num arquivo só: **`index.html`**. tudo em preto e branco, desenhado como a lápis numa página em branco. feito pra **iPhone (Safari)** e PC.

## o que acontece

1. **começar** — botão na página em branco. ao tocar, a música começa (libera o som no iPhone) e ela aparece.
2. **andar** — partículas de tinta negra flutuando no ar; ela anda pra esquerda/direita.
3. **a flor** — depois de andar um pouco, uma flor desabrocha caindo na diagonal, *sendo desenhada*, e plana até a mão dela → primeiro textinho.
4. **os olhos** — ela anda mais, e vários olhos sketch abrem devagar lá em cima e a encaram, seguindo ela. somem → segundo textinho.
5. **a escada** — uma escada-rampa diagonal surge; ela sobe **o quanto quiser** enquanto o terceiro textinho aparece. quando você toca em *prosseguir*, a escada acaba.
6. **a floresta** — ela volta ao plano, para sozinha, e uma floresta inteira (árvores + flores) nasce à frente *sendo desenhada* com a câmera dando zoom → texto final.

> os textos digitam letra-a-letra (devagar, de propósito), em fonte de livro, e **rolam** se forem longos (arrasta pra cima/baixo, ou setas/scroll no PC).

## ⚠️ falta só a música

põe um arquivo **`musica.mp3`** aqui nesta pasta. se faltar, o jogo toca um som ambiente sintetizado sozinho pra não ficar mudo — mas o ideal é a tua música.

## como abrir no iPhone dela

precisa de um endereço **https** (por causa do som):

1. **Netlify Drop** (sem cadastro): entra em https://app.netlify.com/drop no PC e **arrasta a pasta `aquarela` inteira**. ele te dá um link `https://...netlify.app`. manda pra ela abrir no Safari.
2. **testar no PC agora**: dentro da pasta roda `python -m http.server 8099` e abre `http://localhost:8099`.

## controles

- **começar / prosseguir / som**: toque (ou Enter/Espaço no PC; 🔊 no canto liga/desliga).
- **andar**: botões ◀ ▶ nos cantos de baixo (ou setas / `A` `D` no PC).
- **rolar o texto**: arrasta na área do texto (ou setas ↑↓ / scroll).

## trocar textos / mexer

abre o `index.html` e edita o bloco **`TEXTS`** no comecinho do `<script>` (`flor`, `olhos`, `escada`, `floresta`). usa `\n\n` pra separar parágrafos.

## sprite da personagem

`walk.png` é a folha de caminhada (16 frames de 140×237), recortada do `elaanda.mp4` com fundo já transparente. os `.mp4` e o `ela_ultimoframe.png` ficam aqui só de arquivo — **não entram no jogo**.
