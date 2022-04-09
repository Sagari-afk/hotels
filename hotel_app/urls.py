from django.urls import path

from views import api_hotels


urlpatterns = [
    path('hotels/all', (api_hotels)),
]
