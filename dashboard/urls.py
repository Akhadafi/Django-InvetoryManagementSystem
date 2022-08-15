from django.urls import path
from dashboard import views

urlpatterns = [
    path("dashboard/", views.index, name="dashboard-index"),
    path("staff/", views.staff, name="dashboard-staff"),
    path("order/", views.order, name="dashboard-order"),
    path("product/", views.product, name="dashboard-product"),
    # path("products/", views.products, name="dashboard-products"),
    # path(
    #     "products/delete/<int:pk>/",
    #     views.product_delete,
    #     name="dashboard-products-delete",
    # ),
    # path(
    #     "products/detail/<int:pk>/",
    #     views.product_detail,
    #     name="dashboard-products-detail",
    # ),
    # path("products/edit/<int:pk>/", views.product_edit, name="dashboard-products-edit"),
    # path("customers/", views.customers, name="dashboard-customers"),
    # path(
    #     "customers/detial/<int:pk>/",
    #     views.customer_detail,
    #     name="dashboard-customer-detail",
    # ),
]
