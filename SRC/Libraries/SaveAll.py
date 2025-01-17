from Libraries import SaveMultiPersonToDatabase, SaveWeaponsToDatabase, Database
def save_everything():
    Database.reset_table()
    SaveWeaponsToDatabase.save_all()
    SaveMultiPersonToDatabase.save_all()