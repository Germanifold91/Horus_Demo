import random
from datetime import date

import numpy as np
import pandas as pd
from faker import Faker

n_rows = 100
columns_df = ['Cedula', 'Primer_Nombre', 'Apellido', 'Genero', 'Fecha_Nacimiento', 'Municipio', 'Cargo', 'Fecha_Contratacion']

identification_no = random.sample(range(1000000, 9999999), n_rows)
first_names = ["German", "Raul", "Carlos", "Maria", "Angela", "Rosa", "Julia", "Rosario", "Jorge", "Paula", "Jennifer", "Natalia", "Heidy", "Lucia"]
last_names = ["Rodriguez", "Romero", "Sanchez", "Ramirez", "Gomez", "Villota", "Carvajal", "Hernandez", "Suescun", "Quintana"]

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


employees_df = pd.DataFrame(columns = columns_df)
employees_df['Cedula'] = identification_no
employees_df['Primer_Nombre'] = random.choices(first_names, k = n_rows)
employees_df['Apellido'] = random.choices(last_names, k = n_rows)
employees_df['Genero'] = random.choices(gender_dict["gender"], gender_dict["gender_weights"], k = n_rows)
employees_df['Fecha_Nacimiento'] = birthday_dates
employees_df['Municipio'] = random.choices(locations_dict["locations"], locations_dict["locations_weights"], k = n_rows)
employees_df['Cargo'] = random.choices(assignments_dict["assignments"], assignments_dict["assignments_weights"], k = n_rows)
employees_df['Fecha_Contratacion'] = starting_dates
employees_df['Nombre_Completo'] = employees_df["Primer_Nombre"] + ' ' + employees_df["Apellido"]



# displaying random integers in data frame
print(employees_df)