import requests

# กำหนด API URL และ API Key
API_URL = "https://api.lazada.com.my/rest"
API_KEY = "your_api_key_here"  # ใส่ API Key ของคุณที่นี่

# หมวดหมู่สินค้าต่าง ๆ (ตัวอย่าง)
CATEGORY_IDS = {
    "clothing": "12345",  # หมวดหมู่เสื้อผ้า
    "mouse": "67890",     # หมวดหมู่เมาส์
    "keyboard": "11223"   # หมวดหมู่คีย์บอร์ด
}

# ฟังก์ชันในการดึงข้อมูลสินค้า
def get_product_data(category_id):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    # ตัวอย่าง API endpoint เพื่อดึงข้อมูลสินค้าจากหมวดหมู่ที่เลือก
    url = f"{API_URL}/products/get?category_id={category_id}"

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()  # คืนค่าข้อมูล JSON ของสินค้าทั้งหมด
    else:
        print(f"Error: {response.status_code}")
        return None

# ฟังก์ชันในการจัดอันดับสินค้า
def rank_products(products):
    # จัดอันดับสินค้าจากยอดขาย (sales) หรือคะแนนรีวิว (rating)
    ranked_products = sorted(products, key=lambda x: x['sales'], reverse=True)  # จัดอันดับจากยอดขาย
    return ranked_products

# ฟังก์ชันหลักในการทำงาน
def main():
    # ดึงข้อมูลสินค้าจากหมวดหมู่เสื้อผ้า, เมาส์, คีย์บอร์ด
    for category, category_id in CATEGORY_IDS.items():
        print(f"Ranking products in {category} category:")
        products_data = get_product_data(category_id)
        
        if products_data and 'products' in products_data:
            products = products_data['products']
            ranked_products = rank_products(products)

            # แสดงสินค้าที่จัดอันดับ
            for rank, product in enumerate(ranked_products, 1):
                print(f"Rank {rank}: {product['name']} - Sales: {product['sales']}, Rating: {product['rating']}")
        else:
            print(f"No data found for {category} category.")

if __name__ == "__main__":
    main()
