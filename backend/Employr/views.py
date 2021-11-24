from django.shortcuts import render
from django.http import JsonResponse
from schema import Schema
import json

# QUICK TOOLS
def extract_data():
  data = []
  with open('./Employr/data/employees.json', 'r') as openfile:
    data = json.load(openfile)  

  return data

def save_data(data):
  with open('./Employr/data/employees.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

# VIEWS
def list_employees(request):
  print('Listing employees')
  return JsonResponse(extract_data(), safe=False)

def retrieve_employees(request, employee_id):
  print(employee_id)
  return JsonResponse(extract_data()[int(employee_id)])

def add_employee(request):
  new_employee  = json.loads(request.body)

  data = extract_data()
  data.append(new_employee)
  save_data(data)

  return JsonResponse(data, safe=False)

def remove_employee(request, employee_id):
  data = extract_data()
  data.pop(int(employee_id))
  save_data(data)

  return JsonResponse(data, safe=False)