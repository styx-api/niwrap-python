# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TSFINFO_METADATA = Metadata(
    id="45e3911b111372c34cdd626a6ab7dceee95afdc9.boutiques",
    name="tsfinfo",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


TsfinfoConfigParameters = typing.TypedDict('TsfinfoConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


TsfinfoParameters = typing.TypedDict('TsfinfoParameters', {
    "__STYX_TYPE__": typing.Literal["tsfinfo"],
    "count": bool,
    "ascii": typing.NotRequired[str | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[TsfinfoConfigParameters] | None],
    "help": bool,
    "version": bool,
    "tracks": list[InputPathType],
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
        "tsfinfo": tsfinfo_cargs,
        "config": tsfinfo_config_cargs,
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


def tsfinfo_config_params(
    key: str,
    value: str,
) -> TsfinfoConfigParameters:
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


def tsfinfo_config_cargs(
    params: TsfinfoConfigParameters,
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


class TsfinfoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tsfinfo(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def tsfinfo_params(
    tracks: list[InputPathType],
    count: bool = False,
    ascii_: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TsfinfoConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> TsfinfoParameters:
    """
    Build parameters.
    
    Args:
        tracks: the input track scalar file.
        count: count number of tracks in file explicitly, ignoring the header.
        ascii_: save values of each track scalar file in individual ascii\
            files, with the specified prefix.
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
        "__STYXTYPE__": "tsfinfo",
        "count": count,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "tracks": tracks,
    }
    if ascii_ is not None:
        params["ascii"] = ascii_
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def tsfinfo_cargs(
    params: TsfinfoParameters,
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
    cargs.append("tsfinfo")
    if params.get("count"):
        cargs.append("-count")
    if params.get("ascii") is not None:
        cargs.extend([
            "-ascii",
            params.get("ascii")
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
    cargs.extend([execution.input_file(f) for f in params.get("tracks")])
    return cargs


def tsfinfo_outputs(
    params: TsfinfoParameters,
    execution: Execution,
) -> TsfinfoOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TsfinfoOutputs(
        root=execution.output_file("."),
    )
    return ret


def tsfinfo_execute(
    params: TsfinfoParameters,
    execution: Execution,
) -> TsfinfoOutputs:
    """
    Print out information about a track scalar file.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TsfinfoOutputs`).
    """
    params = execution.params(params)
    cargs = tsfinfo_cargs(params, execution)
    ret = tsfinfo_outputs(params, execution)
    execution.run(cargs)
    return ret


def tsfinfo(
    tracks: list[InputPathType],
    count: bool = False,
    ascii_: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TsfinfoConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> TsfinfoOutputs:
    """
    Print out information about a track scalar file.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        tracks: the input track scalar file.
        count: count number of tracks in file explicitly, ignoring the header.
        ascii_: save values of each track scalar file in individual ascii\
            files, with the specified prefix.
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
        NamedTuple of outputs (described in `TsfinfoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TSFINFO_METADATA)
    params = tsfinfo_params(
        count=count,
        ascii_=ascii_,
        info=info,
        quiet=quiet,
        debug=debug,
        force=force,
        nthreads=nthreads,
        config=config,
        help_=help_,
        version=version,
        tracks=tracks,
    )
    return tsfinfo_execute(params, execution)


__all__ = [
    "TSFINFO_METADATA",
    "TsfinfoConfigParameters",
    "TsfinfoOutputs",
    "TsfinfoParameters",
    "tsfinfo",
    "tsfinfo_config_params",
    "tsfinfo_params",
]
