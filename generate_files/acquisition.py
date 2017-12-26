# Dropbox justin_personal_wedding
import dropbox
import pandas
import pickle
token = "SJ_XC7jen80AAAAAAAAKtahSwGAh8Fxjk0nmeaSpPoAgt5d-rsW0u3YBtB-dSmMt"
dbx = dropbox.Dropbox(token)
dbx.users_get_current_account()

prep = dbx.files_list_folder("/PRÉPARATIFS")
mariage = dbx.files_list_folder("/MARIAGE")
couple = dbx.files_list_folder("/COUPLE ET RÉCEPTION/couple")
couple_reception = dbx.files_list_folder("/COUPLE ET RÉCEPTION")

prep_url = []
for i in prep.entries:
    prep_url.append(dbx.sharing_create_shared_link(i.path_display).url)

mariage_url = []
for i in mariage.entries:
    mariage_url.append(dbx.sharing_create_shared_link(i.path_display).url)

couple_reception_url = []
for i in couple_reception.entries:
    couple_reception_url.append(dbx.sharing_create_shared_link(i.path_display).url)

with open("prep_url.txt", "wb") as fp:
	pickle.dump(prep_url, fp)

with open("mariage_url.txt", "wb") as fp:
	pickle.dump(mariage_url, fp)

with open("couple_reception_url.txt", "wb") as fp:
	pickle.dump(couple_reception_url, fp)

with open("couple_reception_url.txt", "rb") as fp:
    b = pickle.load(fp)