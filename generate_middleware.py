import configparser
from jinja2 import Environment, FileSystemLoader


def generate_middleware_code(middleware_name, log_route, use_subrequest):
    class_name = middleware_name.title().replace("_", "") + "Middleware"

    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("middleware_template.j2")

    middleware_code = template.render(
        class_name=class_name,
        middleware_name=middleware_name,
        log_route=log_route,
        use_subrequest=use_subrequest,
    )
    return middleware_code


def main():
    config = configparser.ConfigParser()
    config.read("/config/config.ini")

    middleware_name = config["settings"]["middleware_name"]
    log_route = config["settings"]["log_route"]
    use_subrequest = config["settings"].getboolean("use_subrequest")

    middleware_code = generate_middleware_code(
        middleware_name, log_route, use_subrequest
    )

    file_name = f"/output/{middleware_name}.py"
    with open(file_name, "w") as file:
        file.write(middleware_code)
    print(f"کد در فایل '{file_name}' ذخیره شد.")


if __name__ == "__main__":
    main()
