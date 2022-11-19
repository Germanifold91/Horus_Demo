import random
from datetime import date
from itertools import product

import numpy as np
import pandas as pd
from faker import Faker

#Construccion de Data Frame empleados dimensiones usando informacion generada aleatoriamente

n_rows = 100
columns_employees = ['Cedula', 'Nombre_completo', 'Genero', 'Fecha_Nacimiento', 'Municipio', 'Cargo', 'Fecha_Contratacion']

identification_no = random.sample(range(1000000, 9999999), n_rows)
first_names = ["German", "Raul", "Carlos", "Maria", "Angela", "Rosa", "Julia", "Rosario", "Jorge", "Paula", "Jennifer", "Natalia", "Heidy", "Lucia"]
last_names = ["Rodriguez", "Romero", "Sanchez", "Ramirez", "Gomez", "Villota", "Carvajal", "Hernandez", "Suescun", "Quintana"]

full_name = list(product(first_names, last_names))
full_name = [" ".join(tuple) for tuple in full_name]


assignments_dict = {
    "assignments": ["Aseador", "Todero", "Secretaria", "Supervisora", "Atencion al Cliente", "Comercial"],
    "assignments_weights": [0.6, 0.3, 0.03, 0.02, 0.03, 0.02]
}

locations_dict = {
    "locations": ["Bogota", "Tunja", "Soacha", "Cajica", "Chia", "Mosquera", "Zipaquira", "Girardot"],
    "locations_weights": [0.8, 0.03, 0.02, 0.05, 0.02, 0.03, 0.03, 0.02]
}

gender_dict = {
    "gender": ["Femenino", "Masculino"],
    "gender_weights": [0.8, 0.2]
}

fake = Faker()
birthday_dates = [fake.date_between(start_date=date(1970, 1, 1), end_date=date(2000, 12, 31)).strftime('%Y-%m-%d') for _ in range(n_rows)]
starting_dates = [fake.date_between(start_date=date(2017, 1, 1), end_date=date(2022, 10, 31)).strftime('%Y-%m-%d') for _ in range(n_rows)]


employees_df = pd.DataFrame(columns = columns_employees)
employees_df['Cedula'] = identification_no
employees_df['Nombre_Completo'] = random.sample(full_name, k = n_rows)
employees_df['Genero'] = random.choices(gender_dict["gender"], gender_dict["gender_weights"], k = n_rows)
employees_df['Fecha_Nacimiento'] = birthday_dates
employees_df['Municipio'] = random.choices(locations_dict["locations"], locations_dict["locations_weights"], k = n_rows)
employees_df['Cargo'] = random.choices(assignments_dict["assignments"], assignments_dict["assignments_weights"], k = n_rows)
employees_df['Fecha_Contratacion'] = starting_dates

# Construccion de Data Frame de clientes a partir de informacion generada aleatoriamente
n_clinets = 35
columns_client = ['NIT_ID', 'Nombre', 'Tipo_Ubicacion', 'Numero_Telefono', 'Ciudad', 'Inicio_Contrato', 'Estado_Contrato', 'Fin_Contrato']
nit_id = random.sample(range(1000000, 9999999), n_clinets)
nombre_dict = {
    "first_part": ["Conjunto", "Centro Empresarial", "Complejo Industrial", "Residencias", "Balcones", "Altos de"],
    "second_part": ["Rosario", "Bogota", "Cedros", "Nogales", "Arrayanes", "Bolivar"]
    }
full_name_center = list(product(nombre_dict["first_part"], nombre_dict["second_part"]))
full_name_center = [" ".join(tuple) for tuple in full_name_center]
location_type = ["Residencial", "Industrial", "Comercial", "Oficina"]
phone_number = random.sample(range(1000000, 9999999), n_clinets)
starting_dates = [fake.date_between(start_date=date(2019, 1, 1), end_date=date(2022, 12, 31)).strftime('%Y-%m-%d') for _ in range(n_clinets)]


clients_df = pd.DataFrame(columns = columns_client)
clients_df['NIT_ID'] = nit_id
clients_df['Nombre'] = random.sample(full_name_center, k = n_clinets)
clients_df['Tipo_Ubicacion'] = random.choices(location_type, k = n_clinets)
clients_df['Numero_Telefono'] = phone_number
clients_df['Ciudad'] = random.choices(locations_dict["locations"], locations_dict["locations_weights"], k = n_clinets)
clients_df['Inicio_Contrato'] = starting_dates
clients_df['Estado_Contrato'] = "Activo"
clients_df['Fin_Contrato'] = None 

#displaying random integers in data frame
print(clients_df)