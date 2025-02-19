import requests
import base64

# obtain OAuth 2.0 access token
def get_access_token(client_id, client_secret):
    """
    this is an authontification function, it use App ID (client_is) and Cert id (client_secret). to authentificate 
    it send an HTTP request with client_is and client_secret encoded in 64 base to obtain token used to extract data 
    """
    url = 'https://api.ebay.com/identity/v1/oauth2/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic ' + base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode(),
    }
    data = {
        'grant_type': 'client_credentials',
        'scope': 'https://api.ebay.com/oauth/api_scope'
    }
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()['access_token']

# search for computers on eBay
def search_computers(product_name, access_token, country_code):
    """
    this function use the token extracted with function 'get_access_token' and extract product using Brows API from eBay.
    product_name : name of the product 
    country_code : name of the country from where to extract products 
    thats documenetation link of the api : https://developer.ebay.com/api-docs/buy/browse/overview.html
    """
    countries = {
        'US': 'EBAY_US',
        'CA': 'EBAY_CA',  # eBay Canada (English)
        'GB': 'EBAY_GB',  # eBay UK
        'AU': 'EBAY_AU',  # eBay Australia
        'AT': 'EBAY_AT',  # eBay Austria
        'BE': 'EBAY_NLBE',  # eBay Belgium (Dutch) or 'EBAY_FRBE' for French
        'FR': 'EBAY_FR',  # eBay France
        'DE': 'EBAY_DE',  # eBay Germany
        'IT': 'EBAY_IT',  # eBay Italy
        'NL': 'EBAY_NL',  # eBay Netherlands
        'ES': 'EBAY_ES',  # eBay Spain
        'CH': 'EBAY_CH',  # eBay Switzerland
        'HK': 'EBAY_HK',  # eBay Hong Kong
        'IE': 'EBAY_IE',  # eBay Ireland
        'PL': 'EBAY_PL',  # eBay Poland
        'SG': 'EBAY_SG',  # eBay Singapore
        'CA': 'EBAY_FRCA'  # eBay Canada (French) (Note: 'CA' appears twice, so ensure correct usage)
    }
    url = 'https://api.ebay.com/buy/browse/v1/item_summary/search'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'X-EBAY-C-MARKETPLACE-ID': countries[f'{country_code}']
    }
    params = {
        'q': f'{product_name}',
        'filter': f'deliveryCountry:{country_code}'
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def process_data(json_data):
    """
    this function takes JSON data extracted and processes it.
    """
    try:
        # extract relevant fields
        filtered_data = []
        for item in json_data.get("itemSummaries", []):
            filtered_data.append({
                "Item ID": item.get("itemId"),
                "Title": item.get("title"),
                "Price": item.get("price", {}).get("value"),
                "Currency": item.get("price", {}).get("currency"),
                "Condition": item.get("condition"),
                "Item URL": item.get("itemWebUrl"),
                "Image URL": item.get("image", {}).get("imageUrl"),
                "Seller Username": item.get("seller", {}).get("username"),
                "Seller Feedback %": item.get("seller", {}).get("feedbackPercentage"),
                "Seller Feedback Score": item.get("seller", {}).get("feedbackScore"),
                "Shipping Cost": item.get("shippingOptions", [{}])[0].get("shippingCost", {}).get("value"),
                "Shipping Currency": item.get("shippingOptions", [{}])[0].get("shippingCost", {}).get("currency"),
                "Original Price": item.get("marketingPrice", {}).get("originalPrice", {}).get("value"),
                "Discount Percentage": item.get("marketingPrice", {}).get("discountPercentage"),
                "Discount Amount": item.get("marketingPrice", {}).get("discountAmount", {}).get("value"),
                "Categories": ", ".join([cat.get("categoryName", "Unknown") if isinstance(cat, dict) else str(cat) for cat in item.get("categories", [])]),
                "Country": item.get("itemLocation", {}).get("country", {}),
            })
        return filtered_data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred for marketplace {e}")