# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FDR_METADATA = Metadata(
    id="38262a2e430aeb6077cd46188c492f9fa6205b5d.boutiques",
    name="fdr",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


FdrParameters = typing.TypedDict('FdrParameters', {
    "__STYXTYPE__": typing.Literal["fdr"],
    "infile": InputPathType,
    "maskfile": typing.NotRequired[InputPathType | None],
    "qvalue": typing.NotRequired[float | None],
    "adjustedimage": typing.NotRequired[str | None],
    "othresh_flag": bool,
    "order_flag": bool,
    "oneminusp_flag": bool,
    "positive_corr_flag": bool,
    "independent_flag": bool,
    "conservative_flag": bool,
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
        "fdr": fdr_cargs,
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
        "fdr": fdr_outputs,
    }.get(t)


class FdrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fdr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_adjusted: OutputPathType | None
    """Output FDR-adjusted p-values image"""
    output_thresholded: OutputPathType
    """Thresholded output p-value image"""
    output_order: OutputPathType
    """Output order values image"""


def fdr_params(
    infile: InputPathType,
    maskfile: InputPathType | None = None,
    qvalue: float | None = None,
    adjustedimage: str | None = None,
    othresh_flag: bool = False,
    order_flag: bool = False,
    oneminusp_flag: bool = False,
    positive_corr_flag: bool = False,
    independent_flag: bool = False,
    conservative_flag: bool = False,
    debug_flag: bool = False,
    verbose_flag: bool = False,
) -> FdrParameters:
    """
    Build parameters.
    
    Args:
        infile: Input p-value image file.
        maskfile: Mask image file.
        qvalue: Q-value (FDR) threshold.
        adjustedimage: Output image with FDR-adjusted p-values.
        othresh_flag: Output a thresholded p-value image.
        order_flag: Output image of order values.
        oneminusp_flag: Treat input as 1-p (also save output like this).
        positive_corr_flag: Use FDR correction factor that assumes positive\
            correlation.
        independent_flag: Use FDR correction factor that assumes independence.
        conservative_flag: Use conservative FDR correction factor (allows for\
            any correlation).
        debug_flag: Switch on debugging output.
        verbose_flag: Switch on diagnostic messages.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fdr",
        "infile": infile,
        "othresh_flag": othresh_flag,
        "order_flag": order_flag,
        "oneminusp_flag": oneminusp_flag,
        "positive_corr_flag": positive_corr_flag,
        "independent_flag": independent_flag,
        "conservative_flag": conservative_flag,
        "debug_flag": debug_flag,
        "verbose_flag": verbose_flag,
    }
    if maskfile is not None:
        params["maskfile"] = maskfile
    if qvalue is not None:
        params["qvalue"] = qvalue
    if adjustedimage is not None:
        params["adjustedimage"] = adjustedimage
    return params


def fdr_cargs(
    params: FdrParameters,
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
    cargs.append("fdr")
    cargs.extend([
        "-i",
        execution.input_file(params.get("infile"))
    ])
    if params.get("maskfile") is not None:
        cargs.extend([
            "-m",
            execution.input_file(params.get("maskfile"))
        ])
    if params.get("qvalue") is not None:
        cargs.extend([
            "-q",
            str(params.get("qvalue"))
        ])
    if params.get("adjustedimage") is not None:
        cargs.extend([
            "-a",
            params.get("adjustedimage")
        ])
    if params.get("othresh_flag"):
        cargs.append("--othresh")
    if params.get("order_flag"):
        cargs.append("--order")
    if params.get("oneminusp_flag"):
        cargs.append("--oneminusp")
    if params.get("positive_corr_flag"):
        cargs.append("--positivecorr")
    if params.get("independent_flag"):
        cargs.append("--independent")
    if params.get("conservative_flag"):
        cargs.append("--conservative")
    if params.get("debug_flag"):
        cargs.append("--debug")
    if params.get("verbose_flag"):
        cargs.append("-v")
    return cargs


def fdr_outputs(
    params: FdrParameters,
    execution: Execution,
) -> FdrOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FdrOutputs(
        root=execution.output_file("."),
        output_adjusted=execution.output_file(params.get("adjustedimage") + ".nii.gz") if (params.get("adjustedimage") is not None) else None,
        output_thresholded=execution.output_file(pathlib.Path(params.get("infile")).name + "_thr.nii.gz"),
        output_order=execution.output_file(pathlib.Path(params.get("infile")).name + "_order.nii.gz"),
    )
    return ret


def fdr_execute(
    params: FdrParameters,
    execution: Execution,
) -> FdrOutputs:
    """
    False Discovery Rate (FDR) correction tool from FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FdrOutputs`).
    """
    params = execution.params(params)
    cargs = fdr_cargs(params, execution)
    ret = fdr_outputs(params, execution)
    execution.run(cargs)
    return ret


def fdr(
    infile: InputPathType,
    maskfile: InputPathType | None = None,
    qvalue: float | None = None,
    adjustedimage: str | None = None,
    othresh_flag: bool = False,
    order_flag: bool = False,
    oneminusp_flag: bool = False,
    positive_corr_flag: bool = False,
    independent_flag: bool = False,
    conservative_flag: bool = False,
    debug_flag: bool = False,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> FdrOutputs:
    """
    False Discovery Rate (FDR) correction tool from FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        infile: Input p-value image file.
        maskfile: Mask image file.
        qvalue: Q-value (FDR) threshold.
        adjustedimage: Output image with FDR-adjusted p-values.
        othresh_flag: Output a thresholded p-value image.
        order_flag: Output image of order values.
        oneminusp_flag: Treat input as 1-p (also save output like this).
        positive_corr_flag: Use FDR correction factor that assumes positive\
            correlation.
        independent_flag: Use FDR correction factor that assumes independence.
        conservative_flag: Use conservative FDR correction factor (allows for\
            any correlation).
        debug_flag: Switch on debugging output.
        verbose_flag: Switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FdrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FDR_METADATA)
    params = fdr_params(
        infile=infile,
        maskfile=maskfile,
        qvalue=qvalue,
        adjustedimage=adjustedimage,
        othresh_flag=othresh_flag,
        order_flag=order_flag,
        oneminusp_flag=oneminusp_flag,
        positive_corr_flag=positive_corr_flag,
        independent_flag=independent_flag,
        conservative_flag=conservative_flag,
        debug_flag=debug_flag,
        verbose_flag=verbose_flag,
    )
    return fdr_execute(params, execution)


__all__ = [
    "FDR_METADATA",
    "FdrOutputs",
    "FdrParameters",
    "fdr",
    "fdr_params",
]
