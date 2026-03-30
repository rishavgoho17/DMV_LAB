import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("covid_dataset.csv")

# ---------- BAR CHART ----------

city_counts = df['City'].value_counts()

plt.figure()
plt.bar(city_counts.index, city_counts.values)
plt.title("Number of People by City")
plt.xlabel("City")
plt.ylabel("Count")
plt.show()


# ---------- STAIR CHART ----------
df = df.sort_values(by="Age")

plt.figure()

plt.step(df["Age"], df["Fever"], where='mid')

plt.title("Stair Chart: Age vs Fever")
plt.xlabel("Age")
plt.ylabel("Fever Temperature")

plt.show()


# ---------- LINE CHART ----------
df = df.sort_values(by="Age")

plt.figure()

plt.plot(df["Age"], df["Fever"], marker='o')

plt.title("Line Chart: Age vs Fever")
plt.xlabel("Age")
plt.ylabel("Fever Temperature")

plt.show()

# ---------- PIE CHART ----------
gender_counts = df['Gender'].value_counts()

plt.figure()
plt.pie(gender_counts.values, labels=gender_counts.index, autopct='%1.1f%%')
plt.title("Gender Distribution")
plt.show()


# ---------- HISTOGRAM ----------
plt.figure()
plt.hist(df['Age'], bins=10)
plt.title("Age Distribution Histogram")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()