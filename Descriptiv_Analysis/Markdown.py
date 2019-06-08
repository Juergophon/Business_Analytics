import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df_features = pd.read_csv('features.csv')
df_features = df_features.sort_values('Date', ascending=True)

df_store10 = df_features[df_features['Store'].isin([10,23, 30])]

fig, axes = plt.subplots(nrows=5, ncols=1, sharex=True, figsize=(10,7))
ax1 = df_store10.groupby(['Date', 'Store']).sum()['MarkDown1'].unstack().plot(linewidth=0.7, ax=axes[0], title='Markdown 1')
ax1.legend('')
ax1.title.set_size('8')
ax2 = df_store10.groupby(['Date', 'Store']).sum()['MarkDown2'].unstack().plot(linewidth=0.7, ax=axes[1], title='Markdown 2')
ax2.legend('')
ax2.title.set_size('8')
ax3 = df_store10.groupby(['Date', 'Store']).sum()['MarkDown3'].unstack().plot(linewidth=0.7, ax=axes[2], title='Markdown 3')
ax3.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=6)
ax3.title.set_size('8')
ax4 = df_store10.groupby(['Date', 'Store']).sum()['MarkDown4'].unstack().plot(linewidth=0.7, ax=axes[3], title='Markdown 4')
ax4.legend('')
ax4.title.set_size('8')
ax5 = df_store10.groupby(['Date', 'Store']).sum()['MarkDown5'].unstack().plot(linewidth=0.7, ax=axes[4], title='Markdown 5')
ax5.legend('')
ax5.title.set_size('8')

# format axes
plt.xticks(fontsize=6)

plt.show()