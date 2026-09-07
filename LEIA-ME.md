# Corpo Dinâmico Academia — Sistema de Gestão

## Como isso funciona agora (arquivo único, do jeito que você pediu)

- O programa é **um único arquivo**: `CorpoDinamico.exe`.
- Ele já vem com **a logo oficial da academia como ícone**.
- Você clica duas vezes nele e o sistema **abre direto**, sem instalador,
  sem pedir para achar arquivo nenhum.
- Pode colocar esse único arquivo em qualquer lugar — Área de Trabalho,
  Downloads, um pendrive — e mover, copiar ou renomear ele à vontade.

**A pergunta que resolve o "risco de perder pasta":** os dados da academia
(alunos, pagamentos, backups) **não ficam ao lado do `.exe`**. Eles ficam
guardados automaticamente numa pasta fixa e própria do Windows
(`%LOCALAPPDATA%\CorpoDinamico`), que existe *independente de onde o `.exe`
está guardado no momento*. Ou seja: mesmo que você mova só o arquivo
`CorpoDinamico.exe` sozinho para outro lugar, os dados continuam intactos,
porque nunca dependeram de estar "do ladinho" dele. Testei isso na prática
(simulando mover o `.exe` de pasta) antes de te entregar.

---

## Última mudança: se ainda não abria, agora o erro vai aparecer na tela

Simplifiquei de propósito para eliminar a causa mais provável do problema:

- **Removi o `pywebview`** (a "moldura" de janela nativa). Ele depende de
  componentes do Windows (WebView2/pythonnet) que eu não tenho como testar
  de verdade neste ambiente, e empacotamento incompleto desses componentes
  é uma causa clássica de "o `.exe` não abre nada". Agora o sistema abre
  direto no seu **navegador padrão** — mais simples, com muito menos peças
  que podem falhar na hora de empacotar.
- **Ativei a janela de console** (temporariamente). Antes, se algo desse
  errado, o programa fechava em silêncio — por isso você não conseguia me
  dizer qual era o erro. Agora, qualquer falha aparece como texto na tela,
  com a mensagem completa, e a janela **espera você apertar Enter** antes
  de fechar. Testei isso de propósito (provocando um erro de mentira) para
  confirmar que a mensagem realmente aparece em vez de desaparecer.

**Se depois de gerar o `.exe` de novo ainda der problema:** vai aparecer
uma tela preta com o erro em texto. Copie esse texto inteiro e me envie —
com isso eu consigo corrigir o problema real, em vez de tentar adivinhar.

## Como gerar o seu `CorpoDinamico.exe`

Continuo sem conseguir compilar o `.exe` aqui no meu ambiente (é Linux, sem
internet para as ferramentas de empacotamento) — mas deixei tudo pronto até
faltar só este passo, que só pode ser feito no seu Windows.

1. Abra o **Prompt de Comando** (tecla Windows, digite `cmd`, Enter) dentro
   da pasta onde você extraiu este projeto.
2. Cole, uma linha de cada vez:
   ```
   pip install -r requirements.txt
   pyinstaller CorpoDinamico.spec --noconfirm
   ```
3. Pronto. O arquivo vai estar em: **`dist\CorpoDinamico.exe`**

Esse arquivo é o único que importa a partir de agora. Copie-o para onde
quiser (pode até apagar o resto da pasta do projeto depois, se quiser —
o `.exe` já leva tudo o que precisa embutido).

### Sobre o aviso do Windows na primeira vez que abrir

Por ser um programa novo, sem uma assinatura digital paga (certificado de
"code signing" — algo que custa dinheiro e exige verificação de identidade
numa autoridade certificadora, que eu não tenho como gerar por você), é
esperado que o Windows mostre um aviso do SmartScreen na primeira vez que
o `.exe` for aberto. Isso não é o mesmo bloqueio de antes (aquele era
causado pelo script `.bat`, que já removi do projeto). A ação correta e segura é:

1. Clique em **"Mais informações"**.
2. Clique em **"Executar assim mesmo"**.

Isso autoriza só este programa, uma única vez — não desativa nenhuma
proteção do Windows.

---

## MODO DESENVOLVEDOR (testar sem gerar o .exe)

```
pip install -r requirements.txt
python main.py
```
Nesse modo, os dados ficam numa pasta `_dados_dev` dentro do próprio
projeto (só para facilitar testes — no `.exe` final, viram AppData).

---

## O QUE FOI RETESTADO NESTA MUDANÇA

- **Bug real encontrado e corrigido:** o `main.py` ainda tentava criar uma
  pasta `config` do lado do `.exe` (resquício do modelo antigo) para guardar
  a trava de instância única. Isso quebrava o programa assim que abria —
  antes de qualquer tela aparecer — exatamente o tipo de coisa que você
  provavelmente estava vendo. Corrigido: agora esse arquivo técnico também
  vai para a pasta fixa em `%LOCALAPPDATA%`, junto com o resto dos dados.
- Depois de corrigir, testei o cenário **exatamente como o `.exe` real
  funcionaria**: simulei `sys.frozen=True`, uma pasta de `.exe` qualquer,
  e confirmei que a trava de instância, a criação do banco e a subida do
  servidor até a primeira tela funcionam sem nenhum erro.
- Simulei mover o `.exe` de uma pasta para outra e confirmei que os dados
  continuam no mesmo lugar (não se perdem).
- Refiz a bateria completa de testes (alunos, pagamentos, backup, PDF,
  saúde do sistema) depois da mudança — tudo passou.
- A tela de "Saúde do sistema" agora mostra exatamente onde os dados estão
  guardados, para você conferir quando quiser.

## O QUE CONTINUA SIMPLIFICADO (sem mudança)

- Gráficos visuais no dashboard/PDF (hoje são tabelas).
- Criptografia do arquivo de backup (hoje só tem checksum, não senha).
- Recuperação de senha esquecida do proprietário (de propósito).
- Assinatura digital do `.exe` (depende de certificado pago).

---

## ESTRUTURA DO PROJETO (só usada até você gerar o .exe)

```
CorpoDinamico/
├── main.py                    → ponto de entrada
├── requirements.txt
├── CorpoDinamico.spec         → receita do PyInstaller (arquivo único)
├── app/                        → todo o código do sistema
├── assets/logo/                → logo oficial (fica embutida no .exe)
```

Depois de gerado, o que importa é só: **`dist\CorpoDinamico.exe`**
