# DPSGRAPHERLIBRARY

**DPSGRAPHERLIBRARY** is a Python library designed to accurately calculate and visualize Damage Per Second (DPS) for various weapons in the game Destiny 2. It outputs the DPS data into an Excel file, enabling users to create detailed graphs for analysis.

## Description

This library calculates DPS using the following methodology:
- **Damage Data Source:** Damage values are sourced from boss knights in the Legendary Witch Queen Mission: The Investigation.
  ![The Boss Knights](https://github.com/carterdr/DPSGRAPHERLIBRARY/assets/113926029/af30bec6-d400-4c3e-9b88-f38b8811381c)
- **Recording Methodology:** Damage recording is based on 60 fps gameplay and analyzed using a 60 fps recording.
- **Assumptions:**
  -   All reload times are calculated assuming the use of Lunafaction Boots and a reload speed mod.
  -   Surges are always applied to the base damage of a weapon in the code. It is up to your to handle surges with non matching elements.
  -   All damage values assume boss spec if possible.
- **Output:** The library prints unique damage values and timestamps to the console and populates an Excel file for graph plotting. It covers the first 100 seconds of weapon damage.
  ![Final Graph Example](https://github.com/carterdr/DPSGRAPHERLIBRARY/assets/113926029/3b7c98be-1a8c-4370-ba39-13c6c6edc996)



## Getting Started

### Dependencies

- **Python 3**
- **openpyxl**: A Python library for reading/writing Excel 2010 xlsx/xlsm files.
  - Installation: Run `pip install openpyxl` in your terminal.

### Installation

- Clone or download the repository from GitHub.

### Usage

1. **Navigate to the SRC Folder:** The `SRC` folder contains the primary script `Runner.py` with all necessary imports.
2. **Running the Script:** 
   - For single weapon DPS calculation, instantiate the weapon class and call `printDPS()`.
   - For multiple weapons, chain the `printDPS()` method calls, passing the appropriate parameters.
3. **Output File:** The results are written to `DPS.xlsx`. Ensure this file is closed before running the script.
4. **Data Visualization:** Transfer the data to a permanent spreadsheet and create a line chart with time on the x-axis for visualization.

#### Examples

```python
# Single Weapon Example
crux = Rockets.Crux()
crux.printDps(1.25)

# Multiple Weapons Example
crux = Rockets.Crux()
col = crux.printDps(1.25)
cloud = Snipers.CloudStrike()
cloud.printDps(1.25, "Cloudstrike", crux.damage_times, placeInColumn=col)
```
## Customization

To customize DPSGRAPHERLIBRARY for your specific needs, you can modify the parameters for each weapon class. The library is designed to be flexible, allowing changes to various aspects of DPS calculation. For more advanced customizations, refer to the documentation within each weapon's class.

## Version History

- **1.0**
  - Initial Release.
  - Features include:
    - DPS calculation for various weapons in Destiny 2.
    - Excel output for data visualization.
    - Documentation for each weapon class.

## Help

If you encounter issues or have questions regarding the usage of DPSGRAPHERLIBRARY, please follow these steps for assistance:

1. **Check the Documentation:** Most common issues and usage instructions are covered in the in-class documentation.
2. **Open an Issue:** If you can't find the answer in the documentation, open an issue on GitHub detailing the problem. Please provide as much detail as possible to help us understand and address the issue quickly.
3. **Community Support:** You can also seek help from the community by posting your query in relevant forums or discussion groups.
