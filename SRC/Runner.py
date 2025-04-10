
from Libraries.utils.Excel import prepare_sheet, display_data, print_to_sheet
from Libraries.database.SaveAll import save_everything
from Libraries.database.SaveWeaponsToDatabase import calculate_abilities
from Libraries.weapons import *
from Libraries.abilities import *



prepare_sheet(clear_sheet=True)
save_everything()
display_data()



