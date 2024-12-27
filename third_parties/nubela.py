# https://www.linkedin.com/in/cristian-godoy-22385b44/
# https://gist.githubusercontent.com/cristiangodoyy/48627d926a3b76b630b75acad76e350a/raw/87be483dc8297ed07f59a366793367a5ff68a2d2/cristian-godoy.json

"""
esto es una prueba para probar la api de proxycurl para scrapear nuestro
perfil de linkedin.
Tenemos 10 creditos que se vencen en 13 dias.

Para no gastar todos los creditos en esta api creamos un gist en gist.github.com
donde adjuntamos nuestro perfil a una respuesta .json
"""

import requests

api_key = 'DW210IlOU9KSpsGO9bPpDg'
headers = {'Authorization': 'Bearer ' + api_key}
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
params = {
    'linkedin_profile_url': 'https://www.linkedin.com/in/cristian-godoy-22385b44/',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=headers)

print(response.json())
print(response._content)
