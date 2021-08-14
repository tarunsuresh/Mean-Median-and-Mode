import statistics
import pandas as pd

df=pd.read_csv("SOCR-HeightWeight.csv")
data=df["Weight(Pounds)"]

mean=statistics.mean(data)
mode=statistics.mode(data)
median=statistics.median(data)

print("mean is :"+str(mean))
print("mode is :"+str(mode))
print("median is :"+str(median))

