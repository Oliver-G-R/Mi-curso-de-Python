# crea un set con mac address
"""
    Los tipos set son una colección de elementos que no tienen índice y no se pueden repetir.
    Son utilizados para almacenar tipos sin un orden de importancia.
"""
macAddress = {
    "ee:07:2c:f2:9b:72",
    "ee:07:2c:f2:9b:73",
    "ee:07:2c:f2:9b:74",
}

macAddress.add("ee:07:2c:f2:9b:75")
macAddress.remove("ee:07:2c:f2:9b:73")
macAddress.clear()
del macAddress

# Devuelve un valor true si el elemento está en el set o false si no lo está
macAddressCapture = "ee:07:2c:f2:9b:72" in macAddress

print(macAddress)
