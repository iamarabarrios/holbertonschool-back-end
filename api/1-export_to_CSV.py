#!/usr/bin/python3
"""Exporta datos en formato CSV."""

import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        URL = "https://jsonplaceholder.typicode.com"
        ID_EMPLEADO = sys.argv[1]

        respuesta = requests.get(f"{URL}/users/{ID_EMPLEADO}/todos", params={
            "_expand": "user"})
        datos = respuesta.json()

        if datos:
            NOMBRE_EMPLEADO = datos[0]["user"]["name"]

            with open(f"{ID_EMPLEADO}.csv", "w", newline="",
                      encoding="utf-8") as csvfile:
                csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
                for tarea in datos:
                    csv_writer.writerow([ID_EMPLEADO, NOMBRE_EMPLEADO, tarea[
                        "completed"], tarea["title"]])
