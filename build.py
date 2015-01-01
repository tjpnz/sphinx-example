from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.sphinx")


name = "sphinx-example"
default_task = "publish"


@init
def set_properties(project):
    project.build_depends_on("mock")

    project.set_property("sphinx_config_path", "docs/")
    project.set_property("sphinx_source_dir", "docs/")
    project.set_property("sphinx_output_dir", "docs/_build")
