# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RUN_FIRST_ALL_METADATA = Metadata(
    id="969df88743cb206b767170e9a9d7af5b9fccc839.boutiques",
    name="run_first_all",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


RunFirstAllParameters = typing.TypedDict('RunFirstAllParameters', {
    "__STYX_TYPE__": typing.Literal["run_first_all"],
    "method": typing.NotRequired[typing.Literal["auto", "fast", "none"] | None],
    "brainextract_flag": bool,
    "structure": typing.NotRequired[str | None],
    "affine_matrix": typing.NotRequired[InputPathType | None],
    "threestage_flag": bool,
    "debug_flag": bool,
    "verbose_flag": bool,
    "input_image": InputPathType,
    "output_image": str,
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
        "run_first_all": run_first_all_cargs,
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
        "run_first_all": run_first_all_outputs,
    }.get(t)


class RunFirstAllOutputs(typing.NamedTuple):
    """
    Output object returned when calling `run_first_all(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_file: OutputPathType
    """Output image file"""


def run_first_all_params(
    input_image: InputPathType,
    output_image: str,
    method: typing.Literal["auto", "fast", "none"] | None = None,
    brainextract_flag: bool = False,
    structure: str | None = None,
    affine_matrix: InputPathType | None = None,
    threestage_flag: bool = False,
    debug_flag: bool = False,
    verbose_flag: bool = False,
) -> RunFirstAllParameters:
    """
    Build parameters.
    
    Args:
        input_image: Input image file.
        output_image: Output image file.
        method: Method for brain extraction (auto, fast, none or a numerical\
            threshold value).
        brainextract_flag: Input is already brain extracted.
        structure: Run only on one specified structure (e.g. L_Hipp) or a comma\
            separated list (no spaces).
        affine_matrix: Use affine matrix (do not re-run registration).
        threestage_flag: Use 3-stage affine registration (only currently for\
            hippocampus).
        debug_flag: Do not cleanup image output files (useful for debugging).
        verbose_flag: Verbose output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "run_first_all",
        "brainextract_flag": brainextract_flag,
        "threestage_flag": threestage_flag,
        "debug_flag": debug_flag,
        "verbose_flag": verbose_flag,
        "input_image": input_image,
        "output_image": output_image,
    }
    if method is not None:
        params["method"] = method
    if structure is not None:
        params["structure"] = structure
    if affine_matrix is not None:
        params["affine_matrix"] = affine_matrix
    return params


def run_first_all_cargs(
    params: RunFirstAllParameters,
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
    cargs.append("run_first_all")
    if params.get("method") is not None:
        cargs.extend([
            "-m",
            params.get("method")
        ])
    if params.get("brainextract_flag"):
        cargs.append("-b")
    if params.get("structure") is not None:
        cargs.extend([
            "-s",
            params.get("structure")
        ])
    if params.get("affine_matrix") is not None:
        cargs.extend([
            "-a",
            execution.input_file(params.get("affine_matrix"))
        ])
    if params.get("threestage_flag"):
        cargs.append("-3")
    if params.get("debug_flag"):
        cargs.append("-d")
    if params.get("verbose_flag"):
        cargs.append("-v")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_image"))
    ])
    cargs.extend([
        "-o",
        params.get("output_image")
    ])
    return cargs


def run_first_all_outputs(
    params: RunFirstAllParameters,
    execution: Execution,
) -> RunFirstAllOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RunFirstAllOutputs(
        root=execution.output_file("."),
        output_image_file=execution.output_file(params.get("output_image")),
    )
    return ret


def run_first_all_execute(
    params: RunFirstAllParameters,
    execution: Execution,
) -> RunFirstAllOutputs:
    """
    FIRST - FMRIB's Integrated Registration and Segmentation Tool for subcortical
    brain structures.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RunFirstAllOutputs`).
    """
    params = execution.params(params)
    cargs = run_first_all_cargs(params, execution)
    ret = run_first_all_outputs(params, execution)
    execution.run(cargs)
    return ret


def run_first_all(
    input_image: InputPathType,
    output_image: str,
    method: typing.Literal["auto", "fast", "none"] | None = None,
    brainextract_flag: bool = False,
    structure: str | None = None,
    affine_matrix: InputPathType | None = None,
    threestage_flag: bool = False,
    debug_flag: bool = False,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> RunFirstAllOutputs:
    """
    FIRST - FMRIB's Integrated Registration and Segmentation Tool for subcortical
    brain structures.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_image: Input image file.
        output_image: Output image file.
        method: Method for brain extraction (auto, fast, none or a numerical\
            threshold value).
        brainextract_flag: Input is already brain extracted.
        structure: Run only on one specified structure (e.g. L_Hipp) or a comma\
            separated list (no spaces).
        affine_matrix: Use affine matrix (do not re-run registration).
        threestage_flag: Use 3-stage affine registration (only currently for\
            hippocampus).
        debug_flag: Do not cleanup image output files (useful for debugging).
        verbose_flag: Verbose output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RunFirstAllOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RUN_FIRST_ALL_METADATA)
    params = run_first_all_params(
        method=method,
        brainextract_flag=brainextract_flag,
        structure=structure,
        affine_matrix=affine_matrix,
        threestage_flag=threestage_flag,
        debug_flag=debug_flag,
        verbose_flag=verbose_flag,
        input_image=input_image,
        output_image=output_image,
    )
    return run_first_all_execute(params, execution)


__all__ = [
    "RUN_FIRST_ALL_METADATA",
    "RunFirstAllOutputs",
    "RunFirstAllParameters",
    "run_first_all",
    "run_first_all_params",
]
