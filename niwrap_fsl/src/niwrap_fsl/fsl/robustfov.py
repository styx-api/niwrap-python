# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ROBUSTFOV_METADATA = Metadata(
    id="3a5071d68b35032e4f3bb975acdeaa9bc87a8c91.boutiques",
    name="robustfov",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


RobustfovParameters = typing.TypedDict('RobustfovParameters', {
    "__STYXTYPE__": typing.Literal["robustfov"],
    "input_file": InputPathType,
    "output_image": typing.NotRequired[str | None],
    "brain_size": typing.NotRequired[float | None],
    "matrix_output": typing.NotRequired[str | None],
    "debug_flag": bool,
    "verbose_flag": bool,
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
        "robustfov": robustfov_cargs,
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
        "robustfov": robustfov_outputs,
    }.get(t)


class RobustfovOutputs(typing.NamedTuple):
    """
    Output object returned when calling `robustfov(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_roi_volume: OutputPathType | None
    """ROI volume output"""
    output_matrix_file: OutputPathType | None
    """Matrix output (ROI to full FOV)"""


def robustfov_params(
    input_file: InputPathType,
    output_image: str | None = "output",
    brain_size: float | None = None,
    matrix_output: str | None = None,
    debug_flag: bool = False,
    verbose_flag: bool = False,
) -> RobustfovParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input image file.
        output_image: ROI volume output name.
        brain_size: Size of the brain in z-dimension (default 170mm).
        matrix_output: Matrix output name (ROI to full FOV).
        debug_flag: Turn on debugging output.
        verbose_flag: Switch on diagnostic messages.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "robustfov",
        "input_file": input_file,
        "debug_flag": debug_flag,
        "verbose_flag": verbose_flag,
    }
    if output_image is not None:
        params["output_image"] = output_image
    if brain_size is not None:
        params["brain_size"] = brain_size
    if matrix_output is not None:
        params["matrix_output"] = matrix_output
    return params


def robustfov_cargs(
    params: RobustfovParameters,
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
    cargs.append("robustfov")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_file"))
    ])
    if params.get("output_image") is not None:
        cargs.extend([
            "-r",
            params.get("output_image")
        ])
    if params.get("brain_size") is not None:
        cargs.extend([
            "-b",
            str(params.get("brain_size"))
        ])
    if params.get("matrix_output") is not None:
        cargs.extend([
            "-m",
            params.get("matrix_output")
        ])
    if params.get("debug_flag"):
        cargs.append("--debug")
    if params.get("verbose_flag"):
        cargs.append("--verbose")
    return cargs


def robustfov_outputs(
    params: RobustfovParameters,
    execution: Execution,
) -> RobustfovOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RobustfovOutputs(
        root=execution.output_file("."),
        output_roi_volume=execution.output_file(params.get("output_image").removesuffix(".nii.gz") + ".nii.gz") if (params.get("output_image") is not None) else None,
        output_matrix_file=execution.output_file(params.get("matrix_output") + ".txt") if (params.get("matrix_output") is not None) else None,
    )
    return ret


def robustfov_execute(
    params: RobustfovParameters,
    execution: Execution,
) -> RobustfovOutputs:
    """
    Reduce FOV of image to remove lower head and neck.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RobustfovOutputs`).
    """
    params = execution.params(params)
    cargs = robustfov_cargs(params, execution)
    ret = robustfov_outputs(params, execution)
    execution.run(cargs)
    return ret


def robustfov(
    input_file: InputPathType,
    output_image: str | None = "output",
    brain_size: float | None = None,
    matrix_output: str | None = None,
    debug_flag: bool = False,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> RobustfovOutputs:
    """
    Reduce FOV of image to remove lower head and neck.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: Input image file.
        output_image: ROI volume output name.
        brain_size: Size of the brain in z-dimension (default 170mm).
        matrix_output: Matrix output name (ROI to full FOV).
        debug_flag: Turn on debugging output.
        verbose_flag: Switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RobustfovOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ROBUSTFOV_METADATA)
    params = robustfov_params(
        input_file=input_file,
        output_image=output_image,
        brain_size=brain_size,
        matrix_output=matrix_output,
        debug_flag=debug_flag,
        verbose_flag=verbose_flag,
    )
    return robustfov_execute(params, execution)


__all__ = [
    "ROBUSTFOV_METADATA",
    "RobustfovOutputs",
    "RobustfovParameters",
    "robustfov",
    "robustfov_params",
]
