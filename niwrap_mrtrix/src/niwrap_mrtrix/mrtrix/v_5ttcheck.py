# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_5TTCHECK_METADATA = Metadata(
    id="81b3e0b2961a573a6a802146cca2c10ffb8d0868.boutiques",
    name="5ttcheck",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


V5ttcheckConfigParameters = typing.TypedDict('V5ttcheckConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


V5ttcheckParameters = typing.TypedDict('V5ttcheckParameters', {
    "__STYX_TYPE__": typing.Literal["5ttcheck"],
    "voxels": typing.NotRequired[str | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[V5ttcheckConfigParameters] | None],
    "help": bool,
    "version": bool,
    "input": list[InputPathType],
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
        "5ttcheck": v_5ttcheck_cargs,
        "config": v_5ttcheck_config_cargs,
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


def v_5ttcheck_config_params(
    key: str,
    value: str,
) -> V5ttcheckConfigParameters:
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


def v_5ttcheck_config_cargs(
    params: V5ttcheckConfigParameters,
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


class V5ttcheckOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_5ttcheck(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_5ttcheck_params(
    input_: list[InputPathType],
    voxels: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[V5ttcheckConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> V5ttcheckParameters:
    """
    Build parameters.
    
    Args:
        input_: the 5TT image(s) to be tested.
        voxels: output mask images highlighting voxels where the input does not\
            conform to 5TT requirements.
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
        "__STYXTYPE__": "5ttcheck",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "input": input_,
    }
    if voxels is not None:
        params["voxels"] = voxels
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def v_5ttcheck_cargs(
    params: V5ttcheckParameters,
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
    cargs.append("5ttcheck")
    if params.get("voxels") is not None:
        cargs.extend([
            "-voxels",
            params.get("voxels")
        ])
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
    cargs.extend([execution.input_file(f) for f in params.get("input")])
    return cargs


def v_5ttcheck_outputs(
    params: V5ttcheckParameters,
    execution: Execution,
) -> V5ttcheckOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V5ttcheckOutputs(
        root=execution.output_file("."),
    )
    return ret


def v_5ttcheck_execute(
    params: V5ttcheckParameters,
    execution: Execution,
) -> V5ttcheckOutputs:
    """
    Thoroughly check that one or more images conform to the expected ACT
    five-tissue-type (5TT) format.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V5ttcheckOutputs`).
    """
    params = execution.params(params)
    cargs = v_5ttcheck_cargs(params, execution)
    ret = v_5ttcheck_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_5ttcheck(
    input_: list[InputPathType],
    voxels: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[V5ttcheckConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> V5ttcheckOutputs:
    """
    Thoroughly check that one or more images conform to the expected ACT
    five-tissue-type (5TT) format.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        input_: the 5TT image(s) to be tested.
        voxels: output mask images highlighting voxels where the input does not\
            conform to 5TT requirements.
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
        NamedTuple of outputs (described in `V5ttcheckOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_5TTCHECK_METADATA)
    params = v_5ttcheck_params(
        voxels=voxels,
        info=info,
        quiet=quiet,
        debug=debug,
        force=force,
        nthreads=nthreads,
        config=config,
        help_=help_,
        version=version,
        input_=input_,
    )
    return v_5ttcheck_execute(params, execution)


__all__ = [
    "V5ttcheckConfigParameters",
    "V5ttcheckOutputs",
    "V5ttcheckParameters",
    "V_5TTCHECK_METADATA",
    "v_5ttcheck",
    "v_5ttcheck_config_params",
    "v_5ttcheck_params",
]
