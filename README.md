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
Instalação
Clone o repositório e instale as dependências necessárias:

sh
Copiar código
git clone https://github.com/seu-usuario/triple-barrier-atr.git
cd triple-barrier-atr
pip install pandas numpy
Executando o Código
Carregar os dados OHLC:

python
Copiar código
df = pd.read_csv('seu_arquivo_ohlc.csv', index_col='Date', parse_dates=True)
Calcular o ATR:

python
Copiar código
def calculate_atr(df, window):
    high_low = df['High'] - df['Low']
    high_close = np.abs(df['High'] - df['Close'].shift())
    low_close = np.abs(df['Low'] - df['Close'].shift())
    true_range = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    atr = true_range.rolling(window=window, min_periods=1).mean()
    return atr
Aplicar o Método Triple Barrier com ATR:

python
Copiar código
def apply_triple_barrier_atr(df, atr, atr_multiplier, holding_period):
    signals = []
    for idx in range(len(df)):
        start_price = df['Close'].iloc[idx]
        profit_barrier = atr_multiplier * atr[idx]
        loss_barrier = -atr_multiplier * atr[idx]
        
        signal = 0
        for i in range(1, holding_period + 1):
            if idx + i >= len(df):
                break
            current_price = df['Close'].iloc[idx + i]
            price_change = (current_price - start_price) / start_price
            
            if price_change >= profit_barrier:
                signal = 1  # Sinal de compra
                break
            elif price_change <= loss_barrier:
                signal = -1  # Sinal de venda
                break
        
        signals.append(signal)
    
    return signals
Executar a Análise:

python
Copiar código
window = 14  # Período do ATR
atr_multiplier = 1.5  # Multiplicador do ATR para definir as barreiras
holding_period = 10  # Período de retenção

# Calcular o ATR e aplicar a função ao DataFrame
df['ATR'] = calculate_atr(df, window)
df['signal'] = apply_triple_barrier_atr(df, df['ATR'], atr_multiplier, holding_period)

# Analisar os sinais
print(df[['Close', 'ATR', 'signal']])
Contribuição
Sinta-se à vontade para abrir issues e pull requests para melhorar este projeto.