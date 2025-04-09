# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TSFDIVIDE_METADATA = Metadata(
    id="73b4285cd16d7ecd5b79ccc7ed4dd1e67b62377d.boutiques",
    name="tsfdivide",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


TsfdivideConfigParameters = typing.TypedDict('TsfdivideConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


TsfdivideParameters = typing.TypedDict('TsfdivideParameters', {
    "__STYX_TYPE__": typing.Literal["tsfdivide"],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[TsfdivideConfigParameters] | None],
    "help": bool,
    "version": bool,
    "input1": InputPathType,
    "input2": InputPathType,
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
        "tsfdivide": tsfdivide_cargs,
        "config": tsfdivide_config_cargs,
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
        "tsfdivide": tsfdivide_outputs,
    }.get(t)


def tsfdivide_config_params(
    key: str,
    value: str,
) -> TsfdivideConfigParameters:
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


def tsfdivide_config_cargs(
    params: TsfdivideConfigParameters,
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


class TsfdivideOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tsfdivide(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output track scalar file"""


def tsfdivide_params(
    input1: InputPathType,
    input2: InputPathType,
    output: str,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TsfdivideConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> TsfdivideParameters:
    """
    Build parameters.
    
    Args:
        input1: the first input track scalar file.
        input2: the second input track scalar file.
        output: the output track scalar file.
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
        "__STYXTYPE__": "tsfdivide",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "input1": input1,
        "input2": input2,
        "output": output,
    }
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def tsfdivide_cargs(
    params: TsfdivideParameters,
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
    cargs.append("tsfdivide")
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
    cargs.append(execution.input_file(params.get("input1")))
    cargs.append(execution.input_file(params.get("input2")))
    cargs.append(params.get("output"))
    return cargs


def tsfdivide_outputs(
    params: TsfdivideParameters,
    execution: Execution,
) -> TsfdivideOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TsfdivideOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("output")),
    )
    return ret


def tsfdivide_execute(
    params: TsfdivideParameters,
    execution: Execution,
) -> TsfdivideOutputs:
    """
    Divide corresponding values in track scalar files.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TsfdivideOutputs`).
    """
    params = execution.params(params)
    cargs = tsfdivide_cargs(params, execution)
    ret = tsfdivide_outputs(params, execution)
    execution.run(cargs)
    return ret


def tsfdivide(
    input1: InputPathType,
    input2: InputPathType,
    output: str,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TsfdivideConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> TsfdivideOutputs:
    """
    Divide corresponding values in track scalar files.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        input1: the first input track scalar file.
        input2: the second input track scalar file.
        output: the output track scalar file.
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
        NamedTuple of outputs (described in `TsfdivideOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TSFDIVIDE_METADATA)
    params = tsfdivide_params(
        info=info,
        quiet=quiet,
        debug=debug,
        force=force,
        nthreads=nthreads,
        config=config,
        help_=help_,
        version=version,
        input1=input1,
        input2=input2,
        output=output,
    )
    return tsfdivide_execute(params, execution)


__all__ = [
    "TSFDIVIDE_METADATA",
    "TsfdivideConfigParameters",
    "TsfdivideOutputs",
    "TsfdivideParameters",
    "tsfdivide",
    "tsfdivide_config_params",
    "tsfdivide_params",
]
