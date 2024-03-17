import json

from factorio_blueprints.blueprints import json_to_blueprint

DIRECTIONS = {
    "up": 0,
    "down": 4,
    "left": 6,
    "right": 2,
}


class Signal:
    def __init__(self, type, name):
        self.type = type
        self.name = name


class Icon:
    def __init__(self, signal, index):
        self.signal = signal
        self.index = index


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Entity:
    def __init__(
        self,
        entity_number,
        name,
        position,
        direction,
        entity_type=None,
        recipe=None,
        tags=None,
    ):
        self.entity_number = entity_number
        self.name = name
        self.position = position
        self.direction = direction
        self.type = entity_type
        self.recipe = recipe
        self.tags = tags


class Blueprint:
    def __init__(self, icons, entities, item, version):
        self.icons = icons
        self.entities = entities
        self.item = item
        self.version = version

    def to_json(self):
        return json.dumps(
            {"blueprint": self}, default=lambda o: o.__dict__, sort_keys=True, indent=4
        )


def test():
    with open("helmod/recipe.json", "r") as file:
        recipes = json.load(file)

    products = recipes["products"].items()
    icons = []
    for index, (product_name, product) in enumerate(products):
        signal = Signal(product["type"], product_name)
        icon = Icon(signal, index + 1)
        icons.append(icon)
    ingredients = recipes["ingredients"].items()
    entities = []
    # for request-depot only
    entity_number = 1

    for index, (ingredient_name, ingre) in enumerate(ingredients):
        y0 = 267.5
        x0 = 54.5
        # request-depot
        request_depot_delta_y = 3
        request_depot_direction = DIRECTIONS["right"]
        request_depot_x = x0
        request_depot_y = y0 + index * request_depot_delta_y
        request_depot = Entity(
            entity_number=entity_number,
            name="request-depot",
            position=Position(request_depot_x, request_depot_y),
            direction=request_depot_direction,
            recipe="request-" + ingredient_name,
            tags={"transport_depot_tags": {"drone_count": 10}},
        )
        entities.append(request_depot)
        entity_number += 1
        # fast-transport-belt-loader
        fast_transport_belt_loader_direction = DIRECTIONS["left"]
        fast_transport_belt_loader_x = request_depot_x - 2
        fast_transport_belt_loader_y = request_depot_y
        fast_transport_belt_loader = Entity(
            entity_number=entity_number,
            name="fast-transport-belt-loader",
            position=Position(
                fast_transport_belt_loader_x, fast_transport_belt_loader_y
            ),
            direction=fast_transport_belt_loader_direction,
            entity_type="output",
        )
        entities.append(fast_transport_belt_loader)
        entity_number += 1
        # fast-transport-belt next to fast-transport-belt-loader
        # fast_transport_belt_direction = (
        #     DIRECTIONS["down"] if index % 2 == 0 else DIRECTIONS["up"]
        # )
        fast_transport_belt_direction = DIRECTIONS["left"]
        fast_transport_belt_x = fast_transport_belt_loader_x - 1
        fast_transport_belt_y = fast_transport_belt_loader_y
        fast_transport_belt = Entity(
            entity_number=entity_number,
            name="fast-transport-belt",
            position=Position(fast_transport_belt_x, fast_transport_belt_y),
            direction=fast_transport_belt_direction,
        )
        entities.append(fast_transport_belt)
        entity_number += 1

    blueprint = Blueprint(icons, entities, "blueprint", 281479278493696)
    json_result = blueprint.to_json()
    with open("test.json", "w") as file:
        file.write(json_result)

    b64_result = json_to_blueprint(json_result)
    with open("test.txt", "w") as file:
        file.write(b64_result.decode("utf-8"))


if __name__ == "__main__":
    test()
