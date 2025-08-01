# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TCKSTATS_METADATA = Metadata(
    id="5978fa2db061f719e30d3e2617f6bb60e013d444.boutiques",
    name="tckstats",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


TckstatsOutputParameters = typing.TypedDict('TckstatsOutputParameters', {
    "__STYXTYPE__": typing.Literal["output"],
    "field": str,
})


TckstatsConfigParameters = typing.TypedDict('TckstatsConfigParameters', {
    "__STYXTYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


TckstatsParameters = typing.TypedDict('TckstatsParameters', {
    "__STYXTYPE__": typing.Literal["tckstats"],
    "output": typing.NotRequired[list[TckstatsOutputParameters] | None],
    "histogram": typing.NotRequired[str | None],
    "dump": typing.NotRequired[str | None],
    "ignorezero": bool,
    "tck_weights_in": typing.NotRequired[InputPathType | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[TckstatsConfigParameters] | None],
    "help": bool,
    "version": bool,
    "tracks_in": InputPathType,
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
        "tckstats": tckstats_cargs,
        "output": tckstats_output_cargs,
        "config": tckstats_config_cargs,
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
        "tckstats": tckstats_outputs,
    }.get(t)


def tckstats_output_params(
    field: str,
) -> TckstatsOutputParameters:
    """
    Build parameters.
    
    Args:
        field: output only the field specified. Multiple such options can be\
            supplied if required. Choices are: mean, median, std, min, max, count.\
            Useful for use in scripts.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "output",
        "field": field,
    }
    return params


def tckstats_output_cargs(
    params: TckstatsOutputParameters,
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
    cargs.append("-output")
    cargs.append(params.get("field"))
    return cargs


def tckstats_config_params(
    key: str,
    value: str,
) -> TckstatsConfigParameters:
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


def tckstats_config_cargs(
    params: TckstatsConfigParameters,
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


class TckstatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tckstats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    histogram: OutputPathType | None
    """output a histogram of streamline lengths """
    dump: OutputPathType | None
    """dump the streamlines lengths to a text file """


def tckstats_params(
    tracks_in: InputPathType,
    output: list[TckstatsOutputParameters] | None = None,
    histogram: str | None = None,
    dump: str | None = None,
    ignorezero: bool = False,
    tck_weights_in: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TckstatsConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> TckstatsParameters:
    """
    Build parameters.
    
    Args:
        tracks_in: the input track file.
        output: output only the field specified. Multiple such options can be\
            supplied if required. Choices are: mean, median, std, min, max, count.\
            Useful for use in scripts.
        histogram: output a histogram of streamline lengths.
        dump: dump the streamlines lengths to a text file.
        ignorezero: do not generate a warning if the track file contains\
            streamlines with zero length.
        tck_weights_in: specify a text scalar file containing the streamline\
            weights.
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
        "__STYXTYPE__": "tckstats",
        "ignorezero": ignorezero,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "tracks_in": tracks_in,
    }
    if output is not None:
        params["output"] = output
    if histogram is not None:
        params["histogram"] = histogram
    if dump is not None:
        params["dump"] = dump
    if tck_weights_in is not None:
        params["tck_weights_in"] = tck_weights_in
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def tckstats_cargs(
    params: TckstatsParameters,
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
    cargs.append("tckstats")
    if params.get("output") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("output")] for a in c])
    if params.get("histogram") is not None:
        cargs.extend([
            "-histogram",
            params.get("histogram")
        ])
    if params.get("dump") is not None:
        cargs.extend([
            "-dump",
            params.get("dump")
        ])
    if params.get("ignorezero"):
        cargs.append("-ignorezero")
    if params.get("tck_weights_in") is not None:
        cargs.extend([
            "-tck_weights_in",
            execution.input_file(params.get("tck_weights_in"))
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
    cargs.append(execution.input_file(params.get("tracks_in")))
    return cargs


def tckstats_outputs(
    params: TckstatsParameters,
    execution: Execution,
) -> TckstatsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TckstatsOutputs(
        root=execution.output_file("."),
        histogram=execution.output_file(params.get("histogram")) if (params.get("histogram") is not None) else None,
        dump=execution.output_file(params.get("dump")) if (params.get("dump") is not None) else None,
    )
    return ret


def tckstats_execute(
    params: TckstatsParameters,
    execution: Execution,
) -> TckstatsOutputs:
    """
    Calculate statistics on streamlines lengths.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TckstatsOutputs`).
    """
    params = execution.params(params)
    cargs = tckstats_cargs(params, execution)
    ret = tckstats_outputs(params, execution)
    execution.run(cargs)
    return ret


def tckstats(
    tracks_in: InputPathType,
    output: list[TckstatsOutputParameters] | None = None,
    histogram: str | None = None,
    dump: str | None = None,
    ignorezero: bool = False,
    tck_weights_in: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TckstatsConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> TckstatsOutputs:
    """
    Calculate statistics on streamlines lengths.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        tracks_in: the input track file.
        output: output only the field specified. Multiple such options can be\
            supplied if required. Choices are: mean, median, std, min, max, count.\
            Useful for use in scripts.
        histogram: output a histogram of streamline lengths.
        dump: dump the streamlines lengths to a text file.
        ignorezero: do not generate a warning if the track file contains\
            streamlines with zero length.
        tck_weights_in: specify a text scalar file containing the streamline\
            weights.
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
        NamedTuple of outputs (described in `TckstatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TCKSTATS_METADATA)
    params = tckstats_params(
        output=output,
        histogram=histogram,
        dump=dump,
        ignorezero=ignorezero,
        tck_weights_in=tck_weights_in,
        info=info,
        quiet=quiet,
        debug=debug,
        force=force,
        nthreads=nthreads,
        config=config,
        help_=help_,
        version=version,
        tracks_in=tracks_in,
    )
    return tckstats_execute(params, execution)


__all__ = [
    "TCKSTATS_METADATA",
    "TckstatsConfigParameters",
    "TckstatsOutputParameters",
    "TckstatsOutputs",
    "TckstatsParameters",
    "tckstats",
    "tckstats_config_params",
    "tckstats_output_params",
    "tckstats_params",
]
