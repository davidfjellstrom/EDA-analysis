import pandas as pd
from rich.table import Table
from rich.console import Console

df = pd.read_csv('data/messy_IMDB_dataset.csv', sep=';')

console = Console()
table = Table(show_header=True, header_style="bold magenta")

for col in df.columns:
    table.add_column(col)

for _, row in df.iterrows():
    table.add_row(*[str(v) for v in row])

console.print(table)