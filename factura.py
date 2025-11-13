from datetime import datetime

# Clase Factura
class Factura:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items = []
    def agregar_producto(self, producto, cantidad):
        self.items.append((producto, cantidad))
    def mostrar_factura(self):
        subtotal = 0
        print(f"\nFactura del cliente: {self.cliente}\n")
        print("{:<25} {:<10} {:<15}".format("Producto", "Cant.", "Subtotal"))
        print("-" * 50)
        for producto, cantidad in self.items:
            total_item = producto.precio * cantidad
            print(f"{producto.nombre:<25} x{cantidad:<5} ${total_item:,}")
            subtotal += total_item
        iva = subtotal * 0.19
        total = subtotal + iva
        print("\nSubtotal: ${:,.0f}".format(subtotal))
        print("IVA (19%): ${:,.0f}".format(iva))
        print("Total a pagar: ${:,.0f}".format(total))
        # Guardar factura automáticamente
        self.guardar_factura(subtotal, iva, total)
    def guardar_factura(self, subtotal, iva, total):
        """Guarda la factura en un archivo de texto"""
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("facturas.txt", "a", encoding="utf-8") as archivo:
            archivo.write("\n\n")
            archivo.write(f"Factura de {self.cliente} - {fecha}\n")
            archivo.write("\n")
            for producto, cantidad in self.items:
                total_item = producto.precio * cantidad
                archivo.write(f"{producto.nombre} x{cantidad} = ${total_item:,}\n")
            archivo.write(f"\nSubtotal: ${subtotal:,}\n")
            archivo.write(f"IVA (19%): ${iva:,}\n")
            archivo.write(f"TOTAL: ${total:,}\n")
            archivo.write("\n")
        print("\nLa factura ha sido guardada en 'facturas.txt'\n")
