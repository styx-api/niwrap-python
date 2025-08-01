# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

IMAVER_METADATA = Metadata(
    id="8d8afa638c5562c34495b2bfecf8b92253a461cf.boutiques",
    name="imaver",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


ImaverParameters = typing.TypedDict('ImaverParameters', {
    "__STYXTYPE__": typing.Literal["imaver"],
    "out_ave": typing.NotRequired[str | None],
    "out_sig": typing.NotRequired[str | None],
    "input_images": list[InputPathType],
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
        "imaver": imaver_cargs,
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
        "imaver": imaver_outputs,
    }.get(t)


class ImaverOutputs(typing.NamedTuple):
    """
    Output object returned when calling `imaver(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_ave_output: OutputPathType | None
    """Output image file for averages (optional)"""
    out_sig_output: OutputPathType | None
    """Output image file for standard deviations (optional)"""


def imaver_params(
    input_images: list[InputPathType],
    out_ave: str | None = None,
    out_sig: str | None = None,
) -> ImaverParameters:
    """
    Build parameters.
    
    Args:
        input_images: Input image files for processing.
        out_ave: Output average image file. Use '-' to skip output.
        out_sig: Output standard deviation image file. Use '-' to skip output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "imaver",
        "input_images": input_images,
    }
    if out_ave is not None:
        params["out_ave"] = out_ave
    if out_sig is not None:
        params["out_sig"] = out_sig
    return params


def imaver_cargs(
    params: ImaverParameters,
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
    cargs.append("imaver")
    if params.get("out_ave") is not None:
        cargs.append(params.get("out_ave"))
    if params.get("out_sig") is not None:
        cargs.append(params.get("out_sig"))
    cargs.extend([execution.input_file(f) for f in params.get("input_images")])
    return cargs


def imaver_outputs(
    params: ImaverParameters,
    execution: Execution,
) -> ImaverOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ImaverOutputs(
        root=execution.output_file("."),
        out_ave_output=execution.output_file(params.get("out_ave")) if (params.get("out_ave") is not None) else None,
        out_sig_output=execution.output_file(params.get("out_sig")) if (params.get("out_sig") is not None) else None,
    )
    return ret


def imaver_execute(
    params: ImaverParameters,
    execution: Execution,
) -> ImaverOutputs:
    """
    Computes the mean and standard deviation, pixel-by-pixel, of a whole bunch of
    images.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ImaverOutputs`).
    """
    params = execution.params(params)
    cargs = imaver_cargs(params, execution)
    ret = imaver_outputs(params, execution)
    execution.run(cargs)
    return ret


def imaver(
    input_images: list[InputPathType],
    out_ave: str | None = None,
    out_sig: str | None = None,
    runner: Runner | None = None,
) -> ImaverOutputs:
    """
    Computes the mean and standard deviation, pixel-by-pixel, of a whole bunch of
    images.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_images: Input image files for processing.
        out_ave: Output average image file. Use '-' to skip output.
        out_sig: Output standard deviation image file. Use '-' to skip output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImaverOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMAVER_METADATA)
    params = imaver_params(
        out_ave=out_ave,
        out_sig=out_sig,
        input_images=input_images,
    )
    return imaver_execute(params, execution)


__all__ = [
    "IMAVER_METADATA",
    "ImaverOutputs",
    "ImaverParameters",
    "imaver",
    "imaver_params",
]
