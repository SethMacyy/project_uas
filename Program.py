# Class untuk menyimpan data produk
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


# Class untuk memproses logika program
class ProductProcess:
    @staticmethod
    def validate_input(input_value, data_type, min_value=None):
        try:
            value = data_type(input_value)
            if min_value is not None and value < min_value:
                raise ValueError(f"Nilai harus lebih besar atau sama dengan {min_value}.")
            return value
        except ValueError as e:
            raise ValueError(f"Input tidak valid: {e}")


# Class untuk menampilkan data ke layar tanpa library eksternal
class ProductView:
    @staticmethod
    def display_products(products):
        headers = ["No", "Nama Produk", "Harga Satuan", "Jumlah", "Total Harga"]
        print(f"{headers[0]:<5} {headers[1]:<20} {headers[2]:<15} {headers[3]:<10} {headers[4]:<15}")
        print("=" * 65)
        for i, product in enumerate(products, start=1):
            print(f"{i:<5} {product.name:<20} {product.price:<15.2f} {product.quantity:<10} {product.total_price():<15.2f}")
        print("=" * 65)


# Fungsi utama untuk menjalankan program
def main():
    print("=== Program Input Data Produk ===")
    products = []

    while True:
        try:
            name = input("Masukkan nama produk: ").strip()
            if not name:
                raise ValueError("Nama produk tidak boleh kosong.")

            price = ProductProcess.validate_input(
                input("Masukkan harga satuan (angka desimal): "), float, min_value=0
            )
            quantity = ProductProcess.validate_input(
                input("Masukkan jumlah (bilangan bulat): "), int, min_value=1
            )

            product = Product(name, price, quantity)
            products.append(product)

            another = input("Tambah produk lagi? (y/n): ").strip().lower()
            if another != 'y':
                break
        except ValueError as e:
            print(f"Error: {e}")

    print("\n=== Daftar Produk ===")
    ProductView.display_products(products)


if __name__ == "__main__":
    main()
