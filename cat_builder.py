# function catBuilder(name, color, toys) {
#   const cat = {
#     name: name,
#     color: color,
#     toys: toys
#   };

#   return cat;
# }

def cat_builder(name, color, toys):
    cat = {
        'name': name,
        'color': color,
        'toys': toys
    }

    return cat


print(cat_builder('Piper', 'white', 'hairties'))

# function catBuilder(name, color, toys) {
#   const cat = {};

#   cat.name = name;
#   cat.color = color;
#   cat.toys = toys;

#   return cat;
# }


def cat_builder_2(name, color, toys):
    cat = {}

    cat.name = name
    cat.color = color
    cat.toys = toys

    return cat


print(cat_builder_2('Piper', 'white', 'hairties'))
