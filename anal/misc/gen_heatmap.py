
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

infile = '~/Documents/SHINRA/2021-LinkJP/mention_gold_distance.tsv'
gtitle = 'mention_gold_distance'
outfile = '~/Documents/SHINRA/2021-LinkJP/mention_gold_distance_heatmap.png'

df = pd.read_csv(infile, delimiter='\t', names=('cat_attr', 'distance',  'freq'))
print(df)
sns.set(style='darkgrid')
tmp_df_heat = df.pivot('cat_attr', 'distance', 'freq')
print(tmp_df_heat)
sns.heatmap(df, annot=True, cmap="Blues", cbar=False).set(title=gtitle)
plt.savefig(outfile, bbox_inches='tight', pad_inches=0)
