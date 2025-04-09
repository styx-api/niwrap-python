# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

LABELCONVERT_METADATA = Metadata(
    id="4568f3761d8faacbe019ad83a8f076b8f125f859.boutiques",
    name="labelconvert",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


LabelconvertConfigParameters = typing.TypedDict('LabelconvertConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


LabelconvertParameters = typing.TypedDict('LabelconvertParameters', {
    "__STYX_TYPE__": typing.Literal["labelconvert"],
    "spine": typing.NotRequired[InputPathType | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[LabelconvertConfigParameters] | None],
    "help": bool,
    "version": bool,
    "path_in": InputPathType,
    "lut_in": InputPathType,
    "lut_out": InputPathType,
    "image_out": str,
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
        "labelconvert": labelconvert_cargs,
        "config": labelconvert_config_cargs,
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
        "labelconvert": labelconvert_outputs,
    }.get(t)


def labelconvert_config_params(
    key: str,
    value: str,
) -> LabelconvertConfigParameters:
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


def labelconvert_config_cargs(
    params: LabelconvertConfigParameters,
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


class LabelconvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `labelconvert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    image_out: OutputPathType
    """the output image"""


def labelconvert_params(
    path_in: InputPathType,
    lut_in: InputPathType,
    lut_out: InputPathType,
    image_out: str,
    spine: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[LabelconvertConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> LabelconvertParameters:
    """
    Build parameters.
    
    Args:
        path_in: the input image.
        lut_in: the connectome lookup table corresponding to the input image.
        lut_out: the target connectome lookup table for the output image.
        image_out: the output image.
        spine: provide a manually-defined segmentation of the base of the spine\
            where the streamlines terminate, so that this can become a node in the\
            connection matrix.
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
        "__STYXTYPE__": "labelconvert",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "path_in": path_in,
        "lut_in": lut_in,
        "lut_out": lut_out,
        "image_out": image_out,
    }
    if spine is not None:
        params["spine"] = spine
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def labelconvert_cargs(
    params: LabelconvertParameters,
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
    cargs.append("labelconvert")
    if params.get("spine") is not None:
        cargs.extend([
            "-spine",
            execution.input_file(params.get("spine"))
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
    cargs.append(execution.input_file(params.get("path_in")))
    cargs.append(execution.input_file(params.get("lut_in")))
    cargs.append(execution.input_file(params.get("lut_out")))
    cargs.append(params.get("image_out"))
    return cargs


def labelconvert_outputs(
    params: LabelconvertParameters,
    execution: Execution,
) -> LabelconvertOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = LabelconvertOutputs(
        root=execution.output_file("."),
        image_out=execution.output_file(params.get("image_out")),
    )
    return ret


def labelconvert_execute(
    params: LabelconvertParameters,
    execution: Execution,
) -> LabelconvertOutputs:
    """
    Convert a connectome node image from one lookup table to another.
    
    Typical usage is to convert a parcellation image provided by some other
    software, based on the lookup table provided by that software, to conform to
    a new lookup table, particularly one where the node indices increment from
    1, in preparation for connectome construction; examples of such target
    lookup table files are provided in share//mrtrix3//labelconvert//, but can
    be created by the user to provide the desired node set // ordering //
    colours.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `LabelconvertOutputs`).
    """
    params = execution.params(params)
    cargs = labelconvert_cargs(params, execution)
    ret = labelconvert_outputs(params, execution)
    execution.run(cargs)
    return ret


def labelconvert(
    path_in: InputPathType,
    lut_in: InputPathType,
    lut_out: InputPathType,
    image_out: str,
    spine: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[LabelconvertConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> LabelconvertOutputs:
    """
    Convert a connectome node image from one lookup table to another.
    
    Typical usage is to convert a parcellation image provided by some other
    software, based on the lookup table provided by that software, to conform to
    a new lookup table, particularly one where the node indices increment from
    1, in preparation for connectome construction; examples of such target
    lookup table files are provided in share//mrtrix3//labelconvert//, but can
    be created by the user to provide the desired node set // ordering //
    colours.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        path_in: the input image.
        lut_in: the connectome lookup table corresponding to the input image.
        lut_out: the target connectome lookup table for the output image.
        image_out: the output image.
        spine: provide a manually-defined segmentation of the base of the spine\
            where the streamlines terminate, so that this can become a node in the\
            connection matrix.
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
        NamedTuple of outputs (described in `LabelconvertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABELCONVERT_METADATA)
    params = labelconvert_params(
        spine=spine,
        info=info,
        quiet=quiet,
        debug=debug,
        force=force,
        nthreads=nthreads,
        config=config,
        help_=help_,
        version=version,
        path_in=path_in,
        lut_in=lut_in,
        lut_out=lut_out,
        image_out=image_out,
    )
    return labelconvert_execute(params, execution)


__all__ = [
    "LABELCONVERT_METADATA",
    "LabelconvertConfigParameters",
    "LabelconvertOutputs",
    "LabelconvertParameters",
    "labelconvert",
    "labelconvert_config_params",
    "labelconvert_params",
]
