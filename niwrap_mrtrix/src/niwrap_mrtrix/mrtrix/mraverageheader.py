# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRAVERAGEHEADER_METADATA = Metadata(
    id="fd2f9326c744f341eb6c33d25cde30666d1d4b4f.boutiques",
    name="mraverageheader",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


MraverageheaderConfigParameters = typing.TypedDict('MraverageheaderConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


MraverageheaderParameters = typing.TypedDict('MraverageheaderParameters', {
    "__STYX_TYPE__": typing.Literal["mraverageheader"],
    "padding": typing.NotRequired[float | None],
    "resolution": typing.NotRequired[str | None],
    "fill": bool,
    "datatype": typing.NotRequired[str | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[MraverageheaderConfigParameters] | None],
    "help": bool,
    "version": bool,
    "input": list[InputPathType],
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
        "mraverageheader": mraverageheader_cargs,
        "config": mraverageheader_config_cargs,
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
        "mraverageheader": mraverageheader_outputs,
    }.get(t)


def mraverageheader_config_params(
    key: str,
    value: str,
) -> MraverageheaderConfigParameters:
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


def mraverageheader_config_cargs(
    params: MraverageheaderConfigParameters,
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


class MraverageheaderOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mraverageheader(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output image"""


def mraverageheader_params(
    input_: list[InputPathType],
    output: str,
    padding: float | None = None,
    resolution: str | None = None,
    fill: bool = False,
    datatype: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MraverageheaderConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> MraverageheaderParameters:
    """
    Build parameters.
    
    Args:
        input_: the input image(s).
        output: the output image.
        padding: boundary box padding in voxels. Default: 0.
        resolution: subsampling of template compared to smallest voxel size in\
            any input image. Valid options are 'mean': unbiased but loss of\
            resolution for individual images possible, and 'max': smallest voxel\
            size of any input image defines the resolution. Default: mean.
        fill: set the intensity in the first volume of the average space to 1.
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
        "__STYXTYPE__": "mraverageheader",
        "fill": fill,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "input": input_,
        "output": output,
    }
    if padding is not None:
        params["padding"] = padding
    if resolution is not None:
        params["resolution"] = resolution
    if datatype is not None:
        params["datatype"] = datatype
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def mraverageheader_cargs(
    params: MraverageheaderParameters,
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
    cargs.append("mraverageheader")
    if params.get("padding") is not None:
        cargs.extend([
            "-padding",
            str(params.get("padding"))
        ])
    if params.get("resolution") is not None:
        cargs.extend([
            "-resolution",
            params.get("resolution")
        ])
    if params.get("fill"):
        cargs.append("-fill")
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
    cargs.append(params.get("output"))
    return cargs


def mraverageheader_outputs(
    params: MraverageheaderParameters,
    execution: Execution,
) -> MraverageheaderOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MraverageheaderOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("output")),
    )
    return ret


def mraverageheader_execute(
    params: MraverageheaderParameters,
    execution: Execution,
) -> MraverageheaderOutputs:
    """
    Calculate the average (unbiased) coordinate space of all input images.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MraverageheaderOutputs`).
    """
    params = execution.params(params)
    cargs = mraverageheader_cargs(params, execution)
    ret = mraverageheader_outputs(params, execution)
    execution.run(cargs)
    return ret


def mraverageheader(
    input_: list[InputPathType],
    output: str,
    padding: float | None = None,
    resolution: str | None = None,
    fill: bool = False,
    datatype: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MraverageheaderConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MraverageheaderOutputs:
    """
    Calculate the average (unbiased) coordinate space of all input images.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        input_: the input image(s).
        output: the output image.
        padding: boundary box padding in voxels. Default: 0.
        resolution: subsampling of template compared to smallest voxel size in\
            any input image. Valid options are 'mean': unbiased but loss of\
            resolution for individual images possible, and 'max': smallest voxel\
            size of any input image defines the resolution. Default: mean.
        fill: set the intensity in the first volume of the average space to 1.
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
        NamedTuple of outputs (described in `MraverageheaderOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRAVERAGEHEADER_METADATA)
    params = mraverageheader_params(
        padding=padding,
        resolution=resolution,
        fill=fill,
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
        output=output,
    )
    return mraverageheader_execute(params, execution)


__all__ = [
    "MRAVERAGEHEADER_METADATA",
    "MraverageheaderConfigParameters",
    "MraverageheaderOutputs",
    "MraverageheaderParameters",
    "mraverageheader",
    "mraverageheader_config_params",
    "mraverageheader_params",
]
