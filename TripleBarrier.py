import pandas as pd
import numpy as np

# Calcular o ATR
def calculate_atr(df, window):
    high_low = df['high'] - df['low']
    high_close = np.abs(df['high'] - df['close'].shift())
    low_close = np.abs(df['low'] - df['close'].shift())
    true_range = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    atr = true_range.rolling(window=window, min_periods=1).mean()  # Usando média móvel simples
    return atr

# Função para aplicar as barreiras com base no ATR
def apply_triple_barrier_atr(df, atr, atr_multiplier, holding_period):
    signals = []
    for idx in range(len(df)):
        start_price = df['close'].iloc[idx]
        profit_barrier = atr_multiplier * atr[idx]/start_price
        loss_barrier = -atr_multiplier * atr[idx]/start_price
        
        signal = 0
        for i in range(0, holding_period + 1):
            if idx + i >= len(df):
                break
            current_price = df['close'].iloc[idx + i]
            price_change = (current_price - start_price) / start_price
            
            if price_change >= profit_barrier:
                signal = 1  # Sinal de compra
                break
            elif price_change <= loss_barrier:
                signal = -1  # Sinal de venda
                break
        
        signals.append(signal)
    
    return signals

# Definir os parâmetros
window = 14  # Período do ATR
atr_multiplier = 0.5  # Multiplicador do ATR para definir as barreiras
holding_period = 1  # Período de retenção

# Calcular o ATR e aplicar a função ao DataFrame
df['ATR'] = calculate_atr(df, window)
df['signal'] = apply_triple_barrier_atr(df, df['ATR'], atr_multiplier, holding_period)

# Analisar os sinais
print(df[['close', 'ATR', 'signal']])
