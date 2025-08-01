# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MATCH_SMOOTHING_METADATA = Metadata(
    id="b30339df7f06b79582f3ec4f343b57bac26ab4fb.boutiques",
    name="match_smoothing",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


MatchSmoothingParameters = typing.TypedDict('MatchSmoothingParameters', {
    "__STYXTYPE__": typing.Literal["match_smoothing"],
    "example_func": InputPathType,
    "func_smoothing_FWHM": float,
    "example_structural": InputPathType,
    "standard_space_resolution": float,
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
        "match_smoothing": match_smoothing_cargs,
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


class MatchSmoothingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `match_smoothing(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def match_smoothing_params(
    example_func: InputPathType,
    func_smoothing_fwhm: float,
    example_structural: InputPathType,
    standard_space_resolution: float,
) -> MatchSmoothingParameters:
    """
    Build parameters.
    
    Args:
        example_func: Path to the example functional image file.
        func_smoothing_fwhm: Full-width at half maximum (FWHM) of the smoothing\
            kernel applied to the functional data, in millimeters.
        example_structural: Path to the example structural image file.
        standard_space_resolution: Resolution of the standard space, in\
            millimeters.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "match_smoothing",
        "example_func": example_func,
        "func_smoothing_FWHM": func_smoothing_fwhm,
        "example_structural": example_structural,
        "standard_space_resolution": standard_space_resolution,
    }
    return params


def match_smoothing_cargs(
    params: MatchSmoothingParameters,
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
    cargs.append("match_smoothing")
    cargs.append(execution.input_file(params.get("example_func")))
    cargs.append(str(params.get("func_smoothing_FWHM")))
    cargs.append(execution.input_file(params.get("example_structural")))
    cargs.append(str(params.get("standard_space_resolution")))
    return cargs


def match_smoothing_outputs(
    params: MatchSmoothingParameters,
    execution: Execution,
) -> MatchSmoothingOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MatchSmoothingOutputs(
        root=execution.output_file("."),
    )
    return ret


def match_smoothing_execute(
    params: MatchSmoothingParameters,
    execution: Execution,
) -> MatchSmoothingOutputs:
    """
    Computes the smoothing sigma needed to be applied to structural data to match a
    given functional data smoothing level.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MatchSmoothingOutputs`).
    """
    params = execution.params(params)
    cargs = match_smoothing_cargs(params, execution)
    ret = match_smoothing_outputs(params, execution)
    execution.run(cargs)
    return ret


def match_smoothing(
    example_func: InputPathType,
    func_smoothing_fwhm: float,
    example_structural: InputPathType,
    standard_space_resolution: float,
    runner: Runner | None = None,
) -> MatchSmoothingOutputs:
    """
    Computes the smoothing sigma needed to be applied to structural data to match a
    given functional data smoothing level.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        example_func: Path to the example functional image file.
        func_smoothing_fwhm: Full-width at half maximum (FWHM) of the smoothing\
            kernel applied to the functional data, in millimeters.
        example_structural: Path to the example structural image file.
        standard_space_resolution: Resolution of the standard space, in\
            millimeters.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MatchSmoothingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MATCH_SMOOTHING_METADATA)
    params = match_smoothing_params(
        example_func=example_func,
        func_smoothing_fwhm=func_smoothing_fwhm,
        example_structural=example_structural,
        standard_space_resolution=standard_space_resolution,
    )
    return match_smoothing_execute(params, execution)


__all__ = [
    "MATCH_SMOOTHING_METADATA",
    "MatchSmoothingOutputs",
    "MatchSmoothingParameters",
    "match_smoothing",
    "match_smoothing_params",
]
