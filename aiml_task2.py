import matplotlib.pyplot as plt
import pandas as pd

# Load the data into a DataFrame
data = pd.read_csv(r"C:\Users\LENOVO\Desktop\aiml\Steel_industry_data.csv", encoding='latin1')

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(data['Leading_Current_Reactive_Power_kVarh'], data['NSM'])
plt.xlabel('Leading_Current_Reactive_Power_kVarh')
plt.ylabel('NSM')
plt.title('NSM in the Steel Industry Over the Leading_Current_Reactive_Power_kVarh')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the visualization as an image or display it
plt.savefig('steel_industry_Leading_Current_Reactive_Power_kVarh_in_NSM.png')
plt.show()
