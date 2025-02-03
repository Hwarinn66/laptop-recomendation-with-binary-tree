from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.secret_key = '12345'

class   Product:
    def __init__(self, name, brand, processor, ram, storage, vga, price, image_url, youtube,  link="",
                 screen="", battery="", weight="", os="", 
                 wifi="", bluetooth="", keyboard="", camera="",
                 ports="", description="",):
        self.name = name
        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.vga = vga
        self.price = price
        self.image_url = image_url
        self.youtube = youtube
        self.link = link
        self.screen = screen
        self.battery = battery
        self.weight = weight
        self.os = os
        self.wifi = wifi
        self.bluetooth = bluetooth
        self.keyboard = keyboard
        self.camera = camera
        self.ports = ports
        self.description = description
       
        
        

class ProductNode:
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None

class ProductBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, product):
        if self.root is None:
            self.root = ProductNode(product)
        else:
            self._insert_recursively(self.root, product)

    def _insert_recursively(self, current_node, product):
        if product.price <= current_node.product.price:
            if current_node.left is None:
                current_node.left = ProductNode(product)
            else:
                self._insert_recursively(current_node.left, product)
        else:
            if current_node.right is None:
                current_node.right = ProductNode(product)
            else:
                self._insert_recursively(current_node.right, product)

    def recommend_products(self, brand, processor, ram, storage, vga, min_price, max_price, is_gaming):
        recommended_products = []
        self._recommend_recursively(self.root, brand, processor, ram, storage, vga, min_price, max_price, recommended_products, is_gaming)
        return recommended_products

    def _recommend_recursively(self, current_node, brand, processor, ram, storage, vga, min_price, max_price, recommended_products, is_gaming):
        if current_node is None:
            return

        product = current_node.product
        if (is_gaming and product.vga != "") or (not is_gaming and product.vga == ""):
            if (brand in product.brand and
                processor in product.processor and
                product.ram >= ram and
                product.storage >= storage and
                min_price <= product.price <= max_price):
                recommended_products.append(product)

        if product.price >= min_price:
            self._recommend_recursively(current_node.left, brand, processor, ram, storage, vga, min_price, max_price, recommended_products, is_gaming)

        if product.price <= max_price:
            self._recommend_recursively(current_node.right, brand, processor, ram, storage, vga, min_price, max_price, recommended_products, is_gaming)

# Initialize Product Tree
product_tree = ProductBinaryTree()
laptops = [
    Product(
        name="Lenovo LOQ Gaming",
        brand="Intel",
        processor="Intel Core i5",
        ram=12,
        storage=512,
        vga="Nvidia RTX 3050",
        price=13000000,
        image_url="/static/images/lenovo-loq.jpg",
        youtube="https://youtu.be/LtsfUEwP67E?si=oOgMeda611ymgGO5",
        link = "https://tokopedia.link/HbvXT6PrAQb",
        screen="15.6 inch FHD (1920 x 1080) IPS 300nits Anti-glare, 144Hz",
        battery="60Wh",
        weight="2.4 kg",
        os="Windows 11 Home",
        wifi="Wi-Fi 6E",
        bluetooth="Bluetooth 5.1",
        keyboard="Backlit Keyboard",
        camera="HD 720p with E-camera Shutter",
        ports="3x USB 3.2 Gen 1, 1x HDMI 2.0, 1x Ethernet (RJ-45), 1x Headphone / microphone combo jack (3.5mm)",
        description="Laptop gaming entry-level dengan performa yang baik untuk gaming ringan dan pekerjaan sehari-hari."
        
        
    ),
    
    Product(
        name="Asus ROG Zephyrus G14",
        brand="AMD",
        processor="AMD Ryzen 9",
        ram=16,
        storage=512,
        vga="RX6700",
        price=21000000,
        image_url="/static/images/w250.png",
        youtube="https://youtu.be/LtsfUEwP67E?si=oOgMeda611ymgGO5",
        link = "https://tokopedia.link/HbvXT6PrAQb",
        screen="14-inch QHD+ (2560 x 1600) 16:10 165Hz",
        battery="76WHrs",
        weight="1.72 kg",
        os="Windows 11 Pro",
        wifi="Wi-Fi 6E",
        bluetooth="Bluetooth 5.2",
        keyboard="Backlit Keyboard with RGB",
        camera="1080p FHD IR Camera",
        ports="2x USB 4.0 Type-C, 2x USB 3.2 Gen 2 Type-A, 1x HDMI 2.0b, 1x Audio combo jack",
        description="Laptop gaming premium dengan layar yang memukau dan performa tinggi dalam bentuk yang kompak."
        
    ),
    
    Product(
        name="Acer Nitro 5",
        brand="Intel",
        processor="Intel Core i5",
        ram=8,
        storage=512,
        vga="Nvidia RTX3050",
        price=12000000,
        image_url="/static/images/acer-nitro.jpg",
        youtube="https://youtu.be/LtsfUEwP67E?si=oOgMeda611ymgGO5",
        link = "https://tokopedia.link/HbvXT6PrAQb",
        screen="15.6 inch FHD (1920 x 1080) IPS 144Hz",
        battery="57Wh",
        weight="2.5 kg",
        os="Windows 11 Home",
        wifi="Wi-Fi 6",
        bluetooth="Bluetooth 5.0",
        keyboard="4-Zone RGB Keyboard",
        camera="HD Webcam",
        ports="3x USB 3.2 Gen 1 Type-A, 1x USB 3.2 Gen 2 Type-C, 1x HDMI 2.1, 1x RJ45",
        description="Gaming laptop dengan harga terjangkau namun tetap memberikan performa yang baik untuk gaming modern."
        
    ),
    
    Product(
        name="",
        brand="",
        processor="",
        ram="",
        storage="",
        vga="",
        price=11,
        image_url="",
        youtube="",
        link="",
        screen="",
        battery="",
        weight="",
        os="",
        wifi="",
        bluetooth="",
        keyboard="",
        camera="",
        ports="",
        description="",

        
    ),

     Product(
        name="",
        brand="",
        processor="",
        ram="",
        storage="",
        vga="",
        price=11,
        image_url="",
        youtube="",
        link="",
        screen="",
        battery="",
        weight="",
        os="",
        wifi="",
        bluetooth="",
        keyboard="",
        camera="",
        ports="",
        description="",

        
    ),

     Product(
        name="",
        brand="",
        processor="",
        ram="",
        storage="",
        vga="",
        price=11,
        image_url="",
        youtube="",
        link="",
        screen="",
        battery="",
        weight="",
        os="",
        wifi="",
        bluetooth="",
        keyboard="",
        camera="",
        ports="",
        description="",

        
    ),

     Product(
        name="",
        brand="",
        processor="",
        ram="",
        storage="",
        vga="",
        price=11,
        image_url="",
        youtube="",
        link="",
        screen="",
        battery="",
        weight="",
        os="",
        wifi="",
        bluetooth="",
        keyboard="",
        camera="",
        ports="",
        description="",

        
    ),

     Product(
        name="",
        brand="",
        processor="",
        ram="",
        storage="",
        vga="",
        price=11,
        image_url="",
        youtube="",
        link="",
        screen="",
        battery="",
        weight="",
        os="",
        wifi="",
        bluetooth="",
        keyboard="",
        camera="",
        ports="",
        description="",

        
    ),

     Product(
        name="",
        brand="",
        processor="",
        ram="",
        storage="",
        vga="",
        price=11,
        image_url="",
        youtube="",
        link="",
        screen="",
        battery="",
        weight="",
        os="",
        wifi="",
        bluetooth="",
        keyboard="",
        camera="",
        ports="",
        description="",

        
    ),
]


for laptop in laptops:
    product_tree.insert(laptop)

@app.template_filter('format_currency')
def format_currency(value):
    return "{:,.0f}".format(value)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_processors/<brand>')
def get_processors(brand):
    processors = {
        'Intel': ["Intel Core i3","Intel Core i5", "Intel Core i7", "Intel core i9"],
        'AMD': ["AMD Ryzen 3", "AMD Ryzen 5", "AMD Ryzen 7", "AMD Ryzen 9"],
        'Apple': ["Apple M1", "Apple M2"]
    }
    return jsonify(processors.get(brand, []))

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()

    try:
        brand = data.get('brand', '')
        processor = data.get('processor', '')
        ram = int(data.get('ram', 0))
        storage = int(data.get('storage', 0))
        min_price = float(data.get('minPrice', 0))
        max_price = float(data.get('maxPrice', 0))
        is_gaming = data.get('type') == 'gaming'
        vga = data.get('vga', '') if is_gaming else ''
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid input data'}), 400

    results = product_tree.recommend_products(brand, processor, ram, storage, vga, min_price, max_price, is_gaming)
    return jsonify([{
        'name': product.name,
        'price': product.price,
        'brand': product.brand,
        'processor': product.processor,
        'ram': product.ram,
        'storage': product.storage,
        'vga': product.vga,
        'image_url': product.image_url
    } for product in results])

@app.route('/product/<string:name>')
def product_detail(name):
    # Mencari laptop dari daftar laptops yang sudah ada
    product = next((laptop for laptop in laptops if laptop.name == name), None)
    
    if product:
        return render_template('product_detail.html', product=product)
    return "Product not found", 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
