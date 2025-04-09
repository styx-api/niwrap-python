# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SLICETIMER_METADATA = Metadata(
    id="4c58bd416c438fc3d8b3664e317bd8eaaa5287b6.boutiques",
    name="slicetimer",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


SlicetimerParameters = typing.TypedDict('SlicetimerParameters', {
    "__STYX_TYPE__": typing.Literal["slicetimer"],
    "infile": InputPathType,
    "outfile": typing.NotRequired[InputPathType | None],
    "verbose_flag": bool,
    "down_flag": bool,
    "tr_value": typing.NotRequired[float | None],
    "direction": typing.NotRequired[str | None],
    "odd_flag": bool,
    "tcustom_file": typing.NotRequired[InputPathType | None],
    "tglobal_value": typing.NotRequired[float | None],
    "ocustom_file": typing.NotRequired[InputPathType | None],
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
        "slicetimer": slicetimer_cargs,
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
        "slicetimer": slicetimer_outputs,
    }.get(t)


class SlicetimerOutputs(typing.NamedTuple):
    """
    Output object returned when calling `slicetimer(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_timeseries: OutputPathType | None
    """Output timeseries"""


def slicetimer_params(
    infile: InputPathType,
    outfile: InputPathType | None = None,
    verbose_flag: bool = False,
    down_flag: bool = False,
    tr_value: float | None = None,
    direction: str | None = None,
    odd_flag: bool = False,
    tcustom_file: InputPathType | None = None,
    tglobal_value: float | None = None,
    ocustom_file: InputPathType | None = None,
) -> SlicetimerParameters:
    """
    Build parameters.
    
    Args:
        infile: Filename of input timeseries.
        outfile: Filename of output timeseries.
        verbose_flag: Switch on diagnostic messages.
        down_flag: Reverse slice indexing (default is: slices were acquired\
            bottom-up).
        tr_value: Specify TR of data - default is 3s.
        direction: Direction of slice acquisition (x=1,y=2,z=3) - default is z.
        odd_flag: Use interleaved acquisition.
        tcustom_file: Filename of single-column slice timings, in fractions of\
            TR, +ve values shift slices forward in time.
        tglobal_value: Global shift in fraction of TR, (default is 0).
        ocustom_file: Filename of single-column custom interleave order file\
            (first slice is referred to as 1 not 0).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "slicetimer",
        "infile": infile,
        "verbose_flag": verbose_flag,
        "down_flag": down_flag,
        "odd_flag": odd_flag,
    }
    if outfile is not None:
        params["outfile"] = outfile
    if tr_value is not None:
        params["tr_value"] = tr_value
    if direction is not None:
        params["direction"] = direction
    if tcustom_file is not None:
        params["tcustom_file"] = tcustom_file
    if tglobal_value is not None:
        params["tglobal_value"] = tglobal_value
    if ocustom_file is not None:
        params["ocustom_file"] = ocustom_file
    return params


def slicetimer_cargs(
    params: SlicetimerParameters,
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
    cargs.append("slicetimer")
    cargs.extend([
        "-i",
        execution.input_file(params.get("infile"))
    ])
    if params.get("outfile") is not None:
        cargs.extend([
            "-o",
            execution.input_file(params.get("outfile"))
        ])
    if params.get("verbose_flag"):
        cargs.append("-v")
    if params.get("down_flag"):
        cargs.append("--down")
    if params.get("tr_value") is not None:
        cargs.extend([
            "-r",
            str(params.get("tr_value"))
        ])
    if params.get("direction") is not None:
        cargs.extend([
            "-d",
            params.get("direction")
        ])
    if params.get("odd_flag"):
        cargs.append("--odd")
    if params.get("tcustom_file") is not None:
        cargs.extend([
            "--tcustom",
            execution.input_file(params.get("tcustom_file"))
        ])
    if params.get("tglobal_value") is not None:
        cargs.extend([
            "--tglobal",
            str(params.get("tglobal_value"))
        ])
    if params.get("ocustom_file") is not None:
        cargs.extend([
            "--ocustom",
            execution.input_file(params.get("ocustom_file"))
        ])
    return cargs


def slicetimer_outputs(
    params: SlicetimerParameters,
    execution: Execution,
) -> SlicetimerOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SlicetimerOutputs(
        root=execution.output_file("."),
        output_timeseries=execution.output_file(pathlib.Path(params.get("outfile")).name) if (params.get("outfile") is not None) else None,
    )
    return ret


def slicetimer_execute(
    params: SlicetimerParameters,
    execution: Execution,
) -> SlicetimerOutputs:
    """
    FMRIB's Interpolation for Slice Timing.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SlicetimerOutputs`).
    """
    params = execution.params(params)
    cargs = slicetimer_cargs(params, execution)
    ret = slicetimer_outputs(params, execution)
    execution.run(cargs)
    return ret


def slicetimer(
    infile: InputPathType,
    outfile: InputPathType | None = None,
    verbose_flag: bool = False,
    down_flag: bool = False,
    tr_value: float | None = None,
    direction: str | None = None,
    odd_flag: bool = False,
    tcustom_file: InputPathType | None = None,
    tglobal_value: float | None = None,
    ocustom_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> SlicetimerOutputs:
    """
    FMRIB's Interpolation for Slice Timing.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        infile: Filename of input timeseries.
        outfile: Filename of output timeseries.
        verbose_flag: Switch on diagnostic messages.
        down_flag: Reverse slice indexing (default is: slices were acquired\
            bottom-up).
        tr_value: Specify TR of data - default is 3s.
        direction: Direction of slice acquisition (x=1,y=2,z=3) - default is z.
        odd_flag: Use interleaved acquisition.
        tcustom_file: Filename of single-column slice timings, in fractions of\
            TR, +ve values shift slices forward in time.
        tglobal_value: Global shift in fraction of TR, (default is 0).
        ocustom_file: Filename of single-column custom interleave order file\
            (first slice is referred to as 1 not 0).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SlicetimerOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SLICETIMER_METADATA)
    params = slicetimer_params(
        infile=infile,
        outfile=outfile,
        verbose_flag=verbose_flag,
        down_flag=down_flag,
        tr_value=tr_value,
        direction=direction,
        odd_flag=odd_flag,
        tcustom_file=tcustom_file,
        tglobal_value=tglobal_value,
        ocustom_file=ocustom_file,
    )
    return slicetimer_execute(params, execution)


__all__ = [
    "SLICETIMER_METADATA",
    "SlicetimerOutputs",
    "SlicetimerParameters",
    "slicetimer",
    "slicetimer_params",
]
