# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

WARPINIT_METADATA = Metadata(
    id="8d80b9573339b70a44a4d9c060f4b3d6a7b83231.boutiques",
    name="warpinit",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


WarpinitConfigParameters = typing.TypedDict('WarpinitConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


WarpinitParameters = typing.TypedDict('WarpinitParameters', {
    "__STYX_TYPE__": typing.Literal["warpinit"],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[WarpinitConfigParameters] | None],
    "help": bool,
    "version": bool,
    "template": InputPathType,
    "warp": str,
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
        "warpinit": warpinit_cargs,
        "config": warpinit_config_cargs,
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
        "warpinit": warpinit_outputs,
    }.get(t)


def warpinit_config_params(
    key: str,
    value: str,
) -> WarpinitConfigParameters:
    """
    Build parameters.
    
    Args:
        key: temporarily set the value of an MRtrix config file entry.
        value: temporarily set the value of an MRtrix config file entry.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "config",
        "key": key,
        "value": value,
    }
    return params


def warpinit_config_cargs(
    params: WarpinitConfigParameters,
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
    cargs.append("-config")
    cargs.append(params.get("key"))
    cargs.append(params.get("value"))
    return cargs


class WarpinitOutputs(typing.NamedTuple):
    """
    Output object returned when calling `warpinit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    warp: OutputPathType
    """the output warp image."""


def warpinit_params(
    template: InputPathType,
    warp: str,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[WarpinitConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> WarpinitParameters:
    """
    Build parameters.
    
    Args:
        template: the input template image.
        warp: the output warp image.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "warpinit",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "template": template,
        "warp": warp,
    }
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def warpinit_cargs(
    params: WarpinitParameters,
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
    cargs.append("warpinit")
    if params.get("info"):
        cargs.append("-info")
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("debug"):
        cargs.append("-debug")
    if params.get("force"):
        cargs.append("-force")
    if params.get("nthreads") is not None:
        cargs.extend([
            "-nthreads",
            str(params.get("nthreads"))
        ])
    if params.get("config") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("config")] for a in c])
    if params.get("help"):
        cargs.append("-help")
    if params.get("version"):
        cargs.append("-version")
    cargs.append(execution.input_file(params.get("template")))
    cargs.append(params.get("warp"))
    return cargs


def warpinit_outputs(
    params: WarpinitParameters,
    execution: Execution,
) -> WarpinitOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = WarpinitOutputs(
        root=execution.output_file("."),
        warp=execution.output_file(params.get("warp")),
    )
    return ret


def warpinit_execute(
    params: WarpinitParameters,
    execution: Execution,
) -> WarpinitOutputs:
    """
    Create an initial warp image, representing an identity transformation.
    
    This is useful to obtain the warp fields from other normalisation
    applications, by applying the transformation of interest to the warp field
    generated by this program.
    
    The image generated is a 4D image with the same spatial characteristics as
    the input template image. It contains 3 volumes, with each voxel containing
    its own x,y,z coordinates.
    
    Note that this command can be used to create 3 separate X,Y,Z images
    directly (which may be useful to create images suitable for use in the
    registration program) using the following syntax:
    
    $ warpinit template.mif warp-'[]'.nii
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `WarpinitOutputs`).
    """
    params = execution.params(params)
    cargs = warpinit_cargs(params, execution)
    ret = warpinit_outputs(params, execution)
    execution.run(cargs)
    return ret


def warpinit(
    template: InputPathType,
    warp: str,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[WarpinitConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> WarpinitOutputs:
    """
    Create an initial warp image, representing an identity transformation.
    
    This is useful to obtain the warp fields from other normalisation
    applications, by applying the transformation of interest to the warp field
    generated by this program.
    
    The image generated is a 4D image with the same spatial characteristics as
    the input template image. It contains 3 volumes, with each voxel containing
    its own x,y,z coordinates.
    
    Note that this command can be used to create 3 separate X,Y,Z images
    directly (which may be useful to create images suitable for use in the
    registration program) using the following syntax:
    
    $ warpinit template.mif warp-'[]'.nii
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        template: the input template image.
        warp: the output warp image.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `WarpinitOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(WARPINIT_METADATA)
    params = warpinit_params(
        info=info,
        quiet=quiet,
        debug=debug,
        force=force,
        nthreads=nthreads,
        config=config,
        help_=help_,
        version=version,
        template=template,
        warp=warp,
    )
    return warpinit_execute(params, execution)


__all__ = [
    "WARPINIT_METADATA",
    "WarpinitConfigParameters",
    "WarpinitOutputs",
    "WarpinitParameters",
    "warpinit",
    "warpinit_config_params",
    "warpinit_params",
]
