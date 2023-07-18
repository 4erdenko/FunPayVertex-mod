import time
from pprint import pprint

import googleapiclient.discovery
import httplib2
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials

# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'google_sheets/google/creds.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '1fXd2zQNwP2FHB7ni8fQpyLuNk9jzWXnJw4im8jp9TjA'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive',
    ],
)
httpAuth = credentials.authorize(httplib2.Http())
service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)


def read_from_google_sheets(range_name):
    result = None
    try:
        result = (
            service.spreadsheets()
            .values()
            .get(spreadsheetId=spreadsheet_id, range=range_name)
            .execute()
        )
    except googleapiclient.errors.HttpError:
        time.sleep(2)
    return result.get('values', []) if result else []


def write_to_google_sheets(range_name, values, major_dimension='ROWS'):
    body = {'values': values, 'majorDimension': major_dimension}
    result = (
        service.spreadsheets()
        .values()
        .update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption='USER_ENTERED',
            body=body,
        )
        .execute()
    )
    return result


def update_format_google_sheets(range_values, color):
    body = {
        'requests': [
            {
                'repeatCell': {
                    'range': {
                        'sheetId': 0,
                        'startRowIndex': range_values[0],
                        'endRowIndex': range_values[1],
                        'startColumnIndex': range_values[2],
                        'endColumnIndex': range_values[3],
                    },
                    'cell': {
                        'userEnteredFormat': {
                            'backgroundColor': {
                                'red': color[0],
                                'green': color[1],
                                'blue': color[2],
                            }
                        }
                    },
                    'fields': 'userEnteredFormat.backgroundColor',
                }
            }
        ]
    }
    result = (
        service.spreadsheets()
        .batchUpdate(spreadsheetId=spreadsheet_id, body=body)
        .execute()
    )
    return result
