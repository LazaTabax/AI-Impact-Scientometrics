import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Read data
dfAllAlt = pd.read_csv('Altmetrics/AllAlt.tsv', sep='\t', header=0)
df = dfAllAlt[['CitationCount','Score','GroupType']]

# Apply logarithmic scale and norm both metrics to 1
df['CitationCount'] = np.log(df['CitationCount']+1)
df['Score'] = np.log(df['Score']+0.75)
df.rename(columns={ 'Score':'Altmetric Score', 'CitationCount':'Citation Count', 'GroupType': 'Group Type'}, inplace = True)


# Calculated in zones, to be able to isolate Exceptionals, Influencers and Scholars
df1 = df.loc[(df['Citation Count']>=np.log(43)) & (df['Altmetric Score']>=np.log(9)),]
print(  'Exceptionals: ',
        len(df1[df1['Group Type']=='Education'].index)/len(df[df['Group Type']=='Education'].index),
        len(df1[df1['Group Type']=='Company'].index)/len(df[df['Group Type']=='Company'].index),
        len(df1[df1['Group Type']=='Cooperation'].index)/len(df[df['Group Type']=='Cooperation'].index)
    )
df2 = df.loc[(df['Citation Count']<=np.log(3)) & (df['Altmetric Score']>=np.log(9)),]
print(  'Influencers: ',
        len(df2[df2['Group Type']=='Education'].index)/len(df[df['Group Type']=='Education'].index),
        len(df2[df2['Group Type']=='Company'].index)/len(df[df['Group Type']=='Company'].index),
        len(df2[df2['Group Type']=='Cooperation'].index)/len(df[df['Group Type']=='Cooperation'].index)
    )
df3 = df.loc[(df['Citation Count']>=np.log(43)) & (df['Altmetric Score']<=np.log(1.5)),]
print(  'Scholars: ',
        len(df3[df3['Group Type']=='Education'].index)/len(df[df['Group Type']=='Education'].index),
        len(df3[df3['Group Type']=='Company'].index)/len(df[df['Group Type']=='Company'].index),
        len(df3[df3['Group Type']=='Cooperation'].index)/len(df[df['Group Type']=='Cooperation'].index)
    )


# Scatterplot with borders
sns.set(font_scale=2)
plt.figure(figsize =(10, 8))
plt.axvline(x=np.log(1.5), color='black', linestyle='dashed', linewidth=1.5, alpha=0.66)
plt.axvline(x=np.log(9), color='black', linestyle='dashed', linewidth=1.5, alpha=0.66) 
plt.axhline(y=np.log(43), color='black', linestyle='dashed', linewidth=1.5, alpha=0.66)  
plt.axhline(y=np.log(3), color='black', linestyle='dashed', linewidth=1.5)

sns.scatterplot(data=df, x="Altmetric Score", y="Citation Count",  hue="Group Type", palette=['tab:blue','tab:orange','tab:grey']) #, alpha=0.5
sns.scatterplot(data=df1, x="Altmetric Score", y="Citation Count",  hue="Group Type", legend=False, palette=['tab:blue','tab:orange','tab:grey'])
sns.scatterplot(data=df2, x="Altmetric Score", y="Citation Count",  hue="Group Type", legend=False, palette=['tab:blue','tab:orange','tab:grey'])
sns.scatterplot(data=df3, x="Altmetric Score", y="Citation Count",  hue="Group Type", legend=False, palette=['tab:blue','tab:orange','tab:grey'])

plt.legend(loc ='upper left', prop={'size': 17})
plt.ylabel("Citations")
plt.show()

# Calculate the thresholds from above using this line
#print(dfAllAlt['CitationCount'].describe(percentiles=[.2,.8,]), dfAllAlt['Score'].describe(percentiles=[.2,.8]))
