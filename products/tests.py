from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Category, Product

class AuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register(self):
        response = self.client.post('/api/auth/register/', {
            'username': 'testuser',
            'email': 'test@test.com',
            'password' : 'testpass123'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_login(self):
        User.objects.create_user(username='testuser', password='testpass123')
        response = self.client.post('/api/auth/login/', {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

class CategoryTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        response = self.client.post('/api/auth/login/', {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
    
    def test_create_category(self):
        response = self.client.post('/api/categories/', {'name': 'Electrónica'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_list_categories(self):
        Category.objects.create(name = 'Ropa')
        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_category(self):
        category = Category.objects.create(name='Ropa')
        response = self.client.put(f'/api/categories/{category.id}/',{'name': 'Ropa Actualizada'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_category(self):
        category = Category.objects.create(name='Ropa')
        response = self.client.delete(f'/api/categories/{category.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ProductTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        response = self.client.post('/api/auth/login/', {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.category = Category.objects.create(name='Electrónica')

    def test_create_product(self):
        response = self.client.post('/api/products/', {
            'name': 'Laptop',
            'description': 'Laptop 15 pulgadas',
            'price': '850000',
            'stock': 5,
            'category': self.category.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_products(self):
        Product.objects.create(
            name='Laptop', price=850000, stock=5,
            category=self.category, user=self.user
        )
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product(self):
        product = Product.objects.create(
            name='Laptop', price=850000, stock=5,
            category=self.category, user=self.user
        )
        response = self.client.put(f'/api/products/{product.id}/', {
            'name': 'Laptop Actualizada',
            'price': '900000',
            'stock': 3,
            'category': self.category.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_product(self):
        product = Product.objects.create(
            name='Laptop', price=850000, stock=5,
            category=self.category, user=self.user
        )
        response = self.client.delete(f'/api/products/{product.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_only_sees_own_products(self):
        other_user = User.objects.create_user(username='other', password='testpass123')
        Product.objects.create(
            name='Producto ajeno', price=100, stock=1,
            category=self.category, user=other_user
        )
        response = self.client.get('/api/products/')
        self.assertEqual(len(response.data), 0)