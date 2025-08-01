# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DIRFLIP_METADATA = Metadata(
    id="1bc40c1342a5e6b2fe13e011f0393b92cd599ded.boutiques",
    name="dirflip",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


DirflipConfigParameters = typing.TypedDict('DirflipConfigParameters', {
    "__STYXTYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


DirflipParameters = typing.TypedDict('DirflipParameters', {
    "__STYXTYPE__": typing.Literal["dirflip"],
    "permutations": typing.NotRequired[int | None],
    "cartesian": bool,
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[DirflipConfigParameters] | None],
    "help": bool,
    "version": bool,
    "in": InputPathType,
    "out": str,
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
        "dirflip": dirflip_cargs,
        "config": dirflip_config_cargs,
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
        "dirflip": dirflip_outputs,
    }.get(t)


def dirflip_config_params(
    key: str,
    value: str,
) -> DirflipConfigParameters:
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


def dirflip_config_cargs(
    params: DirflipConfigParameters,
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


class DirflipOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dirflip(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out: OutputPathType
    """the output files for the directions."""


def dirflip_params(
    in_: InputPathType,
    out: str,
    permutations: int | None = None,
    cartesian: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[DirflipConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> DirflipParameters:
    """
    Build parameters.
    
    Args:
        in_: the input files for the directions.
        out: the output files for the directions.
        permutations: number of permutations to try (default: 100000000).
        cartesian: Output the directions in Cartesian coordinates [x y z]\
            instead of [az el].
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
        "__STYXTYPE__": "dirflip",
        "cartesian": cartesian,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "in": in_,
        "out": out,
    }
    if permutations is not None:
        params["permutations"] = permutations
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def dirflip_cargs(
    params: DirflipParameters,
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
    cargs.append("dirflip")
    if params.get("permutations") is not None:
        cargs.extend([
            "-permutations",
            str(params.get("permutations"))
        ])
    if params.get("cartesian"):
        cargs.append("-cartesian")
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
    cargs.append(execution.input_file(params.get("in")))
    cargs.append(params.get("out"))
    return cargs


def dirflip_outputs(
    params: DirflipParameters,
    execution: Execution,
) -> DirflipOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DirflipOutputs(
        root=execution.output_file("."),
        out=execution.output_file(params.get("out")),
    )
    return ret


def dirflip_execute(
    params: DirflipParameters,
    execution: Execution,
) -> DirflipOutputs:
    """
    Invert the polarity of individual directions so as to optimise a unipolar
    electrostatic repulsion model.
    
    The orientations themselves are not affected, only their polarity; this is
    necessary to ensure near-optimal distribution of DW directions for
    eddy-current correction.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DirflipOutputs`).
    """
    params = execution.params(params)
    cargs = dirflip_cargs(params, execution)
    ret = dirflip_outputs(params, execution)
    execution.run(cargs)
    return ret


def dirflip(
    in_: InputPathType,
    out: str,
    permutations: int | None = None,
    cartesian: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[DirflipConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> DirflipOutputs:
    """
    Invert the polarity of individual directions so as to optimise a unipolar
    electrostatic repulsion model.
    
    The orientations themselves are not affected, only their polarity; this is
    necessary to ensure near-optimal distribution of DW directions for
    eddy-current correction.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        in_: the input files for the directions.
        out: the output files for the directions.
        permutations: number of permutations to try (default: 100000000).
        cartesian: Output the directions in Cartesian coordinates [x y z]\
            instead of [az el].
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
        NamedTuple of outputs (described in `DirflipOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DIRFLIP_METADATA)
    params = dirflip_params(
        permutations=permutations,
        cartesian=cartesian,
        info=info,
        quiet=quiet,
        debug=debug,
        force=force,
        nthreads=nthreads,
        config=config,
        help_=help_,
        version=version,
        in_=in_,
        out=out,
    )
    return dirflip_execute(params, execution)


__all__ = [
    "DIRFLIP_METADATA",
    "DirflipConfigParameters",
    "DirflipOutputs",
    "DirflipParameters",
    "dirflip",
    "dirflip_config_params",
    "dirflip_params",
]
