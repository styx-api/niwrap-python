# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__AFNI_R_PACKAGE_INSTALL_METADATA = Metadata(
    id="cbebf13217e6c26c27782fa62a21100bbdcabaf7.boutiques",
    name="@afni_R_package_install",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VAfniRPackageInstallParameters = typing.TypedDict('VAfniRPackageInstallParameters', {
    "__STYX_TYPE__": typing.Literal["@afni_R_package_install"],
    "afni": bool,
    "shiny": bool,
    "bayes_view": bool,
    "circos": bool,
    "custom_packages": typing.NotRequired[str | None],
    "mirror": typing.NotRequired[str | None],
    "help": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "@afni_R_package_install": v__afni_r_package_install_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "@afni_R_package_install": v__afni_r_package_install_outputs,
    }.get(t)


class VAfniRPackageInstallOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__afni_r_package_install(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    install_log: OutputPathType
    """A log file listing all installed R packages."""


def v__afni_r_package_install_params(
    afni: bool = False,
    shiny: bool = False,
    bayes_view: bool = False,
    circos: bool = False,
    custom_packages: str | None = None,
    mirror: str | None = None,
    help_: bool = False,
) -> VAfniRPackageInstallParameters:
    """
    Build parameters.
    
    Args:
        afni: Install AFNI related R packages.
        shiny: Install AFNI related shiny app packages.
        bayes_view: Install R packages for bayes_view.
        circos: Install OmicCircos for FATCAT_matplot.
        custom_packages: Install custom R packages (space-separated list). Must\
            start and end with double quotes.
        mirror: Set the CRAN mirror to a custom URL.
        help_: Show help message.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@afni_R_package_install",
        "afni": afni,
        "shiny": shiny,
        "bayes_view": bayes_view,
        "circos": circos,
        "help": help_,
    }
    if custom_packages is not None:
        params["custom_packages"] = custom_packages
    if mirror is not None:
        params["mirror"] = mirror
    return params


def v__afni_r_package_install_cargs(
    params: VAfniRPackageInstallParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("@afni_R_package_install")
    if params.get("afni"):
        cargs.append("-afni")
    if params.get("shiny"):
        cargs.append("-shiny")
    if params.get("bayes_view"):
        cargs.append("-bayes_view")
    if params.get("circos"):
        cargs.append("-circos")
    if params.get("custom_packages") is not None:
        cargs.extend([
            "-custom",
            params.get("custom_packages")
        ])
    if params.get("mirror") is not None:
        cargs.extend([
            "-mirror",
            params.get("mirror")
        ])
    if params.get("help"):
        cargs.append("-help")
    return cargs


def v__afni_r_package_install_outputs(
    params: VAfniRPackageInstallParameters,
    execution: Execution,
) -> VAfniRPackageInstallOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VAfniRPackageInstallOutputs(
        root=execution.output_file("."),
        install_log=execution.output_file("R_packages_installed.txt"),
    )
    return ret


def v__afni_r_package_install_execute(
    params: VAfniRPackageInstallParameters,
    execution: Execution,
) -> VAfniRPackageInstallOutputs:
    """
    Helper script to install R packages for various afni-ish purposes.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VAfniRPackageInstallOutputs`).
    """
    params = execution.params(params)
    cargs = v__afni_r_package_install_cargs(params, execution)
    ret = v__afni_r_package_install_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__afni_r_package_install(
    afni: bool = False,
    shiny: bool = False,
    bayes_view: bool = False,
    circos: bool = False,
    custom_packages: str | None = None,
    mirror: str | None = None,
    help_: bool = False,
    runner: Runner | None = None,
) -> VAfniRPackageInstallOutputs:
    """
    Helper script to install R packages for various afni-ish purposes.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        afni: Install AFNI related R packages.
        shiny: Install AFNI related shiny app packages.
        bayes_view: Install R packages for bayes_view.
        circos: Install OmicCircos for FATCAT_matplot.
        custom_packages: Install custom R packages (space-separated list). Must\
            start and end with double quotes.
        mirror: Set the CRAN mirror to a custom URL.
        help_: Show help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VAfniRPackageInstallOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__AFNI_R_PACKAGE_INSTALL_METADATA)
    params = v__afni_r_package_install_params(
        afni=afni,
        shiny=shiny,
        bayes_view=bayes_view,
        circos=circos,
        custom_packages=custom_packages,
        mirror=mirror,
        help_=help_,
    )
    return v__afni_r_package_install_execute(params, execution)


__all__ = [
    "VAfniRPackageInstallOutputs",
    "VAfniRPackageInstallParameters",
    "V__AFNI_R_PACKAGE_INSTALL_METADATA",
    "v__afni_r_package_install",
    "v__afni_r_package_install_params",
]
