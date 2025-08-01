# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

WPNG_METADATA = Metadata(
    id="9f9c70ecbedffb509e726c31bb9501a9ecba01a1.boutiques",
    name="wpng",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


WpngParameters = typing.TypedDict('WpngParameters', {
    "__STYXTYPE__": typing.Literal["wpng"],
    "input_file": typing.NotRequired[InputPathType | None],
    "gamma": typing.NotRequired[float | None],
    "bgcolor": typing.NotRequired[str | None],
    "text_flag": bool,
    "time_flag": bool,
    "interlace_flag": bool,
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
        "wpng": wpng_cargs,
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
        "wpng": wpng_outputs,
    }.get(t)


class WpngOutputs(typing.NamedTuple):
    """
    Output object returned when calling `wpng(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Converted PNG file"""


def wpng_params(
    input_file: InputPathType | None = None,
    gamma: float | None = None,
    bgcolor: str | None = None,
    text_flag: bool = False,
    time_flag: bool = False,
    interlace_flag: bool = False,
) -> WpngParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input PNM file (binary PGM 'P5', PPM 'P6' or PAM 'P8').
        gamma: Transfer-function exponent (``gamma'') of the image in\
            floating-point format (e.g., ``0.45455''). If image looks correct on\
            given display system, image gamma is equal to inverse of display-system\
            exponent, i.e., 1 / (LUT * CRT) (where LUT = lookup-table exponent and\
            CRT = CRT exponent; first varies, second is usually 2.2, all are\
            positive).
        bgcolor: Desired background color for alpha-channel images, in\
            7-character hex RGB format (e.g., ``#ff7700'' for orange: same as HTML\
            colors).
        text_flag: Prompt interactively for text info (tEXt chunks).
        time_flag: Include a tIME chunk (last modification time).
        interlace_flag: Write interlaced PNG image.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "wpng",
        "text_flag": text_flag,
        "time_flag": time_flag,
        "interlace_flag": interlace_flag,
    }
    if input_file is not None:
        params["input_file"] = input_file
    if gamma is not None:
        params["gamma"] = gamma
    if bgcolor is not None:
        params["bgcolor"] = bgcolor
    return params


def wpng_cargs(
    params: WpngParameters,
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
    cargs.append("wpng")
    if params.get("input_file") is not None:
        cargs.append(execution.input_file(params.get("input_file")))
    if params.get("gamma") is not None:
        cargs.extend([
            "-gamma",
            str(params.get("gamma"))
        ])
    if params.get("bgcolor") is not None:
        cargs.extend([
            "-bgcolor",
            params.get("bgcolor")
        ])
    if params.get("text_flag"):
        cargs.append("-text")
    if params.get("time_flag"):
        cargs.append("-time")
    if params.get("interlace_flag"):
        cargs.append("-interlace")
    return cargs


def wpng_outputs(
    params: WpngParameters,
    execution: Execution,
) -> WpngOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = WpngOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("[INPUT_FILE_BASE_NAME].png"),
    )
    return ret


def wpng_execute(
    params: WpngParameters,
    execution: Execution,
) -> WpngOutputs:
    """
    Simple PGM/PPM/PAM to PNG Converter.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `WpngOutputs`).
    """
    params = execution.params(params)
    cargs = wpng_cargs(params, execution)
    ret = wpng_outputs(params, execution)
    execution.run(cargs)
    return ret


def wpng(
    input_file: InputPathType | None = None,
    gamma: float | None = None,
    bgcolor: str | None = None,
    text_flag: bool = False,
    time_flag: bool = False,
    interlace_flag: bool = False,
    runner: Runner | None = None,
) -> WpngOutputs:
    """
    Simple PGM/PPM/PAM to PNG Converter.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: Input PNM file (binary PGM 'P5', PPM 'P6' or PAM 'P8').
        gamma: Transfer-function exponent (``gamma'') of the image in\
            floating-point format (e.g., ``0.45455''). If image looks correct on\
            given display system, image gamma is equal to inverse of display-system\
            exponent, i.e., 1 / (LUT * CRT) (where LUT = lookup-table exponent and\
            CRT = CRT exponent; first varies, second is usually 2.2, all are\
            positive).
        bgcolor: Desired background color for alpha-channel images, in\
            7-character hex RGB format (e.g., ``#ff7700'' for orange: same as HTML\
            colors).
        text_flag: Prompt interactively for text info (tEXt chunks).
        time_flag: Include a tIME chunk (last modification time).
        interlace_flag: Write interlaced PNG image.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `WpngOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(WPNG_METADATA)
    params = wpng_params(
        input_file=input_file,
        gamma=gamma,
        bgcolor=bgcolor,
        text_flag=text_flag,
        time_flag=time_flag,
        interlace_flag=interlace_flag,
    )
    return wpng_execute(params, execution)


__all__ = [
    "WPNG_METADATA",
    "WpngOutputs",
    "WpngParameters",
    "wpng",
    "wpng_params",
]
