from django.contrib import sitemaps
from django.urls import reverse

class MySitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['index', 'all_product', 'all_category', 'all_category_filter', 'product',
                'product-detail', 'about', 'contact', 'profile', 'address_view', 'update_address',
                'delete_address', 'add_to_cart', 'show_cart', 'show_wishlist', 'checkout',
                'payment_done', 'orders', 'orderscod', 'cod_checkout', 'search_results',
                'plus_cart', 'minus_cart', 'remove_cart', 'plus_wishlist', 'minus_wishlist',
                'customer_registration', 'login', 'password_change', 'password_change_done',
                'logout', 'password_reset', 'password_reset_done', 'password_reset_confirm',
                'password_reset_complete', 'faq', 'terms_condition', 'privacy', 'support_policy']

    def location(self, item):
        return reverse(item)
