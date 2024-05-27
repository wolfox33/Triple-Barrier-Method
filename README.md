# Triple Barrier Method
Triple Barrier é uma técnica de gerenciamento de risco e definição de eventos de trading, introduzida por Marcos López de Prado em seu livro "Advances in Financial Machine Learning".
Ele envolve a definição de três barreiras: um nível superior, um nível inferior e uma barreira de tempo. A posição é encerrada quando um desses três níveis é atingido.

Triple Barrier Method com ATR para Dados OHLC
Este projeto implementa o método Triple Barrier para definir sinais de compra e venda em dados OHLC (Open, High, Low, Close) utilizando o ATR (Average True Range) para definir as barreiras dinâmicas de lucro e perda.

Descrição
O método Triple Barrier é uma técnica de gerenciamento de risco e definição de eventos de trading que utiliza três barreiras para determinar o momento de entrada e saída de trades: uma barreira de lucro, uma barreira de perda e uma barreira de tempo. Neste projeto, as barreiras de lucro e perda são definidas como múltiplos do ATR, adaptando-se assim à volatilidade do mercado.

Funcionalidades
Cálculo do ATR: Calcula o Average True Range (ATR) para um determinado período.
Definição de Barreiras: Define barreiras dinâmicas de lucro e perda com base no ATR.
Geração de Sinais: Gera sinais de compra e venda utilizando o método Triple Barrier.

Uso
Pré-requisitos
Python 3.x
Pandas
Numpy


##Contribuição
Sinta-se à vontade para abrir issues e pull requests para melhorar este projeto.