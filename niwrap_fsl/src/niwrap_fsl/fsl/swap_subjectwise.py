# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SWAP_SUBJECTWISE_METADATA = Metadata(
    id="281cd4302b7a84b291d077861717f5646ab39a05.boutiques",
    name="swap_subjectwise",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


SwapSubjectwiseParameters = typing.TypedDict('SwapSubjectwiseParameters', {
    "__STYXTYPE__": typing.Literal["swap_subjectwise"],
    "dyads": InputPathType,
    "fmean": InputPathType,
    "mask": typing.NotRequired[InputPathType | None],
    "obasename": typing.NotRequired[str | None],
    "xthresh": typing.NotRequired[float | None],
    "averageonly_flag": bool,
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
        "swap_subjectwise": swap_subjectwise_cargs,
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


class SwapSubjectwiseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `swap_subjectwise(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def swap_subjectwise_params(
    dyads: InputPathType,
    fmean: InputPathType,
    mask: InputPathType | None = None,
    obasename: str | None = None,
    xthresh: float | None = None,
    averageonly_flag: bool = False,
    verbose_flag: bool = False,
) -> SwapSubjectwiseParameters:
    """
    Build parameters.
    
    Args:
        dyads: List of list of dyads.
        fmean: List of list of mean fsamples.
        mask: Filename of brain mask.
        obasename: Output obasename [default=swapped].
        xthresh: A.R.D. threshold - default=0.1.
        averageonly_flag: Average only?.
        verbose_flag: Switch on diagnostic messages.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "swap_subjectwise",
        "dyads": dyads,
        "fmean": fmean,
        "averageonly_flag": averageonly_flag,
        "verbose_flag": verbose_flag,
    }
    if mask is not None:
        params["mask"] = mask
    if obasename is not None:
        params["obasename"] = obasename
    if xthresh is not None:
        params["xthresh"] = xthresh
    return params


def swap_subjectwise_cargs(
    params: SwapSubjectwiseParameters,
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
    cargs.append("swap_subjectwise")
    cargs.extend([
        "-r",
        execution.input_file(params.get("dyads"))
    ])
    cargs.extend([
        "-f",
        execution.input_file(params.get("fmean"))
    ])
    if params.get("mask") is not None:
        cargs.extend([
            "-m",
            execution.input_file(params.get("mask"))
        ])
    if params.get("obasename") is not None:
        cargs.extend([
            "-b",
            params.get("obasename")
        ])
    if params.get("xthresh") is not None:
        cargs.extend([
            "--xthresh",
            str(params.get("xthresh"))
        ])
    if params.get("averageonly_flag"):
        cargs.append("--averageonly")
    if params.get("verbose_flag"):
        cargs.append("--verbose")
    return cargs


def swap_subjectwise_outputs(
    params: SwapSubjectwiseParameters,
    execution: Execution,
) -> SwapSubjectwiseOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SwapSubjectwiseOutputs(
        root=execution.output_file("."),
    )
    return ret


def swap_subjectwise_execute(
    params: SwapSubjectwiseParameters,
    execution: Execution,
) -> SwapSubjectwiseOutputs:
    """
    Reordering of the dyadic vectors and fsamples according to average inter-subject
    modal orientations.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SwapSubjectwiseOutputs`).
    """
    params = execution.params(params)
    cargs = swap_subjectwise_cargs(params, execution)
    ret = swap_subjectwise_outputs(params, execution)
    execution.run(cargs)
    return ret


def swap_subjectwise(
    dyads: InputPathType,
    fmean: InputPathType,
    mask: InputPathType | None = None,
    obasename: str | None = None,
    xthresh: float | None = None,
    averageonly_flag: bool = False,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> SwapSubjectwiseOutputs:
    """
    Reordering of the dyadic vectors and fsamples according to average inter-subject
    modal orientations.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        dyads: List of list of dyads.
        fmean: List of list of mean fsamples.
        mask: Filename of brain mask.
        obasename: Output obasename [default=swapped].
        xthresh: A.R.D. threshold - default=0.1.
        averageonly_flag: Average only?.
        verbose_flag: Switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SwapSubjectwiseOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SWAP_SUBJECTWISE_METADATA)
    params = swap_subjectwise_params(
        dyads=dyads,
        fmean=fmean,
        mask=mask,
        obasename=obasename,
        xthresh=xthresh,
        averageonly_flag=averageonly_flag,
        verbose_flag=verbose_flag,
    )
    return swap_subjectwise_execute(params, execution)


__all__ = [
    "SWAP_SUBJECTWISE_METADATA",
    "SwapSubjectwiseOutputs",
    "SwapSubjectwiseParameters",
    "swap_subjectwise",
    "swap_subjectwise_params",
]
