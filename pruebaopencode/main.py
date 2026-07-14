import pandas as pd


def load_games_from_json():
    # Cargar el fichero JSON de juegos
    file_path = 'data/mejores_juegos.json'
    try:
        df = pd.read_json(file_path)
        print(df)  # Imprimir el DataFrame por consola
        return df
    except Exception as e:
        print(f'Error al cargar el archivo: {e}')
        return None


if __name__ == '__main__':
    load_games_from_json()