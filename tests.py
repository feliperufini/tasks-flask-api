import pytest
import requests

BASE_URL = 'http://localhost:5000'
tasks = []

def testCreateTask():
  newTaskData = {
    "title": "Teste de tarefa",
    "description": "Descrição do teste"
  }
  resposne = requests.post(f'{BASE_URL}/tasks', json=newTaskData)
  assert resposne.status_code == 200
