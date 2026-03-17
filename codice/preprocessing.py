import pandas as pd
import os
from abc import ABC, abstractmethod

# --- 1. DEFINIZIONE DELLA FACTORY ---

class AbstractOpener(ABC):
    def open(self, dataframe_path: str) -> pd.DataFrame:
        if not os.path.exists(dataframe_path):
            raise FileNotFoundError(f"File {dataframe_path} non trovato")
        try:
            return self._load_data(dataframe_path)
        except Exception as e:
            raise RuntimeError(f"Errore durante la lettura del file {dataframe_path}: {e}")

    @abstractmethod
    def _load_data(self, path: str) -> pd.DataFrame:
        pass

class XLSOpener(AbstractOpener):
    def _load_data(self, path: str) -> pd.DataFrame:
        return pd.read_excel(path)

class CSVOpener(AbstractOpener):
    def _load_data(self, path: str) -> pd.DataFrame:
        return pd.read_csv(path)

class JSONOpener(AbstractOpener):
    def _load_data(self, path: str) -> pd.DataFrame:
        return pd.read_json(path)

def scegli_opener(dataframe_path: str) -> AbstractOpener:
    ext = dataframe_path.split('.')[-1].lower()
    match ext:
        case 'csv' | 'txt':
            return CSVOpener()
        case 'xls' | 'xlsx':
            return XLSOpener()
        case 'json':
            return JSONOpener()
        case _:
            raise RuntimeError(f"Tipo di file non supportato: {ext}")

# --- 2. CLASSE PREPROCESSING ---

class Preprocessing:
    """
    Classe incaricata della pulizia e preparazione del dataset.
    Riceve il dataframe già unito e restituisce il dataframe processato.
    """
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.df = dataframe.copy()

    def esegui(self) -> pd.DataFrame:
        """
        Punto di ingresso per tutte le operazioni di pulizia.
        """
        # Qui in futuro chiamerai i metodi di pulizia:
        self.df = self.elimina_duplicati(self.df)
        return self.df

        # Metodo per eliminare duplicati
    def elimina_duplicati(self, dati):
        dati = dati.drop_duplicates()
        # Riassegna gli indici dopo l'eliminazione
        dati = dati.reset_index(drop=True)
        return dati

# --- 3. MAIN SCRIPT ---

current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, '..', 'data')

try:
    path_values = os.path.join(data_dir, 'train_values.csv')
    path_labels = os.path.join(data_dir, 'train_labels.csv')

    # CARICAMENTO
    print("Caricamento file in corso...")
    train_values = scegli_opener(path_values).open(path_values)
    train_labels = scegli_opener(path_labels).open(path_labels)

    # MERGE
    train_full = train_values.merge(train_labels, on='building_id')
    print(f"File caricati e uniti. Righe totali: {train_full.shape[0]}")

    # PREPROCESSING
    preprocessor = Preprocessing(train_full)
    df_processato = preprocessor.esegui()

    print("\n--- RESOCONTO FINALE ---")
    print(f"Dimensioni Righe: {df_processato.shape[0]}")
    print(f"Dimensioni Colonne:  {df_processato.shape[1]}")
    print(f"Valori mancanti residui: {df_processato.isnull().sum().sum()}")

except Exception as e:
    print(f"Errore: {e}")