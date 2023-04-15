from os      import environ
from os.path import join, dirname
from dotenv  import load_dotenv

from decorators import exception

ENV_FILE = "../.env"

#### Load .env
@exception
def load_env() -> None:
  env_file = join(dirname(__file__), ENV_FILE)
  load_dotenv(env_file)
load_env()

#### Read all shell variables
env = dict()
for k,v in environ.items():
  env[k]  = v

#### Unit Test
if __name__ == "__main__":
  print(env)