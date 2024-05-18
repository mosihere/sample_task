from rest_framework.pagination import PageNumberPagination



class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 50

    def get_page_size(self, request):
        page_size = super().get_page_size(request)
        if page_size is None:
            page_size = self.page_size
            
        return page_size