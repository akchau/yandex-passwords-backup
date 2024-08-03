import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Use the JSON key you've downloaded
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/glaz/Загрузки/client_secret_283706753417-nqcle4ttjaeq8m72d1rin7kfnu6ql2qk.apps.googleusercontent.com.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
sheet = client.open("Пароли").sheet1

# Get all records of the data
records = sheet.get_all_records()

# Convert dict to DataFrame
data = pd.DataFrame.from_records(records)

# To download as CSV
data.to_csv('/home/glaz/yandex-password-backup/temp_data/google-password.csv')

print(data)