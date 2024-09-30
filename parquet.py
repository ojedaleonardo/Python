import pandas as pd

# Configurar Pandas para mostrar todo el contenido sin recortar
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Leer archivo Parquet usando PyArrow
df = pd.read_parquet('/home/leonardo/00c8e3027116157de26bb495408e017f.gz.parquet', engine='pyarrow')

print(df)
