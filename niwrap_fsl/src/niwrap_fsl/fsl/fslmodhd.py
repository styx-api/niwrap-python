# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSLMODHD_METADATA = Metadata(
    id="4d79af63e716050570a42ab303ea6efb6b7d6d71.boutiques",
    name="fslmodhd",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


FslmodhdParameters = typing.TypedDict('FslmodhdParameters', {
    "__STYXTYPE__": typing.Literal["fslmodhd"],
    "image": InputPathType,
    "keyword": str,
    "value": str,
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
        "fslmodhd": fslmodhd_cargs,
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
    }.get(t)


class FslmodhdOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslmodhd(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fslmodhd_params(
    image: InputPathType,
    keyword_: str,
    value: str,
) -> FslmodhdParameters:
    """
    Build parameters.
    
    Args:
        image: Input image file (e.g. image.nii.gz).
        keyword_: Header keyword to modify (e.g. 'dim', 'pixdim').
        value: New value for the given header keyword.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslmodhd",
        "image": image,
        "keyword": keyword_,
        "value": value,
    }
    return params


def fslmodhd_cargs(
    params: FslmodhdParameters,
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
    cargs.append("fslmodhd")
    cargs.append(execution.input_file(params.get("image")))
    cargs.append(params.get("keyword"))
    cargs.append(params.get("value"))
    return cargs


def fslmodhd_outputs(
    params: FslmodhdParameters,
    execution: Execution,
) -> FslmodhdOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslmodhdOutputs(
        root=execution.output_file("."),
    )
    return ret


def fslmodhd_execute(
    params: FslmodhdParameters,
    execution: Execution,
) -> FslmodhdOutputs:
    """
    A tool for modifying header information of NIfTI images.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslmodhdOutputs`).
    """
    params = execution.params(params)
    cargs = fslmodhd_cargs(params, execution)
    ret = fslmodhd_outputs(params, execution)
    execution.run(cargs)
    return ret


def fslmodhd(
    image: InputPathType,
    keyword_: str,
    value: str,
    runner: Runner | None = None,
) -> FslmodhdOutputs:
    """
    A tool for modifying header information of NIfTI images.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        image: Input image file (e.g. image.nii.gz).
        keyword_: Header keyword to modify (e.g. 'dim', 'pixdim').
        value: New value for the given header keyword.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslmodhdOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLMODHD_METADATA)
    params = fslmodhd_params(
        image=image,
        keyword_=keyword_,
        value=value,
    )
    return fslmodhd_execute(params, execution)


__all__ = [
    "FSLMODHD_METADATA",
    "FslmodhdOutputs",
    "FslmodhdParameters",
    "fslmodhd",
    "fslmodhd_params",
]
