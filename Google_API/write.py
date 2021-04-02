import httplib2 
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials	
spreadsheetId = "1uXPmptPKzy_tWXIEzi6OaWbAg1GhVWS2nUqyAdeN2e4"

CREDENTIALS_FILE = 'credentials.json'  # Имя файла с закрытым ключом, вы должны подставить свое

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth) # Выбираем работу с таблицами и 4 версию API 


# Добавление листа
results = service.spreadsheets().batchUpdate(
    spreadsheetId = spreadsheetId,
    body = 
{
"requests": [
    {
    "addSheet": {
        "properties": {
        "title": "Еще один лист",
        "gridProperties": {
            "rowCount": 20,
            "columnCount": 12
        }
        }
    }
    }
]
}).execute()


# Получаем список листов, их Id и название
spreadsheet = service.spreadsheets().get(spreadsheetId = spreadsheetId).execute()
sheetList = spreadsheet.get('sheets')
for sheet in sheetList:
    print(sheet['properties']['sheetId'], sheet['properties']['title'])
    
sheetId = sheetList[0]['properties']['sheetId']

print('Мы будем использовать лист с Id = ', sheetId)