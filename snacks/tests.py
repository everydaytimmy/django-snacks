from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class SnackTest(TestCase):
  def setUp(self):
    self.user = get_user_model().objects.create_user(
      username='tester', email='tester@gmail.com', password='pass'
    )

    self.snack = Snack.objects.create(
      name='fried pickles',
      description="Don't forget the ranch",
      purchaser=self.user
    )

  def test_string_representation(self):
        self.assertEqual(str(self.snack), "fried pickles")

  def test_snack_content(self):
        self.assertEqual(f"{self.snack.name}", "fried pickles")
        self.assertEqual(f"{self.snack.purchaser}", "tester")
        self.assertEqual(f"{self.snack.description}", "Don't forget the ranch")

  def test_snack_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "fried pickles")
        self.assertTemplateUsed(response, "snack_list.html")

  def test_snack_detail_view(self):
        response = self.client.get(reverse("snack_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Purchaser: tester")
        self.assertTemplateUsed(response, "snack_detail.html")

  # def test_snack_create_view(self):
  #       response = self.client.post(
  #           reverse("snack_create"),
  #           {
  #               "name": "Samoas",
  #               "description": "Best Girl Scout Cookie",
  #               "purchaser": self.user.id,
  #           },
  #           follow=True,
  #       )

  #       self.assertRedirects(response, reverse("snack_detail", args="2"))
  #       self.assertContains(response, "Details about Samoas")

  def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"name": "Updated name", "description": "no", "purchaser": self.user.id},
        )

        self.assertRedirects(response, reverse("snack_detail", args="1"))

  def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)