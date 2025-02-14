from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '19rwYHvaG9lgMn_lFB1NLSZOHepksXIK-cMlDoYva9is'
SAMPLE_RANGE_NAME = 'Реестр клиентов!A2:BT'

def read(mode):
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Success.')

    if mode == 'data':
        print(len(values))
        print('before - ', values)
        for j in range(0, len(values)):
            if len(values[j]) < 72:
                for i in range(len(values), 73):
                    values[j].append('')
        print('after - ', values)
        return values
    elif mode == 'users':
        users = []
        flag = True
        for i in values:
            if not i:
                flag = False
            if flag:
                users.append(i[3])
        return users
    else:
        return 'BAD MODE'
