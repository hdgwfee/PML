import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os

parser = argparse.ArgumentParser(description='vom csvDie schrite.')
parser.add_argument('csv_file', type=str, nargs='?', default='/home/safran/Desktop/pml/CSV/schritte.csv', help='Path zur CSV ')
args = parser.parse_args()

schritte_df = pd.read_csv(args.csv_file)
schritte_df['Datum'] = pd.to_datetime(schritte_df['Datum'])
lina_df = schritte_df[schritte_df['Name'] == 'Lina']
lina_df['Woche'] = lina_df['Datum'].dt.isocalendar().week
wochendurchschnitt = lina_df.groupby('Woche')['Schritte'].mean()

plt.figure(figsize=(12, 6))
plt.plot(lina_df['Datum'], lina_df['Schritte'])
plt.title('Linas Schrittanzahl  Zeit')
plt.xlabel('Datum')
plt.ylabel('Schritte')
plt.xticks(rotation=45)
plt.tight_layout()

output_dir = '/home/safran/Desktop/pml/CSV'
plt.savefig(os.path.join(output_dir, 'Lina.png'))
plt.show()

aktive_tage = lina_df[lina_df['Schritte'] > 10000]
aktive_tage.to_csv(os.path.join(output_dir, 'aktiv.csv'))
plt.xticks(rotation=45)
plt.tight_layout()




plt.show()


