# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRCHECKERBOARDMASK_METADATA = Metadata(
    id="a3b0ea1bbc979f69d0d7f7f9d44b33ccf51605d8.boutiques",
    name="mrcheckerboardmask",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


MrcheckerboardmaskConfigParameters = typing.TypedDict('MrcheckerboardmaskConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


MrcheckerboardmaskParameters = typing.TypedDict('MrcheckerboardmaskParameters', {
    "__STYX_TYPE__": typing.Literal["mrcheckerboardmask"],
    "tiles": typing.NotRequired[int | None],
    "invert": bool,
    "nan": bool,
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[MrcheckerboardmaskConfigParameters] | None],
    "help": bool,
    "version": bool,
    "input": InputPathType,
    "output": str,
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
        "mrcheckerboardmask": mrcheckerboardmask_cargs,
        "config": mrcheckerboardmask_config_cargs,
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
        "mrcheckerboardmask": mrcheckerboardmask_outputs,
    }.get(t)


def mrcheckerboardmask_config_params(
    key: str,
    value: str,
) -> MrcheckerboardmaskConfigParameters:
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


def mrcheckerboardmask_config_cargs(
    params: MrcheckerboardmaskConfigParameters,
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


class MrcheckerboardmaskOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mrcheckerboardmask(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output binary image mask."""


def mrcheckerboardmask_params(
    input_: InputPathType,
    output: str,
    tiles: int | None = None,
    invert: bool = False,
    nan: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrcheckerboardmaskConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> MrcheckerboardmaskParameters:
    """
    Build parameters.
    
    Args:
        input_: the input image to be used as a template.
        output: the output binary image mask.
        tiles: specify the number of tiles in any direction.
        invert: invert output binary mask.
        nan: use NaN as the output zero value.
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
        "__STYXTYPE__": "mrcheckerboardmask",
        "invert": invert,
        "nan": nan,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "input": input_,
        "output": output,
    }
    if tiles is not None:
        params["tiles"] = tiles
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def mrcheckerboardmask_cargs(
    params: MrcheckerboardmaskParameters,
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
    cargs.append("mrcheckerboardmask")
    if params.get("tiles") is not None:
        cargs.extend([
            "-tiles",
            str(params.get("tiles"))
        ])
    if params.get("invert"):
        cargs.append("-invert")
    if params.get("nan"):
        cargs.append("-nan")
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
    cargs.append(execution.input_file(params.get("input")))
    cargs.append(params.get("output"))
    return cargs


def mrcheckerboardmask_outputs(
    params: MrcheckerboardmaskParameters,
    execution: Execution,
) -> MrcheckerboardmaskOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrcheckerboardmaskOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("output")),
    )
    return ret


def mrcheckerboardmask_execute(
    params: MrcheckerboardmaskParameters,
    execution: Execution,
) -> MrcheckerboardmaskOutputs:
    """
    Create bitwise checkerboard image.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrcheckerboardmaskOutputs`).
    """
    params = execution.params(params)
    cargs = mrcheckerboardmask_cargs(params, execution)
    ret = mrcheckerboardmask_outputs(params, execution)
    execution.run(cargs)
    return ret


def mrcheckerboardmask(
    input_: InputPathType,
    output: str,
    tiles: int | None = None,
    invert: bool = False,
    nan: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrcheckerboardmaskConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MrcheckerboardmaskOutputs:
    """
    Create bitwise checkerboard image.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        input_: the input image to be used as a template.
        output: the output binary image mask.
        tiles: specify the number of tiles in any direction.
        invert: invert output binary mask.
        nan: use NaN as the output zero value.
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
        NamedTuple of outputs (described in `MrcheckerboardmaskOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRCHECKERBOARDMASK_METADATA)
    params = mrcheckerboardmask_params(
        tiles=tiles,
        invert=invert,
        nan=nan,
        info=info,
        quiet=quiet,
        debug=debug,
        force=force,
        nthreads=nthreads,
        config=config,
        help_=help_,
        version=version,
        input_=input_,
        output=output,
    )
    return mrcheckerboardmask_execute(params, execution)


__all__ = [
    "MRCHECKERBOARDMASK_METADATA",
    "MrcheckerboardmaskConfigParameters",
    "MrcheckerboardmaskOutputs",
    "MrcheckerboardmaskParameters",
    "mrcheckerboardmask",
    "mrcheckerboardmask_config_params",
    "mrcheckerboardmask_params",
]
