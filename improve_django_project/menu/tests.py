from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Menu, Item, Ingredient
from .forms import MenuForm


class MenuModelTests(TestCase):
    def test_create_menu_model(self):
        self.menu = Menu.objects.create(season='test')
        self.assertEqual(str(self.menu), self.menu.season)


class ItemModelTests(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            id='1',
            username='Test',
            email='test@test.com',
            password='test123'
        )

    def test_create_item_model(self):
        self.item = Item.objects.create(
            name='item',
            description='item description',
            chef=self.test_user
        )
        self.assertEqual(str(self.item), self.item.name)


class IngredientModelTests(TestCase):
    def test_create_ingredient_model(self):
        self.ingredient = Ingredient.objects.create(
            name='item ingredient'
        )
        self.assertEqual(str(self.ingredient), self.ingredient.name)


class MenuViewsTests(TestCase):
    def setUp(self):
        self.menu = Menu.objects.create(season='test')
        self.item = Item.objects.create(
            name='item',
            description='item description',
            chef=User.objects.create(username='test_user')
        )
        self.ingredient = Ingredient.objects.create(
            name='item ingredient'
        )

    def test_home_view(self):
        resp = self.client.get(reverse('menu_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'menu/menu_home.html')

    def test_menu_detail_view(self):
        resp = self.client.get(reverse('menu_detail',
                                       kwargs={'pk': self.menu.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'test')
        self.assertTemplateUsed(resp, 'menu/menu_detail.html')

    def test_item_detail_view(self):
        resp = self.client.get(reverse('item_detail',
                                       kwargs={'pk': self.item.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'menu/detail_item.html')

    def test_create_new_menu_view(self):
        resp = self.client.get(reverse('menu_new'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'menu/menu_edit.html')

    def test_edit_menu_view(self):
        resp = self.client.get(reverse('menu_edit',
                                       kwargs={'pk': self.menu.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'menu/menu_edit.html')


class UrlFileTests(TestCase):
    def test_home_url(self):
        url = reverse('menu_list')
        self.assertEqual(url, '/')

    def test_menu_edit_url(self):
        url = reverse('menu_edit', args=[1])
        self.assertEqual(url, '/menu_edit/1/')

    def test_menu_detail_url(self):
        url = reverse('menu_detail', args=[1])
        self.assertEqual(url, '/menu_detail/1/')

    def test_menu_item_url(self):
        url = reverse('item_detail', args=[1])
        self.assertEqual(url, '/menu_item/1/')

    def test_menu_new_url(self):
        url = reverse('menu_new')
        self.assertEqual(url, '/menu_create_new/')


class MenuFormTests(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            id='1',
            username='Test',
            email='test@test.com',
            password='test123'
        )

        self.item = Item.objects.create(name='item',
                                        description='item description',
                                        chef=self.test_user)

        self.form = {'season': 'test',
                     'items': [self.item.id],
                     'expiration_date': '9999-12-31'}

    def test_menu_form(self):
        self.form = MenuForm(data=self.form)
        self.assertTrue(self.form.is_valid())