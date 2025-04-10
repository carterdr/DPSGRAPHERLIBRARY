# Damage Simulation Tool

This project simulates damage over time using a modular system of weapons, abilities, and simulation parameters. Results are able to be exported to a Google Cloud Database or Excel files and graphed.

### Project Structure
Brief overview:
```
📁 SRC/
├── Libraries/             
│   ├── abilities/         # Ability implementations
│   ├── database/          # Database interaction logic and python files to run all calculations
│   ├── models/            # Core simulation models and result representations
│   ├── utils/             # Helper files like config, Excel export, constants
│   └── weapons/           # Weapon type logic and damage implementations
├── Runner.py              # Main script to run simulation
├── DPS.xlsx               # Output excel file for Damage Per Second
```
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
  ![Final Graph Example](https://github.com/carterdr/DPSGRAPHERLIBRARY/assets/113926029/7131c2f8-d6a8-4255-a651-a5bf12b6523c)




## Getting Started

### Installation
```bash
git clone <your-repo>
cd <your-repo>
pip install -r requirements.txt
```
(You can generate `requirements.txt` via `pip freeze > requirements.txt`)


### Database setup
#### Setup .env file in root directory
```
MONGO_URI
DB_NAME
COLLECTION_NAME
```
#### Setup key.json file in root directory


### Usage
# Basic usage
python Runner.py

# Ensure the config in `utils/config.py` is set correctly before running.

#### Examples
- Each calculate() call returns a DamageResult.
- The DamageResult can be saved to the database with DamageResult().save()
- The Damage Result can be printed to the excel sheet with print_to_sheet(DamageResult())

# Single Weapon Example
```python
ExoticPrimaries.ChoirOfOne(out_of_range=False).calculate()
```

# Multiple Weapons Example
```python
x = Rockets.Ghally().calculate()
x.add(FusionRifles.Cartesian().calculate(prev_result=x))
```
# Saving to the Database
```python
ExoticPrimaries.ChoirOfOne(out_of_range=False).calculate().save()
```

# Printing to the excel sheet
```python
print_to_sheet(FusionRifles.Cartesian().calculate())
```

# Setting up the sheet
```python
prepare_sheet(clear_excel=True) # Clears the sheet and creates the time column
display_data() # Displays the data in the sheet using matplotlib
```
