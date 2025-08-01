# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSLMEANTS_METADATA = Metadata(
    id="713a470928670ea0baa7642933e8a1bb7a9199d2.boutiques",
    name="fslmeants",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


FslmeantsParameters = typing.TypedDict('FslmeantsParameters', {
    "__STYXTYPE__": typing.Literal["fslmeants"],
    "input_image": InputPathType,
    "output": typing.NotRequired[str | None],
    "mask": typing.NotRequired[InputPathType | None],
    "coordinates": typing.NotRequired[list[float] | None],
    "usemm_flag": bool,
    "showall_flag": bool,
    "eigenv_flag": bool,
    "eigenvariates_order": typing.NotRequired[float | None],
    "no_bin_flag": bool,
    "label_image": typing.NotRequired[InputPathType | None],
    "transpose_flag": bool,
    "weighted_mean_flag": bool,
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
        "fslmeants": fslmeants_cargs,
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
        "fslmeants": fslmeants_outputs,
    }.get(t)


class FslmeantsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslmeants(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_text_matrix: OutputPathType | None
    """Output text matrix from fslmeants"""


def fslmeants_params(
    input_image: InputPathType,
    output: str | None = None,
    mask: InputPathType | None = None,
    coordinates: list[float] | None = None,
    usemm_flag: bool = False,
    showall_flag: bool = False,
    eigenv_flag: bool = False,
    eigenvariates_order: float | None = None,
    no_bin_flag: bool = False,
    label_image: InputPathType | None = None,
    transpose_flag: bool = False,
    weighted_mean_flag: bool = False,
    verbose_flag: bool = False,
    help_flag: bool = False,
) -> FslmeantsParameters:
    """
    Build parameters.
    
    Args:
        input_image: Input 4D image.
        output: Output text matrix.
        mask: Input 3D mask.
        coordinates: Requested spatial coordinate (instead of mask). Must have\
            exactly three numerical entries in the list (3-vector).
        usemm_flag: Use mm instead of voxel coordinates (for -c option).
        showall_flag: Show all voxel time series (within mask) instead of\
            averaging.
        eigenv_flag: Calculate Eigenvariate(s) instead of mean (output will\
            have 0 mean).
        eigenvariates_order: Select number of Eigenvariates (default 1).
        no_bin_flag: Do not binarise the mask for calculation of Eigenvariates.
        label_image: Input 3D label image (generate separate mean for each\
            integer label value - cannot be used with showall).
        transpose_flag: Output results in transpose format (one row per\
            voxel/mean).
        weighted_mean_flag: Output weighted mean, using mask values as weights,\
            and exit.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display the help message.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslmeants",
        "input_image": input_image,
        "usemm_flag": usemm_flag,
        "showall_flag": showall_flag,
        "eigenv_flag": eigenv_flag,
        "no_bin_flag": no_bin_flag,
        "transpose_flag": transpose_flag,
        "weighted_mean_flag": weighted_mean_flag,
        "verbose_flag": verbose_flag,
        "help_flag": help_flag,
    }
    if output is not None:
        params["output"] = output
    if mask is not None:
        params["mask"] = mask
    if coordinates is not None:
        params["coordinates"] = coordinates
    if eigenvariates_order is not None:
        params["eigenvariates_order"] = eigenvariates_order
    if label_image is not None:
        params["label_image"] = label_image
    return params


def fslmeants_cargs(
    params: FslmeantsParameters,
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
    cargs.append("fslmeants")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_image"))
    ])
    if params.get("output") is not None:
        cargs.extend([
            "-o",
            params.get("output")
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "-m",
            execution.input_file(params.get("mask"))
        ])
    if params.get("coordinates") is not None:
        cargs.extend([
            "-c",
            *map(str, params.get("coordinates"))
        ])
    if params.get("usemm_flag"):
        cargs.append("--usemm")
    if params.get("showall_flag"):
        cargs.append("--showall")
    if params.get("eigenv_flag"):
        cargs.append("--eig")
    if params.get("eigenvariates_order") is not None:
        cargs.extend([
            "--order",
            str(params.get("eigenvariates_order"))
        ])
    if params.get("no_bin_flag"):
        cargs.append("--no_bin")
    if params.get("label_image") is not None:
        cargs.extend([
            "--label",
            execution.input_file(params.get("label_image"))
        ])
    if params.get("transpose_flag"):
        cargs.append("--transpose")
    if params.get("weighted_mean_flag"):
        cargs.append("-w")
    if params.get("verbose_flag"):
        cargs.append("-v")
    if params.get("help_flag"):
        cargs.append("-h")
    return cargs


def fslmeants_outputs(
    params: FslmeantsParameters,
    execution: Execution,
) -> FslmeantsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslmeantsOutputs(
        root=execution.output_file("."),
        output_text_matrix=execution.output_file(params.get("output")) if (params.get("output") is not None) else None,
    )
    return ret


def fslmeants_execute(
    params: FslmeantsParameters,
    execution: Execution,
) -> FslmeantsOutputs:
    """
    Prints average timeseries (intensities) to the screen (or saves to a file).
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslmeantsOutputs`).
    """
    params = execution.params(params)
    cargs = fslmeants_cargs(params, execution)
    ret = fslmeants_outputs(params, execution)
    execution.run(cargs)
    return ret


def fslmeants(
    input_image: InputPathType,
    output: str | None = None,
    mask: InputPathType | None = None,
    coordinates: list[float] | None = None,
    usemm_flag: bool = False,
    showall_flag: bool = False,
    eigenv_flag: bool = False,
    eigenvariates_order: float | None = None,
    no_bin_flag: bool = False,
    label_image: InputPathType | None = None,
    transpose_flag: bool = False,
    weighted_mean_flag: bool = False,
    verbose_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> FslmeantsOutputs:
    """
    Prints average timeseries (intensities) to the screen (or saves to a file).
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_image: Input 4D image.
        output: Output text matrix.
        mask: Input 3D mask.
        coordinates: Requested spatial coordinate (instead of mask). Must have\
            exactly three numerical entries in the list (3-vector).
        usemm_flag: Use mm instead of voxel coordinates (for -c option).
        showall_flag: Show all voxel time series (within mask) instead of\
            averaging.
        eigenv_flag: Calculate Eigenvariate(s) instead of mean (output will\
            have 0 mean).
        eigenvariates_order: Select number of Eigenvariates (default 1).
        no_bin_flag: Do not binarise the mask for calculation of Eigenvariates.
        label_image: Input 3D label image (generate separate mean for each\
            integer label value - cannot be used with showall).
        transpose_flag: Output results in transpose format (one row per\
            voxel/mean).
        weighted_mean_flag: Output weighted mean, using mask values as weights,\
            and exit.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display the help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslmeantsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLMEANTS_METADATA)
    params = fslmeants_params(
        input_image=input_image,
        output=output,
        mask=mask,
        coordinates=coordinates,
        usemm_flag=usemm_flag,
        showall_flag=showall_flag,
        eigenv_flag=eigenv_flag,
        eigenvariates_order=eigenvariates_order,
        no_bin_flag=no_bin_flag,
        label_image=label_image,
        transpose_flag=transpose_flag,
        weighted_mean_flag=weighted_mean_flag,
        verbose_flag=verbose_flag,
        help_flag=help_flag,
    )
    return fslmeants_execute(params, execution)


__all__ = [
    "FSLMEANTS_METADATA",
    "FslmeantsOutputs",
    "FslmeantsParameters",
    "fslmeants",
    "fslmeants_params",
]
