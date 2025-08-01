# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

HIST2PROB_METADATA = Metadata(
    id="9a0694f1331e41c1803a820e366b78bb807361a8.boutiques",
    name="hist2prob",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


Hist2probParameters = typing.TypedDict('Hist2probParameters', {
    "__STYXTYPE__": typing.Literal["hist2prob"],
    "image": InputPathType,
    "size": int,
    "low_threshold": float,
    "high_threshold": float,
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
        "hist2prob": hist2prob_cargs,
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
        "hist2prob": hist2prob_outputs,
    }.get(t)


class Hist2probOutputs(typing.NamedTuple):
    """
    Output object returned when calling `hist2prob(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_probability_map: OutputPathType
    """Output probability map converted from histogram"""


def hist2prob_params(
    image: InputPathType,
    size: int,
    low_threshold: float,
    high_threshold: float,
) -> Hist2probParameters:
    """
    Build parameters.
    
    Args:
        image: Input histogram image.
        size: Size of the histogram.
        low_threshold: Lower threshold for probability conversion.
        high_threshold: Higher threshold for probability conversion.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "hist2prob",
        "image": image,
        "size": size,
        "low_threshold": low_threshold,
        "high_threshold": high_threshold,
    }
    return params


def hist2prob_cargs(
    params: Hist2probParameters,
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
    cargs.append("hist2prob")
    cargs.append(execution.input_file(params.get("image")))
    cargs.append(str(params.get("size")))
    cargs.append(str(params.get("low_threshold")))
    cargs.append(str(params.get("high_threshold")))
    return cargs


def hist2prob_outputs(
    params: Hist2probParameters,
    execution: Execution,
) -> Hist2probOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Hist2probOutputs(
        root=execution.output_file("."),
        output_probability_map=execution.output_file(pathlib.Path(params.get("image")).name + "_probability_map.nii.gz"),
    )
    return ret


def hist2prob_execute(
    params: Hist2probParameters,
    execution: Execution,
) -> Hist2probOutputs:
    """
    Converts a histogram image to a probability map based on specified thresholds.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Hist2probOutputs`).
    """
    params = execution.params(params)
    cargs = hist2prob_cargs(params, execution)
    ret = hist2prob_outputs(params, execution)
    execution.run(cargs)
    return ret


def hist2prob(
    image: InputPathType,
    size: int,
    low_threshold: float,
    high_threshold: float,
    runner: Runner | None = None,
) -> Hist2probOutputs:
    """
    Converts a histogram image to a probability map based on specified thresholds.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        image: Input histogram image.
        size: Size of the histogram.
        low_threshold: Lower threshold for probability conversion.
        high_threshold: Higher threshold for probability conversion.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Hist2probOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(HIST2PROB_METADATA)
    params = hist2prob_params(
        image=image,
        size=size,
        low_threshold=low_threshold,
        high_threshold=high_threshold,
    )
    return hist2prob_execute(params, execution)


__all__ = [
    "HIST2PROB_METADATA",
    "Hist2probOutputs",
    "Hist2probParameters",
    "hist2prob",
    "hist2prob_params",
]
