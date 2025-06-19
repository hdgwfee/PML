import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os

parser = argparse.ArgumentParser(description='Analyze Umsatz data from a CSV file.')
parser.add_argument('csv_file', type=str, nargs='?', default='/home/safran/Desktop/pml/CSV/umsatz.csv', help='Path to the Umsatz CSV file')
args = parser.parse_args()

umsatz_df = pd.read_csv(args.csv_file)
umsatz_pro_abteilung = umsatz_df.groupby('Abteilung')['Umsatz'].sum()
top_5_abteilungen = umsatz_pro_abteilung.sort_values(ascending=False).head(5)
top_5_abteilungen.plot(kind='bar')
plt.title('Top 5 Abteilungen nach Umsatz')
plt.xlabel('Abteilung')
plt.ylabel('Umsatz')
plt.xticks(rotation=45)
plt.tight_layout()

output_dir = '/home/safran/Desktop/pml/CSV'
plt.savefig(os.path.join(output_dir, 'umsatz_balkendiagramm.png'))
plt.show()
top_5_abteilungen.to_csv(os.path.join(output_dir, 'auswertung.csv'))
plt.savefig(os.path.join(script_dir, 'umsatz_balkendiagramm.png'))
plt.show()
top_5_abteilungen.to_csv(os.path.join(script_dir, 'auswertung.csv'))
