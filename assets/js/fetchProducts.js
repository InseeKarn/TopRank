// ฟังก์ชันสำหรับดึงข้อมูลสินค้าจาก API
async function fetchProductsByCategory(category) {
  try {
      const response = await fetch(`https://api.shopee.com/v1/products?category=${category}`, {
          method: 'GET',
          headers: {
              'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
          }
      });
      const data = await response.json();
      return data.products; // ส่งกลับข้อมูลสินค้า
  } catch (error) {
      console.error('Error fetching products:', error);
  }
}
