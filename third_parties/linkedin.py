import os
import requests

from dotenv import load_dotenv

load_dotenv()
# token DW210IlOU9KSpsGO9bPpDg
def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile
    """
    if mock:
        linkedin_profile_url = linkedin_profile_url
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers=header_dic,
            timeout=10,
        )

    data = response.json()

    # We need it is because we need send the payload data only with la data justa because chatgpt con cobra por token
    # segun the quantity of the keys-values that json payload has.
    data = {  # it snippet code delete redundant fields, that has empty array [], blank values and null values
        k: v for k, v in data.items()
        if v not in ([], "", "", None)
           and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
#
# if __name__ == '__main__':
#     response = scrape_linkedin_profile(
#         linkedin_profile_url='https://gist.githubusercontent.com/cristiangodoyy/48627d926a3b76b630b75acad76e350a/raw/cbf4ce82940c4140574c55343568ef89cb2240af/cristian-godoy.json',
#         mock=True
#     )
#     print(response)
