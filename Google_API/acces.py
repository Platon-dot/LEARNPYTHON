import httplib2 
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials	
spreadsheetId = "1uXPmptPKzy_tWXIEzi6OaWbAg1GhVWS2nUqyAdeN2e4"

driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth) # Выбираем работу с Google Drive и 3 версию API
access = driveService.permissions().create(
    fileId = spreadsheetId,
    body = {'type': 'user', 'role': 'writer', 'emailAddress': 'ambalexey@gmail.com'},  # Открываем доступ на редактирование
    fields = 'id'
).execute()

