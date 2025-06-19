import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os

parser = argparse.ArgumentParser(description='ernehrungs data von der csv Analyseiren')
parser.add_argument('csv_file', type=str, nargs='?', default='/home/safran/Desktop/pml/CSV/ernaehrung.csv', help='Pathzur  CSV')
args = parser.parse_args()

ernaehrung_df = pd.read_csv(args.csv_file)
proteinreiche_gerichte = ernaehrung_df[ernaehrung_df['Protein'] > 20]
kalorienarme_gerichte = proteinreiche_gerichte.sort_values('Kalorien').head(3)
print("drei kalorienärmsten Gerichte  mehr als 20g Protein:")
print(kalorienarme_gerichte)

plt.figure(figsize=(8, 8))
plt.pie(proteinreiche_gerichte['Protein'], labels=proteinreiche_gerichte['Gericht'], autopct='%1.1f%%', startangle=140)
plt.title('Proteingehalt Gerichte (über 20g Protein)')
plt.tight_layout()

output_dir = '/home/safran/Desktop/pml/CSV'
plt.savefig(os.path.join(output_dir, 'proteingehalt.png'))
plt.show()

plt.title('Proteingehalt über 20g Protein')
plt.tight_layout()


output_dir = '/home/safran/Desktop/pml/CSV'
plt.savefig(os.path.join(output_dir, 'proteingehalt.png'))


