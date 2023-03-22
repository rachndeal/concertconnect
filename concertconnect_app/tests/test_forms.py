from django import TestCase
from concertconnect_app.forms import UserForm, CategoryForm, UerProfileForm

class testForms(TestCase):
    def test_user_form_valid_data(self):
        form = UserForm(fields={
            'username' : 'concert1',
            'email': 'hello@gmail.com'
            'password': 'He!lo'
            })
        self.assertTrue(form.is_valid())

    def test_user_form_no_data(self):
        form = UserForm(fields={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)

    def test_category_form_valid_data(self):
        form = CategoryForm(fields={
            'likes':'1',
            'views':'1',
            'name':'James'
            })
        self.assertTrue(form.is_valid())
        
    def test_category_form_no_data(self):
        form = CategoryForm(fields={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)

    def test_user_profile_form_vaild_data(self):
        form = UserProfileForm(feilds={
            'concerts': 'Hydro'
            'picture': 'PhotoOfHydro'
            })
        self.assertTrue(form.is_valid())

    def test_user_profile_form_no_data(self):
        form = UserProfileForm(fields{})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),2)
        
    
        
            
            

