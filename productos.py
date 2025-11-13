class Producto:
    def __init__(self, codigo, nombre, precio, categoria):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
    def mostrar_producto(self):
        print(f"{self.codigo} - {self.nombre} (${self.precio}) - {self.categoria}")
# Catálogo de productos
catalogo = {
    "\nLínea Blanca": {
        "LB001": Producto("LB001", "Nevecón Side By Side", 1920900, "Línea Blanca"),
        "LB002": Producto("LB002", "Lavadora Carga Superior", 3779900, "Línea Blanca"),
        "LB003": Producto("LB003", "Torre de Lavado Carga Frontal", 7279900, "Línea Blanca"),
        "LB004": Producto("LB004", "Dispensador de Agua", 1119900, "Línea Blanca"),
        "LB005": Producto("LB005", "Minibar Frigobar", 599900, "Línea Blanca"),
    },

    "\nPequeños Electrodomésticos": {
        "PE001": Producto("PE001", "Licuadora Magic Bullet", 239900, "Pequeños Electrodomésticos"),
        "PE002": Producto("PE002", "Sanduchera Imusa Panini", 249900, "Pequeños Electrodomésticos"),
        "PE003": Producto("PE003", "Waflera Antidesbordamiento", 339900, "Pequeños Electrodomésticos"),
        "PE004": Producto("PE004", "Crepera Eléctrica", 359900, "Pequeños Electrodomésticos"),
        "PE005": Producto("PE005", "Tostadora Retro", 359900, "Pequeños Electrodomésticos"),
    },

    "\nEntretenimiento": {
        "EN001": Producto("EN001", "TV KALLEY 40 Pulgadas", 799900, "Entretenimiento"),
        "EN002": Producto("EN002", "TV SAMSUNG 75 Pulgadas", 1500000, "Entretenimiento"),
        "EN003": Producto("EN003", "Combo Sala de TV + Repisa", 869900, "Entretenimiento"),
        "EN004": Producto("EN004", "Amplificador Recargable", 349900, "Entretenimiento"),
        "EN005": Producto("EN005", "Sistema De Audio 2.1 Rms", 239900, "Entretenimiento"),
    },

    "\nAires Acondicionados": {
        "AA001": Producto("AA001", "Aire Samsung 12000 BTU", 2200000, "Aires Acondicionados"),
        "AA002": Producto("AA002", "Aire LG Dual Inverter", 2600000, "Aires Acondicionados"),
        "AA003": Producto("AA003", "Aire Midea 18000 BTU", 3000000, "Aires Acondicionados"),
        "AA004": Producto("AA004", "Aire Panasonic 24000 BTU", 3500000, "Aires Acondicionados"),
        "AA005": Producto("AA005", "Aire Carrier 30000 BTU", 4000000, "Aires Acondicionados"),
    }
}
