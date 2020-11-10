from django.test import TestCase
from django.urls import reverse
from django_glossary.models import Term, Synonym


class GlossaryTestCase(TestCase):

    #urls = 'urls'

    def setUp(self):
        self.ace = Term.objects.create( title="Ace", slug = "ace", description="Description for Ace")
        self.base = Term.objects.create( title="Bace", slug = "base", description="Ace of BASE!")
        self.case = Term.objects.create( title="Case", slug = "case", description="Make a case")
        self.dace = Term.objects.create( title="Dace", slug = "dace", description="A dude named Dace")
        self.eco = Term.objects.create( title="Eco", slug = "eco", description="Eco-awesomeness")
        self.face = Term.objects.create( title="Face", slug = "face", description="In your face!")
        self.gale = Term.objects.create( title="Gale", slug = "gale", description="Dorothy Gale?")
        self.hail = Term.objects.create( title="Hail", slug = "hail", description="Hail of fail")
        self.ill = Term.objects.create( title="Ill", slug = "ill", description="That coat is ill.")
        self.synonym = Synonym.objects.create(title="Synonym", term = self.ace)

    def test_term(self):
        # These really aren't supposed to be different without non-ascii test data:
        self.assertEqual(str(self.ace), str(self.ace))

        self.assertEqual(self.ace.title, u"Ace")
        self.assertEqual(self.ace.slug, "ace")

    def test_synonym(self):
        self.assertEqual(self.ace.title, self.synonym.term.title)

        # These really aren't supposed to be different without non-ascii test data:
        self.assertEqual(str(self.synonym), str(self.synonym))

        self.assertIn("synonym for", str(self.synonym))
        self.assertIn(self.ace.title, str(self.synonym))

    def test_term_view(self):
        response = self.client.get(reverse("django_glossary:term-list"))
        self.assertTrue(response.status_code == 200)
