"""this module defines internal paths used by program and is safe to import before dependencies are installed in launch.py"""

import argparse
import os

script_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sd_configs_path = os.path.join(script_path, "configs")
sd_default_config = os.path.join(sd_configs_path, "v1-inference.yaml")
sd_model_file = os.path.join(script_path, 'model.ckpt')
default_sd_model_file = sd_model_file

# Parse the --data-dir flag first so we can use it as a base for our other argument default values
parser_pre = argparse.ArgumentParser(add_help=False)
parser_pre.add_argument("--data-dir", type=str, default=os.path.dirname(os.path.dirname(os.path.realpath(__file__))), help="base path where all user data is stored",)
parser_pre.add_argument("--models-dir", type=str, default="models", help="base path where all models are stored",)
cmd_opts_pre = parser_pre.parse_known_args()[0]
data_path = cmd_opts_pre.data_dir

models_path = os.path.join(cmd_opts_pre.models_dir)
extensions_dir = os.path.join(data_path, "extensions")
extensions_builtin_dir = os.path.join(data_path, "extensions-builtin")
