# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SLICES_SUMMARY_METADATA = Metadata(
    id="7e12274a48ff3a22f816a66d47a48b98cc85883c.boutiques",
    name="slices_summary",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


SlicesSummaryParameters = typing.TypedDict('SlicesSummaryParameters', {
    "__STYX_TYPE__": typing.Literal["slices_summary"],
    "4d_input_file": InputPathType,
    "threshold": float,
    "background_image": InputPathType,
    "pictures_sum": str,
    "single_slice_flag": bool,
    "darker_background_flag": bool,
    "dumb_rule_flag": bool,
    "pictures_sum_second": str,
    "output_png": str,
    "timepoints": str,
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
        "slices_summary": slices_summary_cargs,
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
        "slices_summary": slices_summary_outputs,
    }.get(t)


class SlicesSummaryOutputs(typing.NamedTuple):
    """
    Output object returned when calling `slices_summary(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    summary_images_directory: OutputPathType
    """Directory containing summary images"""
    combined_summary_image: OutputPathType
    """Combined summary PNG image"""


def slices_summary_params(
    v_4d_input_file: InputPathType,
    threshold: float,
    background_image: InputPathType,
    pictures_sum: str,
    pictures_sum_second: str,
    output_png: str,
    timepoints: str,
    single_slice_flag: bool = False,
    darker_background_flag: bool = False,
    dumb_rule_flag: bool = False,
) -> SlicesSummaryParameters:
    """
    Build parameters.
    
    Args:
        v_4d_input_file: 4D input image (e.g., melodic_IC).
        threshold: Threshold value for the slices.
        background_image: Background image file (e.g., standard/MNI152_T1_2mm).
        pictures_sum: Output directory for summary images.
        pictures_sum_second: Path to summary images directory.
        output_png: Output PNG file.
        timepoints: Space-separated list of timepoints to use; first timepoint\
            is 0.
        single_slice_flag: Generate single-slice summary images instead of\
            3-slice.
        darker_background_flag: Make background darker and colour brighter, for\
            greater colour visibility.
        dumb_rule_flag: Use dumber rule for choosing optimal slice.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "slices_summary",
        "4d_input_file": v_4d_input_file,
        "threshold": threshold,
        "background_image": background_image,
        "pictures_sum": pictures_sum,
        "single_slice_flag": single_slice_flag,
        "darker_background_flag": darker_background_flag,
        "dumb_rule_flag": dumb_rule_flag,
        "pictures_sum_second": pictures_sum_second,
        "output_png": output_png,
        "timepoints": timepoints,
    }
    return params


def slices_summary_cargs(
    params: SlicesSummaryParameters,
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
    cargs.append("slices_summary")
    cargs.append(execution.input_file(params.get("4d_input_file")))
    cargs.append(str(params.get("threshold")))
    cargs.append(execution.input_file(params.get("background_image")))
    cargs.append(params.get("pictures_sum"))
    if params.get("single_slice_flag"):
        cargs.append("-1")
    if params.get("darker_background_flag"):
        cargs.append("-d")
    if params.get("dumb_rule_flag"):
        cargs.append("-c")
    cargs.append(params.get("pictures_sum_second"))
    cargs.append(params.get("output_png"))
    cargs.append(params.get("timepoints"))
    return cargs


def slices_summary_outputs(
    params: SlicesSummaryParameters,
    execution: Execution,
) -> SlicesSummaryOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SlicesSummaryOutputs(
        root=execution.output_file("."),
        summary_images_directory=execution.output_file(params.get("pictures_sum_second")),
        combined_summary_image=execution.output_file(params.get("output_png")),
    )
    return ret


def slices_summary_execute(
    params: SlicesSummaryParameters,
    execution: Execution,
) -> SlicesSummaryOutputs:
    """
    Generate summary PNG images for 4D neuroimaging data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SlicesSummaryOutputs`).
    """
    params = execution.params(params)
    cargs = slices_summary_cargs(params, execution)
    ret = slices_summary_outputs(params, execution)
    execution.run(cargs)
    return ret


def slices_summary(
    v_4d_input_file: InputPathType,
    threshold: float,
    background_image: InputPathType,
    pictures_sum: str,
    pictures_sum_second: str,
    output_png: str,
    timepoints: str,
    single_slice_flag: bool = False,
    darker_background_flag: bool = False,
    dumb_rule_flag: bool = False,
    runner: Runner | None = None,
) -> SlicesSummaryOutputs:
    """
    Generate summary PNG images for 4D neuroimaging data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        v_4d_input_file: 4D input image (e.g., melodic_IC).
        threshold: Threshold value for the slices.
        background_image: Background image file (e.g., standard/MNI152_T1_2mm).
        pictures_sum: Output directory for summary images.
        pictures_sum_second: Path to summary images directory.
        output_png: Output PNG file.
        timepoints: Space-separated list of timepoints to use; first timepoint\
            is 0.
        single_slice_flag: Generate single-slice summary images instead of\
            3-slice.
        darker_background_flag: Make background darker and colour brighter, for\
            greater colour visibility.
        dumb_rule_flag: Use dumber rule for choosing optimal slice.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SlicesSummaryOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SLICES_SUMMARY_METADATA)
    params = slices_summary_params(
        v_4d_input_file=v_4d_input_file,
        threshold=threshold,
        background_image=background_image,
        pictures_sum=pictures_sum,
        single_slice_flag=single_slice_flag,
        darker_background_flag=darker_background_flag,
        dumb_rule_flag=dumb_rule_flag,
        pictures_sum_second=pictures_sum_second,
        output_png=output_png,
        timepoints=timepoints,
    )
    return slices_summary_execute(params, execution)


__all__ = [
    "SLICES_SUMMARY_METADATA",
    "SlicesSummaryOutputs",
    "SlicesSummaryParameters",
    "slices_summary",
    "slices_summary_params",
]
