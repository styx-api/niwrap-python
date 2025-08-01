# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

WHIRLGIF_METADATA = Metadata(
    id="a9057496ef5501a1d303c580fec62c7576b5c90a.boutiques",
    name="whirlgif",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


WhirlgifParameters = typing.TypedDict('WhirlgifParameters', {
    "__STYXTYPE__": typing.Literal["whirlgif"],
    "outfile": typing.NotRequired[InputPathType | None],
    "loop_count": typing.NotRequired[int | None],
    "delay_time": typing.NotRequired[int | None],
    "disp_flag": typing.NotRequired[typing.Literal["none", "back", "prev", "not"] | None],
    "list_file": typing.NotRequired[InputPathType | None],
    "input_files": list[InputPathType],
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
        "whirlgif": whirlgif_cargs,
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
        "whirlgif": whirlgif_outputs,
    }.get(t)


class WhirlgifOutputs(typing.NamedTuple):
    """
    Output object returned when calling `whirlgif(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """The generated GIF animation"""


def whirlgif_params(
    input_files: list[InputPathType],
    outfile: InputPathType | None = None,
    loop_count: int | None = None,
    delay_time: int | None = None,
    disp_flag: typing.Literal["none", "back", "prev", "not"] | None = None,
    list_file: InputPathType | None = None,
) -> WhirlgifParameters:
    """
    Build parameters.
    
    Args:
        input_files: Input image files for the animation.
        outfile: Specify the output file.
        loop_count: Specify the loop count for the animation.
        delay_time: Specify the delay time between frames.
        disp_flag: Specify the disposal method for frames.
        list_file: Input list file containing names of images to be used for\
            animation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "whirlgif",
        "input_files": input_files,
    }
    if outfile is not None:
        params["outfile"] = outfile
    if loop_count is not None:
        params["loop_count"] = loop_count
    if delay_time is not None:
        params["delay_time"] = delay_time
    if disp_flag is not None:
        params["disp_flag"] = disp_flag
    if list_file is not None:
        params["list_file"] = list_file
    return params


def whirlgif_cargs(
    params: WhirlgifParameters,
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
    cargs.append("whirlgif")
    if params.get("outfile") is not None:
        cargs.extend([
            "-o",
            execution.input_file(params.get("outfile"))
        ])
    if params.get("loop_count") is not None:
        cargs.extend([
            "-loop",
            str(params.get("loop_count"))
        ])
    if params.get("delay_time") is not None:
        cargs.extend([
            "-time",
            str(params.get("delay_time"))
        ])
    if params.get("disp_flag") is not None:
        cargs.extend([
            "-disp",
            params.get("disp_flag")
        ])
    if params.get("list_file") is not None:
        cargs.extend([
            "-i",
            execution.input_file(params.get("list_file"))
        ])
    cargs.extend([execution.input_file(f) for f in params.get("input_files")])
    return cargs


def whirlgif_outputs(
    params: WhirlgifParameters,
    execution: Execution,
) -> WhirlgifOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = WhirlgifOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(pathlib.Path(params.get("outfile")).name) if (params.get("outfile") is not None) else None,
    )
    return ret


def whirlgif_execute(
    params: WhirlgifParameters,
    execution: Execution,
) -> WhirlgifOutputs:
    """
    GIF animation tool.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `WhirlgifOutputs`).
    """
    params = execution.params(params)
    cargs = whirlgif_cargs(params, execution)
    ret = whirlgif_outputs(params, execution)
    execution.run(cargs)
    return ret


def whirlgif(
    input_files: list[InputPathType],
    outfile: InputPathType | None = None,
    loop_count: int | None = None,
    delay_time: int | None = None,
    disp_flag: typing.Literal["none", "back", "prev", "not"] | None = None,
    list_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> WhirlgifOutputs:
    """
    GIF animation tool.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_files: Input image files for the animation.
        outfile: Specify the output file.
        loop_count: Specify the loop count for the animation.
        delay_time: Specify the delay time between frames.
        disp_flag: Specify the disposal method for frames.
        list_file: Input list file containing names of images to be used for\
            animation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `WhirlgifOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(WHIRLGIF_METADATA)
    params = whirlgif_params(
        outfile=outfile,
        loop_count=loop_count,
        delay_time=delay_time,
        disp_flag=disp_flag,
        list_file=list_file,
        input_files=input_files,
    )
    return whirlgif_execute(params, execution)


__all__ = [
    "WHIRLGIF_METADATA",
    "WhirlgifOutputs",
    "WhirlgifParameters",
    "whirlgif",
    "whirlgif_params",
]
