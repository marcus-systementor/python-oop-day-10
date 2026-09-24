"""A working procedural TV program to inspect before building a class."""


def create_tv(brand):
    return {"brand": brand, "is_on": False, "volume": 10}


def turn_on(tv):
    tv["is_on"] = True


def increase_volume(tv):
    if tv["is_on"]:
        tv["volume"] += 1


def get_status(tv):
    return f"{tv['brand']}: on={tv['is_on']}, volume={tv['volume']}"


def main():
    first = create_tv("Nord")
    second = create_tv("Syd")
    turn_on(first)
    increase_volume(first)
    increase_volume(first)
    increase_volume(second)
    print(get_status(first))
    print(get_status(second))


if __name__ == "__main__":
    main()
