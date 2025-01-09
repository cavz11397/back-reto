import os
import yaml

# Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Ruta al archivo config.yaml
CONFIG_PATH = os.path.join(BASE_DIR, "config", "config.yaml")

def load_config(file_path: str):
    try:
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el archivo de configuración: {file_path}")
    except Exception as e:
        raise Exception(f"Error al cargar la configuración: {e}")

# Cargar configuración
config = load_config(CONFIG_PATH)


# Construir la URL de conexión
DATABASE_URL = (
    f"postgresql://{config['database']['user']}:{config['database']['password']}"
    f"@{config['database']['host']}:{config['database']['port']}/{config['database']['name']}"
)

SECRET_KEY = config['security']['secret_key']

ACCOUNTS_ROUTES = config['rutas']['accounts']
INVENTORY_ROUTES = config['rutas']['inventory']
ITEMS_ROUTES = config['rutas']['items']