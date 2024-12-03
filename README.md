# North America Cars Dataset (1984–2025)
This repository contains a dataset of North American cars manufactured between 1984 and 2025. The dataset is versatile and can be used for various purposes, including creating vehicle pickers for customers to select specific models via dropdown menus or for general data analysis in the automotive industry.
---
## Dataset Description
The dataset is provided as a CSV file: **`north_america_cars_1984_2025.csv`**.
### **Columns**
- **`cylinders`**: Number of cylinders in the engine.
- **`make`**: Manufacturer of the vehicle (e.g., Toyota, Ford, etc.).
- **`model`**: Specific variant of the vehicle (e.g., Corolla HEV, F-150 XLT).
- **`VClass`**: Vehicle class, such as "car," "truck," "SUV," "sedan," or "van."  
  - **Note**: We did our best to assign accurate vehicle classes. While most vehicles are classified, around 700 rows remain labeled as "Special Purpose Vehicle" and need further refinement.
- **`year`**: Year the vehicle was manufactured.
- **`baseModel`**: Base designation of the model (e.g., Corolla, F-150).
- **`atvType`**: Indicates the type of ATV (if applicable).
---
## Features and Notes
1. **Vehicle Class**:  
   The dataset includes the primary vehicle classes: *car, truck, SUV, sedan, and van*. While we manually classified most vehicles, approximately 700 rows remain unclassified ("Special Purpose Vehicle") and would benefit from contributions to refine these entries.
2. **Duplicates Removed**:  
   We cleaned the dataset by removing duplicate entries.
3. **Base Model vs. Model**:  
   The `baseModel` column represents the general model name (e.g., Corolla), while the `model` column provides the specific variant (e.g., Corolla HEV, Corolla XSE).
4. **Added Original `vehicles.csv`**:  
   We have added the original **`vehicles.csv`** file from [FuelEconomy.gov](https://www.fueleconomy.gov/feg/download.shtml) to this repository. This file is provided as a copy for users who prefer to perform their own data cleaning or analysis. Feel free to modify and adapt the data to suit your needs. Both the cleaned **`north_america_cars_1984_2025.csv`** and the unaltered **`vehicles.csv`** are now available in the repository, giving you flexibility in how you work with the data.
---
## How to Use
This dataset can be loaded and explored using tools like Python and pandas. Below is an example:
```python
import pandas as pd
# Load the dataset directly from the GitHub repository
url = "https://raw.githubusercontent.com/WaryaWayne/north-america-cars-dataset/refs/heads/master/north_america_cars_1984_2025.csv"
df = pd.read_csv(url)
# Display the first few rows
print(df.head())
```
## License
This dataset is provided under the MIT License.
Credit is appreciated. Contributions, especially for refining the remaining unclassified rows, are welcome!
## Acknowledgments
Special thanks to FuelEconomy.gov for providing the original dataset that formed the basis of this resource.