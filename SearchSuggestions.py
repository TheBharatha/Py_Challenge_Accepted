class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        product_suggestions = []
        products.sort()
        for i in range(len(searchWord)):
            search_term = searchWord[:i+1]
            viable_products = [product for product in products if product.startswith(search_term)]
            product_suggestions.append(viable_products[:3])
        return product_suggestions
