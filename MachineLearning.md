#Notas - Machine Learning

## Termos:
  - ML -> Machine Learning
  - DM -> Data Mining

## Origens
  - ~viagem sobre banco de dados arcaicos e tudo mais do livro~
  - O campo de pesquisa nasceu em um ambiente em que os dados disponíveis, métodos estatísticos e poder de processamento evoluiram rapidamente e simultaneamente;
  - A enorme quantidade de dados precisava de novos métodos para análise;
  - O desenvolvimento simultâneo e rápido surgiu graças as grandes quantidades de dados que estavam disponíveis, assim como os metodos estatísticos e o poder de processamento que já está constantemente aumentado;
  - 'Primo' do **data mining**, que está preocupado em gerar uma nova forma de observar (compreender) os dados de um banco de dados extenso;
    - Os campos são parecidos, porém se diferenciam no fato em que o **data mining** tenta achar informações escondidas enquanto **machine learning** foca em realizar alguma tarefa conhecida;
    - ex: Data Mining serve para achar o carro mais seguro e Machine Learning para dirigi-ló;

## Usos e Abusos
  - O interesse de **ML** é primeiramente interessado no sentido de dados complexos;
    - Missão ampla e agnóstica de aplicação
  - Usos:
    * Prever resultado de eleições
    * Filtrar spam e mensagens de email
    * Prever ação criminosa
    * Automizar sinais de trafégo com base em condições de trânsito
    * Produzir estimativas financeiras de desastres naturais
    * Examinar rotatividade de clientes
    * Criar veículos autonômos
    * Identificar individuos com capacidade de doar
    * Focar propaganda em tipos específicos de clientes
  - Todas essa tarefas possuem um processamento comum. Um algoritmo de *ML* consegue identificar padrões que podem ser usado para ações.
    - Alguns casos são tão bem sucedidos que eles atingem um status *lendário*
  - **História do varejista vs. pai**
  - Usos no varejo:
    - Promoções "miradas"
    - Gerenciamento de estoque
    - Posicionamento de items na loja
    - Gerar promoções para items no carrinho
    - Propagandas baseadas no histórico
    - Utiliza padrões de comportamento de clientes para fazer recomendações
    - *magic*
    - Seus dados mostram seu comportamento
      - Eles conhecem melhor você do que você mesmo
      - Uns acham divertido, legal, outros já acham intrusivo

### Considerações éticas
  - Implações legais e sociais são incertas e em fluxo constante, devido a velocidade que a disciplina evolui.
    - Cautela na análise dos dados para se ter certeza que não está quebrando nenhuma lei, violando termos de serviço ou acordo de uso de dados, abusando da confiança ou violando a privacidade de cliente ou do público.
    - O *lema* informal do Google, que é a empresa que mais coleta dados de individuos que qualquer outra, é **Don't be evil**
  - Certas juridisções impedem de usar dados raciais, étnicos, religiosos ou de qualquer outra *classe protegida* para questões comerciais
    - Porem excluindo esses dados da sua analise as vezes não é suficiente, algoritmos de *ML* podem **sem querer** aprender essas informações.
    - EX: Um certo segmento é composto de pessoas que moram em uma região específica, comprar um certo produto ou se comportam de uma maneira que as identifica como um grupo, um algoritmo de *ML* poderá inferir informação protegida a partir de informação aparentemente inofensiva.
      - Nesse caso as pessoas deverão ser *de-identificadas*, atráves da exclusão de dados que a possam identificar em adição dos dados protegidos
  - O uso dos dados de seus clientes poderá *machucar* ou até mesmo *assustar* seus clientes, casos seus dados pessoais se tornem públicos.
  - Várias aplicações-web notórias sofreram um *exodo massivo* depois que seus usuários se sentiram explorados, quando seus *termos de serviço* mudaram e seus dados eram utilizados para objetivos além do que os usuários inicialmente concordaram. ***FALTA FONTES***
  - É importante considerar a relação da sua *user-base* com privacidade de seus dados antes de começar o seu projeto.
  - "The fact that you *can* use data for a particular end does not
always mean that you *should*."

## Como máquinas aprendem?
  - "Uma máquina é dita que aprende se ela é capaz de adiquirir experiência e a utilizar de forma que melhore sua performance em experiências similares no futuro" - Tom M. Mitchell
  - Processo de aprendizado é semelhante ao de humanos:
    1. Entrada de dados: Utiliza-se observação, armazenamento em memória e "relembrar" parar prover uma base parcial para melhor entendimento
    2. Abstração: Tradução de dados em representações mais amplas
    3. Generalização: Utiliza dados abstratos como base para uma ação
    - O processo é intrisecamente ligado. Apesar de serem divididos em 3 passos, é impossível dizer que um funcionaria sem o outro.
    - Isso não é uma coisa ruim (a divisão nas máquinas), já que o processo é transparente e o conhecimento aprendido pode ser examinado e utilizado para futas ações.
    - Em humanos esse processo acontece subcoscientemente
  - **~historinha da ultima vez que estudou**
  - Não se trata de aprender todas as respostas e sim aprender o padrão das respostas, uma vez que o primeiro é uma estratégia insustentável

### Abstração e representação de conhecimento
  - Representação de dados de entradas *crus* em um formato estruturado é uma tarefa essencial para um algoritm de aprendizado. Esse trabalho acontece no processo de **abstração**.
  - **Representação de conhecimento**: Saber que uma representação de alguma coisa não é a coisa real, é apenas uma *sugestão* de que a sua representação é conectada a esta coisa.
    - **~história do cachimbo**
    - formação de estruturas lógicas que tornam informação sensorial em conhecimento com valor.
  - Durante o processo de **representação do conhecimento**, o computador transforma dados de entrada em um modelo, que é uma definição explicita dos padrões estruturados em dados. Exemplos disso são equações, diagramas (como arvores e grafos), regras lógicas (if, else), grupos de dados (chamados de *clusters*).
    - A escolha do modelo é ditada pela tarefa de aprendizado e o tipo de dado em análise.
  - O processo de *encaixar* um modelo em um conjunto de dados é chamado de **treinamento**
    - ***~explicação de porquê TREINAR e não APRENDER~***
    - **~exemplo descobrimento da gravidade**
  - Maioria dos modelos não resulta no desenvolvimento de teorias que irão abalar a comunidade cientifica atráves dos anos, porém ele poderá descobrir relações entre dados diferentes. As relações, assim como na gravidade, sempre existiram, porém não estava discriminadas e explicitas.
    - psychologists might identify a combination of characteristics indicating a new disorder

### Generalização
  - O processo de aprendizado não está concluído enquanto o aprendiz não pode utilizar seus conhecimentos abstratos para futuras ações.
  - **Generalização** descreve o processo de transformar conhecimento abstrato em um formulario para ser utilizado para realizar ações.
  - É um processo vago e difícil de se descrever.
   - Tradicionalmente *(o processo de generalização)* é imaginado como uma busca em um conjunto de modelos (isto é, teorias) que puderam ser abstraidas durante o treinamento.
   - se você imaginar um conjuneto hipotético contendo todos as teorias possívels que puderam ser obtidas dos dados, **generalização** generalização envolve a redução do conjunto em um número administrável de achados importantes.
   - Não é muito prático reduzir o número de potenciais conceitos os analisando um-a-um para determinar qual é o mais útil. Ao invés disso algoritmos de *ml* gerealmente empregam atalhos que dividem o conjunto de conceitos. Por esse meio o algoritmo irá utilizar eurísticas, ou "estimativas educadas" de onde achar os conceitos mais importantes.
    - Heurísticas utilizam aproximações e outras regras, e não é garantido que se vai achar um conjunetoasd ótimo de coneitos que modelam os dados. Porém é necessário utilizar esses *atalhos* se não achar informações em um conjunto de dados muito grande seria impraticável.
  - Heurística (computador) = Instinto (humano)
    - Lembrar de um resultado de um evento atráves de experiência;
    - A avalibilidade de heurística pode ajudar a explicar o porquê as pessoas tem mais medo de viajar de avião do que de viajar de carro, mesmo carros sendo estatisticamente mais perigosos.
      - Acidente de aviões são traumatizantes e noticiados pelos jornais que acidente de carros.
  - Falhas de heurística não acontecem apenas com humanos.
    - *Gambler's fallacy*
    - Heurísticas aplicadas por algoritEu tô sussaonados sobre uma linha (boca). O algoritmo vai ter problema em achar rostos que não estejam de acordo com esse modelo, como óculos, viradas em um ângulo diferente, de lado ou com tons de pele mais escuro, ou com cor de olhos mais claros.
      - A *tendência* nem sempre é algo ruim. É muito difícil escolher em um grupo com elementos diferentes sem um certo tipo de tendência para te ajudar.

### Avaliando o sucesso do aprendizado
  - Tendência é um mal necessário;
  - Todo mundo tem suas fraquezas e é tendencioso de uma maneira particular (para pensar);
  - Não existe um super-modelo que irá funcionar para todos os casos;
  - **O passo final da generlização é determinar o sucesso do modelo apesar de suas tendências**
  - Falha dos modelos associada ao problema de *ruído* (noise) ou variações inexplicáveis nos dados:
    - sensores imprecisos;
    - problemas com dados de relatórios, como usuários que respondem qualquer coisa para terminar logo;
    - dados corrompidos;
    - Modelar o ruído nos dados é a base de um problema chamado de **Overfitting** (sobre ajustação (?)).
      - Ruído é inexplicável por definição, e tentar explicá-lo irá resultar em conclusões erroneas.
      - Tentar gerar teorias que expliquem o ruído resulta em modelos mais complexos que ignoram o o padrão que se quer identificar;
    - Um modelo que roda bem em treinamento mas tem performance ruim durante treinamento é chamado de **overfitted** para a base de dados de treinamento pois ele não generaliza bem.
    - Problemas de **overfitting** são especificos para cada tipo de aproximação de *machine learning*

## PASSOS PARA APLICAR MACHINE LERANING EM SEUS DADOS
1. Coletar dados
2. Explorar e preparar os dados
  - A qualidade de um projeto de *machine learning* está associado a qualidade dos dados que serão utilizados;
3. Treinar o modelo nos dados
4. Avaliar a performance do modelo
5. Melhorar a performance do modelo
