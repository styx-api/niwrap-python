# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRMATH_METADATA = Metadata(
    id="db96b07f1077adff39e302c1a364e5fdc77ddbc2.boutiques",
    name="mrmath",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


MrmathConfigParameters = typing.TypedDict('MrmathConfigParameters', {
    "__STYXTYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


MrmathParameters = typing.TypedDict('MrmathParameters', {
    "__STYXTYPE__": typing.Literal["mrmath"],
    "axis": typing.NotRequired[int | None],
    "keep_unary_axes": bool,
    "datatype": typing.NotRequired[str | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[MrmathConfigParameters] | None],
    "help": bool,
    "version": bool,
    "input": list[InputPathType],
    "operation": str,
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
        "mrmath": mrmath_cargs,
        "config": mrmath_config_cargs,
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
        "mrmath": mrmath_outputs,
    }.get(t)


def mrmath_config_params(
    key: str,
    value: str,
) -> MrmathConfigParameters:
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


def mrmath_config_cargs(
    params: MrmathConfigParameters,
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


class MrmathOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mrmath(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output image."""


def mrmath_params(
    input_: list[InputPathType],
    operation: str,
    output: str,
    axis: int | None = None,
    keep_unary_axes: bool = False,
    datatype: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrmathConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> MrmathParameters:
    """
    Build parameters.
    
    Args:
        input_: the input image(s).
        operation: the operation to apply, one of: mean, median, sum, product,\
            rms, norm, var, std, min, max, absmax, magmax.
        output: the output image.
        axis: perform operation along a specified axis of a single input image.
        keep_unary_axes: Keep unary axes in input images prior to calculating\
            the stats. The default is to wipe axes with single elements.
        datatype: specify output image data type. Valid choices are: float32,\
            float32le, float32be, float64, float64le, float64be, int64, uint64,\
            int64le, uint64le, int64be, uint64be, int32, uint32, int32le, uint32le,\
            int32be, uint32be, int16, uint16, int16le, uint16le, int16be, uint16be,\
            cfloat32, cfloat32le, cfloat32be, cfloat64, cfloat64le, cfloat64be,\
            int8, uint8, bit.
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
        "__STYXTYPE__": "mrmath",
        "keep_unary_axes": keep_unary_axes,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "input": input_,
        "operation": operation,
        "output": output,
    }
    if axis is not None:
        params["axis"] = axis
    if datatype is not None:
        params["datatype"] = datatype
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def mrmath_cargs(
    params: MrmathParameters,
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
    cargs.append("mrmath")
    if params.get("axis") is not None:
        cargs.extend([
            "-axis",
            str(params.get("axis"))
        ])
    if params.get("keep_unary_axes"):
        cargs.append("-keep_unary_axes")
    if params.get("datatype") is not None:
        cargs.extend([
            "-datatype",
            params.get("datatype")
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
    cargs.append(params.get("operation"))
    cargs.append(params.get("output"))
    return cargs


def mrmath_outputs(
    params: MrmathParameters,
    execution: Execution,
) -> MrmathOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrmathOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("output")),
    )
    return ret


def mrmath_execute(
    params: MrmathParameters,
    execution: Execution,
) -> MrmathOutputs:
    """
    Compute summary statistic on image intensities either across images, or along a
    specified axis of a single image.
    
    Supported operations are:
    
    mean, median, sum, product, rms (root-mean-square value), norm (vector
    2-norm), var (unbiased variance), std (unbiased standard deviation), min,
    max, absmax (maximum absolute value), magmax (value with maximum absolute
    value, preserving its sign).
    
    This command is used to traverse either along an image axis, or across a set
    of input images, calculating some statistic from the values along each
    traversal. If you are seeking to instead perform mathematical calculations
    that are done independently for each voxel, pleaase see the 'mrcalc'
    command.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrmathOutputs`).
    """
    params = execution.params(params)
    cargs = mrmath_cargs(params, execution)
    ret = mrmath_outputs(params, execution)
    execution.run(cargs)
    return ret


def mrmath(
    input_: list[InputPathType],
    operation: str,
    output: str,
    axis: int | None = None,
    keep_unary_axes: bool = False,
    datatype: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrmathConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MrmathOutputs:
    """
    Compute summary statistic on image intensities either across images, or along a
    specified axis of a single image.
    
    Supported operations are:
    
    mean, median, sum, product, rms (root-mean-square value), norm (vector
    2-norm), var (unbiased variance), std (unbiased standard deviation), min,
    max, absmax (maximum absolute value), magmax (value with maximum absolute
    value, preserving its sign).
    
    This command is used to traverse either along an image axis, or across a set
    of input images, calculating some statistic from the values along each
    traversal. If you are seeking to instead perform mathematical calculations
    that are done independently for each voxel, pleaase see the 'mrcalc'
    command.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        input_: the input image(s).
        operation: the operation to apply, one of: mean, median, sum, product,\
            rms, norm, var, std, min, max, absmax, magmax.
        output: the output image.
        axis: perform operation along a specified axis of a single input image.
        keep_unary_axes: Keep unary axes in input images prior to calculating\
            the stats. The default is to wipe axes with single elements.
        datatype: specify output image data type. Valid choices are: float32,\
            float32le, float32be, float64, float64le, float64be, int64, uint64,\
            int64le, uint64le, int64be, uint64be, int32, uint32, int32le, uint32le,\
            int32be, uint32be, int16, uint16, int16le, uint16le, int16be, uint16be,\
            cfloat32, cfloat32le, cfloat32be, cfloat64, cfloat64le, cfloat64be,\
            int8, uint8, bit.
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
        NamedTuple of outputs (described in `MrmathOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRMATH_METADATA)
    params = mrmath_params(
        axis=axis,
        keep_unary_axes=keep_unary_axes,
        datatype=datatype,
        info=info,
        quiet=quiet,
        debug=debug,
        force=force,
        nthreads=nthreads,
        config=config,
        help_=help_,
        version=version,
        input_=input_,
        operation=operation,
        output=output,
    )
    return mrmath_execute(params, execution)


__all__ = [
    "MRMATH_METADATA",
    "MrmathConfigParameters",
    "MrmathOutputs",
    "MrmathParameters",
    "mrmath",
    "mrmath_config_params",
    "mrmath_params",
]
