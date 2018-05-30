"""marketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from marketplace import views
from marketplace import user
from marketplace import lot
from marketplace.ajax import ajax_validate
from marketplace.ajax import ajax_profile

admin.autodiscover()

urlpatterns = [
    path('', views.view_homepage, name='home'),
    path('admin/', admin.site.urls),
    path('registration/', views.view_regisration, name='registration'),
    path('authorization/', views.view_authorization, name='authorization'),
    path('profile/<int:user_id>/', views.view_user_profile, name='profile'),
    path('inventory/<int:user_id>', views.view_user_inventory, name='inventory'),
    path('inventory/<int:user_id>/item/<int:user_item_id>', views.view_user_inventory_item, name='inventory_item'),
    path('lot/<int:lot_id>/', views.view_lot, name='lot'),
    path('reguser', user.reguser, name='reguser'),
    path('login', user.login_user, name='authorizuser'),
    path('logout/', user.logout_user, name='logout'),
    path('lot/<int:lots_id>/lotitem', lot.lotitem, name='lotitem'),
    path('transaction/', views.view_user_transaction, name='transaction'),
    path('inventory/createnewlot', lot.create, name='create_lot'),
    path('weapon/', views.view_homepage_sort_weapon, name='weapon'),
    path('armor/', views.view_homepage_sort_armor, name='armor'),
    path('food/', views.view_homepage_sort_food, name='food'),
    path('search_item', views.view_homepage_search_item, name='search_item'),
    path('ajax/validate_username/', ajax_validate.validate_username, name='validate_username'),
    path('ajax/validate_email/', ajax_validate.validate_email, name='validate_email'),
    path('profile/<int:user_id>/edit', views.view_user_edit_profile, name='edit_profile'),
    path('ajax/edit_validate_username/', ajax_validate.edit_validate_username, name='edit_validate_username'),
    path('profile/<int:user_id>/change_user', user.change_user, name='change_user'),
    path('ajax/profile_activity/', ajax_profile.profile_activity, name='profile_activity'),
    #path('ajax/validate_authorization/', ajax_validate.validate_authorization, name='validate_authorization'),

]
