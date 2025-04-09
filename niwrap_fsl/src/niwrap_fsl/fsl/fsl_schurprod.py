# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSL_SCHURPROD_METADATA = Metadata(
    id="2b6bc81506dd13e1251f0296c4237340b75a61fe.boutiques",
    name="fsl_schurprod",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


FslSchurprodParameters = typing.TypedDict('FslSchurprodParameters', {
    "__STYX_TYPE__": typing.Literal["fsl_schurprod"],
    "input_file": InputPathType,
    "design_file": InputPathType,
    "output_file": str,
    "regression_flag": bool,
    "index": typing.NotRequired[float | None],
    "mask_file": typing.NotRequired[InputPathType | None],
    "verbose_flag": bool,
    "help_flag": bool,
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
        "fsl_schurprod": fsl_schurprod_cargs,
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
        "fsl_schurprod": fsl_schurprod_outputs,
    }.get(t)


class FslSchurprodOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_schurprod(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_matrix_product: OutputPathType
    """Generated matrix product output file"""


def fsl_schurprod_params(
    input_file: InputPathType,
    design_file: InputPathType,
    output_file: str,
    regression_flag: bool = False,
    index: float | None = None,
    mask_file: InputPathType | None = None,
    verbose_flag: bool = False,
    help_flag: bool = False,
) -> FslSchurprodParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input file name (4D image file).
        design_file: ASCII text matrix of time series to be correlated.
        output_file: Output file base name.
        regression_flag: Use regression rather than correlation.
        index: Index of column in the design to be used for matrix product\
            calculation.
        mask_file: Mask image file name.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display this help text.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fsl_schurprod",
        "input_file": input_file,
        "design_file": design_file,
        "output_file": output_file,
        "regression_flag": regression_flag,
        "verbose_flag": verbose_flag,
        "help_flag": help_flag,
    }
    if index is not None:
        params["index"] = index
    if mask_file is not None:
        params["mask_file"] = mask_file
    return params


def fsl_schurprod_cargs(
    params: FslSchurprodParameters,
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
    cargs.append("fsl_schurprod")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_file"))
    ])
    cargs.extend([
        "-d",
        execution.input_file(params.get("design_file"))
    ])
    cargs.extend([
        "-o",
        params.get("output_file")
    ])
    if params.get("regression_flag"):
        cargs.append("-r")
    if params.get("index") is not None:
        cargs.extend([
            "-i",
            str(params.get("index"))
        ])
    if params.get("mask_file") is not None:
        cargs.extend([
            "-m",
            execution.input_file(params.get("mask_file"))
        ])
    if params.get("verbose_flag"):
        cargs.append("-v")
    if params.get("help_flag"):
        cargs.append("-h")
    return cargs


def fsl_schurprod_outputs(
    params: FslSchurprodParameters,
    execution: Execution,
) -> FslSchurprodOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslSchurprodOutputs(
        root=execution.output_file("."),
        output_matrix_product=execution.output_file(params.get("output_file") + ".nii.gz"),
    )
    return ret


def fsl_schurprod_execute(
    params: FslSchurprodParameters,
    execution: Execution,
) -> FslSchurprodOutputs:
    """
    Generates element-wise matrix products or product of matrices against vectors
    from 4D data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslSchurprodOutputs`).
    """
    params = execution.params(params)
    cargs = fsl_schurprod_cargs(params, execution)
    ret = fsl_schurprod_outputs(params, execution)
    execution.run(cargs)
    return ret


def fsl_schurprod(
    input_file: InputPathType,
    design_file: InputPathType,
    output_file: str,
    regression_flag: bool = False,
    index: float | None = None,
    mask_file: InputPathType | None = None,
    verbose_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> FslSchurprodOutputs:
    """
    Generates element-wise matrix products or product of matrices against vectors
    from 4D data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: Input file name (4D image file).
        design_file: ASCII text matrix of time series to be correlated.
        output_file: Output file base name.
        regression_flag: Use regression rather than correlation.
        index: Index of column in the design to be used for matrix product\
            calculation.
        mask_file: Mask image file name.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display this help text.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslSchurprodOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_SCHURPROD_METADATA)
    params = fsl_schurprod_params(
        input_file=input_file,
        design_file=design_file,
        output_file=output_file,
        regression_flag=regression_flag,
        index=index,
        mask_file=mask_file,
        verbose_flag=verbose_flag,
        help_flag=help_flag,
    )
    return fsl_schurprod_execute(params, execution)


__all__ = [
    "FSL_SCHURPROD_METADATA",
    "FslSchurprodOutputs",
    "FslSchurprodParameters",
    "fsl_schurprod",
    "fsl_schurprod_params",
]
