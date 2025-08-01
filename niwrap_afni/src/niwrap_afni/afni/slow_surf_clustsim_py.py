# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SLOW_SURF_CLUSTSIM_PY_METADATA = Metadata(
    id="ddeecc1fb59992d9c9426870d78e92238ec8b21a.boutiques",
    name="slow_surf_clustsim.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


SlowSurfClustsimPyParameters = typing.TypedDict('SlowSurfClustsimPyParameters', {
    "__STYXTYPE__": typing.Literal["slow_surf_clustsim.py"],
    "on_surface": typing.NotRequired[str | None],
    "save_script": typing.NotRequired[str | None],
    "print_script": bool,
    "uvar": typing.NotRequired[list[str] | None],
    "verbosity": typing.NotRequired[float | None],
    "help": bool,
    "hist": bool,
    "show_default_cvars": bool,
    "show_default_uvars": bool,
    "show_valid_opts": bool,
    "version": bool,
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
        "slow_surf_clustsim.py": slow_surf_clustsim_py_cargs,
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
    }.get(t)


class SlowSurfClustsimPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `slow_surf_clustsim_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def slow_surf_clustsim_py_params(
    on_surface: str | None = None,
    save_script: str | None = None,
    print_script: bool = False,
    uvar: list[str] | None = None,
    verbosity: float | None = None,
    help_: bool = False,
    hist: bool = False,
    show_default_cvars: bool = False,
    show_default_uvars: bool = False,
    show_valid_opts: bool = False,
    version: bool = False,
) -> SlowSurfClustsimPyParameters:
    """
    Build parameters.
    
    Args:
        on_surface: Start from noise on the surface (so no volume data is\
            involved).
        save_script: Save script to given file.
        print_script: Print script to terminal.
        uvar: Set the user variable (use -show_default_uvars to see user vars).\
            Example usage: -uvar spec_file sb23_lh_141_std.spec -uvar surf_vol\
            sb23_SurfVol_aligned+orig.
        verbosity: Set the verbosity level.
        help_: Show this help.
        hist: Show module history.
        show_default_cvars: List default control variables.
        show_default_uvars: List default user variables.
        show_valid_opts: List valid options.
        version: Show current version.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "slow_surf_clustsim.py",
        "print_script": print_script,
        "help": help_,
        "hist": hist,
        "show_default_cvars": show_default_cvars,
        "show_default_uvars": show_default_uvars,
        "show_valid_opts": show_valid_opts,
        "version": version,
    }
    if on_surface is not None:
        params["on_surface"] = on_surface
    if save_script is not None:
        params["save_script"] = save_script
    if uvar is not None:
        params["uvar"] = uvar
    if verbosity is not None:
        params["verbosity"] = verbosity
    return params


def slow_surf_clustsim_py_cargs(
    params: SlowSurfClustsimPyParameters,
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
    cargs.append("slow_surf_clustsim.py")
    if params.get("on_surface") is not None:
        cargs.extend([
            "-on_surface",
            params.get("on_surface")
        ])
    if params.get("save_script") is not None:
        cargs.extend([
            "-save_script",
            params.get("save_script")
        ])
    if params.get("print_script"):
        cargs.append("-print_script")
    if params.get("uvar") is not None:
        cargs.extend([
            "-uvar",
            *params.get("uvar")
        ])
    if params.get("verbosity") is not None:
        cargs.extend([
            "-verb",
            str(params.get("verbosity"))
        ])
    if params.get("help"):
        cargs.append("-help")
    if params.get("hist"):
        cargs.append("-hist")
    if params.get("show_default_cvars"):
        cargs.append("-show_default_cvars")
    if params.get("show_default_uvars"):
        cargs.append("-show_default_uvars")
    if params.get("show_valid_opts"):
        cargs.append("-show_valid_opts")
    if params.get("version"):
        cargs.append("-ver")
    return cargs


def slow_surf_clustsim_py_outputs(
    params: SlowSurfClustsimPyParameters,
    execution: Execution,
) -> SlowSurfClustsimPyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SlowSurfClustsimPyOutputs(
        root=execution.output_file("."),
    )
    return ret


def slow_surf_clustsim_py_execute(
    params: SlowSurfClustsimPyParameters,
    execution: Execution,
) -> SlowSurfClustsimPyOutputs:
    """
    Generate a tcsh script to run clustsim on surface.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SlowSurfClustsimPyOutputs`).
    """
    params = execution.params(params)
    cargs = slow_surf_clustsim_py_cargs(params, execution)
    ret = slow_surf_clustsim_py_outputs(params, execution)
    execution.run(cargs)
    return ret


def slow_surf_clustsim_py(
    on_surface: str | None = None,
    save_script: str | None = None,
    print_script: bool = False,
    uvar: list[str] | None = None,
    verbosity: float | None = None,
    help_: bool = False,
    hist: bool = False,
    show_default_cvars: bool = False,
    show_default_uvars: bool = False,
    show_valid_opts: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> SlowSurfClustsimPyOutputs:
    """
    Generate a tcsh script to run clustsim on surface.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        on_surface: Start from noise on the surface (so no volume data is\
            involved).
        save_script: Save script to given file.
        print_script: Print script to terminal.
        uvar: Set the user variable (use -show_default_uvars to see user vars).\
            Example usage: -uvar spec_file sb23_lh_141_std.spec -uvar surf_vol\
            sb23_SurfVol_aligned+orig.
        verbosity: Set the verbosity level.
        help_: Show this help.
        hist: Show module history.
        show_default_cvars: List default control variables.
        show_default_uvars: List default user variables.
        show_valid_opts: List valid options.
        version: Show current version.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SlowSurfClustsimPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SLOW_SURF_CLUSTSIM_PY_METADATA)
    params = slow_surf_clustsim_py_params(
        on_surface=on_surface,
        save_script=save_script,
        print_script=print_script,
        uvar=uvar,
        verbosity=verbosity,
        help_=help_,
        hist=hist,
        show_default_cvars=show_default_cvars,
        show_default_uvars=show_default_uvars,
        show_valid_opts=show_valid_opts,
        version=version,
    )
    return slow_surf_clustsim_py_execute(params, execution)


__all__ = [
    "SLOW_SURF_CLUSTSIM_PY_METADATA",
    "SlowSurfClustsimPyOutputs",
    "SlowSurfClustsimPyParameters",
    "slow_surf_clustsim_py",
    "slow_surf_clustsim_py_params",
]
