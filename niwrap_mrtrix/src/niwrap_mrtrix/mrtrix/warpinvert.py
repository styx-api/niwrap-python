# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

WARPINVERT_METADATA = Metadata(
    id="f3a20aeefbc1d48a0c5c2320a9ad61ef6bb94f89.boutiques",
    name="warpinvert",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


WarpinvertConfigParameters = typing.TypedDict('WarpinvertConfigParameters', {
    "__STYXTYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


WarpinvertParameters = typing.TypedDict('WarpinvertParameters', {
    "__STYXTYPE__": typing.Literal["warpinvert"],
    "template": typing.NotRequired[InputPathType | None],
    "displacement": bool,
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[WarpinvertConfigParameters] | None],
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
        "warpinvert": warpinvert_cargs,
        "config": warpinvert_config_cargs,
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
        "warpinvert": warpinvert_outputs,
    }.get(t)


def warpinvert_config_params(
    key: str,
    value: str,
) -> WarpinvertConfigParameters:
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


def warpinvert_config_cargs(
    params: WarpinvertConfigParameters,
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


class WarpinvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `warpinvert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out: OutputPathType
    """the output warp image."""


def warpinvert_params(
    in_: InputPathType,
    out: str,
    template: InputPathType | None = None,
    displacement: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[WarpinvertConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> WarpinvertParameters:
    """
    Build parameters.
    
    Args:
        in_: the input warp image.
        out: the output warp image.
        template: define a template image grid for the output warp.
        displacement: indicates that the input warp field is a displacement\
            field; the output will also be a displacement field.
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
        "__STYXTYPE__": "warpinvert",
        "displacement": displacement,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "in": in_,
        "out": out,
    }
    if template is not None:
        params["template"] = template
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def warpinvert_cargs(
    params: WarpinvertParameters,
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
    cargs.append("warpinvert")
    if params.get("template") is not None:
        cargs.extend([
            "-template",
            execution.input_file(params.get("template"))
        ])
    if params.get("displacement"):
        cargs.append("-displacement")
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


def warpinvert_outputs(
    params: WarpinvertParameters,
    execution: Execution,
) -> WarpinvertOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = WarpinvertOutputs(
        root=execution.output_file("."),
        out=execution.output_file(params.get("out")),
    )
    return ret


def warpinvert_execute(
    params: WarpinvertParameters,
    execution: Execution,
) -> WarpinvertOutputs:
    """
    Invert a non-linear warp field.
    
    By default, this command assumes that the input warp field is a deformation
    field, i.e. each voxel stores the corresponding position in the other image
    (in scanner space), and the calculated output warp image will also be a
    deformation field. If the input warp field is instead a displacment field,
    i.e. where each voxel stores an offset from which to sample the other image
    (but still in scanner space), then the -displacement option should be used;
    the output warp field will additionally be calculated as a displacement
    field in this case.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `WarpinvertOutputs`).
    """
    params = execution.params(params)
    cargs = warpinvert_cargs(params, execution)
    ret = warpinvert_outputs(params, execution)
    execution.run(cargs)
    return ret


def warpinvert(
    in_: InputPathType,
    out: str,
    template: InputPathType | None = None,
    displacement: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[WarpinvertConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> WarpinvertOutputs:
    """
    Invert a non-linear warp field.
    
    By default, this command assumes that the input warp field is a deformation
    field, i.e. each voxel stores the corresponding position in the other image
    (in scanner space), and the calculated output warp image will also be a
    deformation field. If the input warp field is instead a displacment field,
    i.e. where each voxel stores an offset from which to sample the other image
    (but still in scanner space), then the -displacement option should be used;
    the output warp field will additionally be calculated as a displacement
    field in this case.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        in_: the input warp image.
        out: the output warp image.
        template: define a template image grid for the output warp.
        displacement: indicates that the input warp field is a displacement\
            field; the output will also be a displacement field.
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
        NamedTuple of outputs (described in `WarpinvertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(WARPINVERT_METADATA)
    params = warpinvert_params(
        template=template,
        displacement=displacement,
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
    return warpinvert_execute(params, execution)


__all__ = [
    "WARPINVERT_METADATA",
    "WarpinvertConfigParameters",
    "WarpinvertOutputs",
    "WarpinvertParameters",
    "warpinvert",
    "warpinvert_config_params",
    "warpinvert_params",
]
