# Dropbox justin_personal_wedding
import dropbox
token = "SJ_XC7jen80AAAAAAAAKtahSwGAh8Fxjk0nmeaSpPoAgt5d-rsW0u3YBtB-dSmMt"
dbx = dropbox.Dropbox(token)
dbx.users_get_current_account()

prep = dbx.files_list_folder("/PRÉPARATIFS")
mariage = dbx.files_list_folder("/MARIAGE")

prep_url = []
for i in prep.entries:
    prep_url.append(dbx.sharing_create_shared_link(i.path_display).url)

mariage_url = []
for i in prep.entries:
    mariage_url.append(dbx.sharing_create_shared_link(i.path_display).url)

couple_reception_url = []
for i in prep.entries:
    couple_reception_url.append(dbx.sharing_create_shared_link(i.path_display).url)    
