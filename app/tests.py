# Importez les modules nécessaires pour les tests unitaires Django
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Model3d

# Créez une classe de tests pour votre application
class CodelinTest(TestCase):

    # Méthode setUp : exécutée avant chaque test
    def setUp(self):
        # Créez un utilisateur de test
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    # Testez la création d'un modèle 3D
    def test_create_model3d(self):
        # Connectez l'utilisateur de test
        self.client.login(username='testuser', password='testpassword')

        # Créez un modèle 3D
        response = self.client.post('/api/model3d/', {'name': 'Mon Modèle 3D'}, format='json')

        # Vérifiez si la création a réussi (code de réponse HTTP 201)
        self.assertEqual(response.status_code, 201)

        # Vérifiez si le modèle 3D existe dans la base de données
        model3d = Model3d.objects.get(name='Mon Modèle 3D')
        self.assertIsNotNone(model3d)

    # Testez l'accès à la liste des modèles 3D (exemple d'accès authentifié)
    def test_access_model3d_list(self):
        # Connectez l'utilisateur de test
        self.client.login(username='testuser', password='testpassword')

        # Accédez à la liste des modèles 3D
        response = self.client.get('/api/model3d/')

        # Vérifiez si l'accès est autorisé (code de réponse HTTP 200)
        self.assertEqual(response.status_code, 200)

    # Testez l'accès à la liste des modèles 3D (exemple d'accès non authentifié)
    def test_access_model3d_list_unauthenticated(self):
        # Déconnectez l'utilisateur de test (il est inutile de le connecter)
        self.client.logout()

        # Accédez à la liste des modèles 3D sans être authentifié
        response = self.client.get('/api/model3d/')

        # Vérifiez si l'accès est refusé (code de réponse HTTP 403)
        self.assertEqual(response.status_code, 403)

    # Méthode tearDown : exécutée après chaque test
    def tearDown(self):
        # Supprimez l'utilisateur de test
        self.user.delete()
