import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import re


df = pd.read_csv("company_dataset.csv")



df['review_count'] = df['review_count'].str.replace('[(),Reviews ]','', regex=True)
df['review_count'] = df['review_count'].str.replace('k','000')
df['review_count'] = df['review_count'].astype(float)


df['years'] = df['years'].str.extract('(\d+)').astype(int)



print("\nHeadquarters of First 10 Companies:\n")
for i in range(10):
    print(df.loc[i,'name'], ":", df.loc[i,'hq'])



emp_counts = df['employees'].value_counts()

plt.figure(figsize=(7,7))
plt.pie(emp_counts.values, labels=emp_counts.index, autopct='%1.1f%%')
plt.title("Companies Distribution by Employees")
plt.grid(True)
plt.show()



plt.figure(figsize=(10,6))
plt.bar(df['name'][:10], df['ratings'][:10])
plt.title("Company Ratings")
plt.xlabel("Companies")
plt.ylabel("Ratings")
plt.xticks(rotation=60)
plt.grid(True)
plt.show()



plt.figure(figsize=(10,6))
plt.plot(df['name'][:10], df['years'][:10], marker='o')
plt.title("Company Age (Years)")
plt.xlabel("Companies")
plt.ylabel("Years")
plt.xticks(rotation=60)
plt.grid(True)
plt.show()


top_reviews = df.sort_values(by='review_count', ascending=False).head(10)

fig = px.funnel(top_reviews,
                x='review_count',
                y='name',
                title="Company Reviews Funnel")

fig.show()