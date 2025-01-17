import configuration
import data
import sender_stand_request


def create_user():
    user_response = sender_stand_request.post_new_user(data.user_body)
    return(user_response.json()["authToken"])

def create_kit(kit_body):
    token = create_user()
    kit_response = sender_stand_request.post_products_kits(kit_body, token)
    print(kit_response.status_code)

kit_body = {  "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}
create_kit(kit_body)

# Función de prueba positiva
def positive_assert(kit_body):
    token = create_user()
    kit_response = sender_stand_request.post_products_kits(kit_body, token)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

#Función de prueba negativa
def negative_assert(kit_body):
    token = create_user()
    kit_response = sender_stand_request.post_products_kits(kit_body, token)
    assert kit_response.status_code == 400

 
# Prueba 1	El número permitido de caracteres (1):
def test_create_kit_with_1_character_in_name():
    kit_body = data.kit_with_1_character_in_name
    positive_assert(kit_body)

# Prueba 2	El número permitido de caracteres (511):
def test_create_kit_with_511_character_in_name():
     kit_body = data.with_511_character_in_name
     positive_assert(kit_body)

# Prueba 3	El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_with_0_character_in_name():
    kit_body = data.with_0_character_in_name
    negative_assert(kit_body)

# Prueba 4	El número de caracteres es mayor que la cantidad permitida (512):
def test_create_kit_with_512_character_in_name():
    kit_body = data.with_512_character_in_name
    negative_assert(kit_body)

# Prueba 5	Se permiten caracteres especiales:
def test_create_kit_with_special_characters_in_name():
    kit_body = data.special_characters_in_name
    positive_assert(kit_body)

# Prueba 6	Se permiten espacios
def test_create_kit_with_spaces_in_name():
    kit_body = data.spaces_in_name
    positive_assert(kit_body)

# Prueba 7	Se permiten número
def test_create_kit_with_numbers_in_name():
    kit_body = data.numbers_in_name
    positive_assert(kit_body)

# Prueba 8	El parámetro no se pasa en la solicitud
def test_create_kit_with_no_parameter_in_name():
    kit_body = data.no_parameter_in_name
    negative_assert(kit_body)

# Prueba 9	Se ha pasado un tipo de parámetro diferente (número)
def test_create_kit_diferent_value_type_as_parameter_in_name():
    kit_body = data.diferent_value_type_as_parameter_in_name
    negative_assert(kit_body)