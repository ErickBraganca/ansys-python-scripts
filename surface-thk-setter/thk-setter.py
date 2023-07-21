'''
    Please use this script to extract the thickness value from the geometry name
    and apply it in surface props.
    For proper functionality, it's important to use a colon (-) and [-]
    to separate the surface name and the thickness value.

    Example: [Surface Srf1 - 9.53]

    Developed by: Erick Braganca / Fernando Luiz
'''
# Function for thikness set
def setSurfaceThk(surface):
    # Get surface string name
    surface_name = surface.Name

    # Obtain the range where the numbe is placed
    start_index = surface_name.find("-") + 1
    end_index = surface_name.find("]", start_index)
    surface_thk_string = surface_name[start_index:end_index].strip()

    # Getting the result of validation name
    isOk = validateThkString(surface_thk_string)

    if isOk['state']:
        surface_thk_unit=" [mm]"
        surface_thk_value = surface_thk_string + surface_thk_unit
        surface_thk=Quantity(surface_thk_value)
        surface.Thickness=surface_thk

        print(surface_name, isOk['msg'])
    else:
        print(surface_name, isOk['msg'])
#-----------------------------------------#
# Function to validade thk string
def validateThkString(thk_value):
    hasComma = "," in thk_value
    hasLetter = any(let.isalpha() for let in thk_value)
    if hasComma:
        return {"state": False, "msg": "Has a comma in the surface name"}
    elif hasLetter:
        return {"state": False, "msg": "Has letter in the surface name"}
    else:
        return {"state": True, "msg": "Thk Setted"}
#-----------------------------------------#
def init():
    models = Model.Geometry.Children
    for model in models:
        surfaces =  model.Children
    for surface in surfaces:
        setSurfaceThk(surface)
#-----------------------------------------#
init()
