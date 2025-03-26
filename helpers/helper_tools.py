class HelperTools:
    @staticmethod
    def get_digit_price(price: str) -> float:
        clean_price = ''.join(char for char in price if char.isdigit() or char in [",", "."])
        if not clean_price:
            return 0.0
        return float(clean_price.replace(",", "."))
