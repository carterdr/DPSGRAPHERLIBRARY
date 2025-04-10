from Libraries.database import SaveMultiPersonToDatabase, SaveWeaponsToDatabase, Database
def save_everything():
    Database.drop_dot_collection()
    SaveWeaponsToDatabase.save_all()
    SaveMultiPersonToDatabase.save_all()